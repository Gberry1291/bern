from django.shortcuts import render, redirect, get_object_or_404
from core.forms import LivingOptionSearchForm,ProviderRegistrationForm,ProviderEditForm,LivingOptionCreateForm,LivingOptionEditForm
from core.search import search_living_options
from django.utils import translation,timezone
from django.http import JsonResponse
from core.embeddings import generate_embedding
from core.feedback import get_click_boosts, get_feedback_adjustments
from django.views.decorators.http import require_POST
from core.models import SearchClick, SearchEvent, LivingOption, SearchImpression,Provider,ProviderMagicLink
from core.feedback import get_feedback_adjustments
from django.utils.translation import get_language
from django.utils.translation import gettext as _
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
import re

from .models import Provider

CARE_TARGET_MAP = {
    "low": 1,
    "medium": 3,
    "high": 5,
}

def livingoption_search(request):
    ui_lang = (request.COOKIES.get("django_language") or request.session.get("ui_lang") or "de").lower()
    if ui_lang.startswith("en"):
        ui_lang = "en"
    elif ui_lang.startswith("de"):
        ui_lang = "de"
    elif ui_lang.startswith("fr"):
        ui_lang = "fr"
    elif ui_lang.startswith("it"):
        ui_lang = "it"
    else:
        ui_lang = "de"

    translation.activate(ui_lang)


    is_partial = request.headers.get("X-Partial") == "results"
    query = request.GET.get("q", "").strip()
    wheelchair_raw = request.GET.get("wheelchair")
    care_target_key = request.GET.get("care_target")
    language_filter = request.GET.getlist("language")
    age_raw = request.GET.get("age", "").strip()
    age = int(age_raw) if age_raw.isdigit() else None
    age = age or extract_age_from_text(query)
    if not language_filter:
        language_filter = None
    search_lang = (language_filter[0] if language_filter else ui_lang)

    CARE_TARGET_MAP = {"low": 1, "medium": 3, "high": 5}
    care_target = CARE_TARGET_MAP.get(care_target_key)

    wheelchair_required = None
    if wheelchair_raw is not None:
        wheelchair_required = wheelchair_raw.lower() in ("true", "1", "on", "yes")

    results = []
    best_results = []
    other_results = []
    display_results = []
    search_event_id = None

    if is_partial:
        return render(request, "core/_search_form_and_results.html", context)

    if query:
        query_embedding = generate_embedding(query)
        boosts, penalties = get_feedback_adjustments(query_embedding, lang=search_lang)

        results = search_living_options(
            user_text=query,
            lang=search_lang,
            languages=language_filter or None,
            wheelchair_required=wheelchair_required,
            care_target=care_target,
            age=age,
            click_boosts=boosts,
            skip_penalties=penalties,
        )

        # Split for display
        best_results = [r for r in results if r.get("tier") == "best"][:5]
        other_results = [r for r in results if r.get("tier") != "best"][:3]

        # Only log feedback on FULL page loads, not partial swaps
        if not is_partial:
            ev = SearchEvent.objects.create(
                query=query,
                lang=search_lang,
                wheelchair_required=((wheelchair_raw.lower() in ("true","1","on","yes")) if wheelchair_raw else None),
                care_target=care_target,
                language_filter=search_lang,
                query_embedding=query_embedding,
            )
            search_event_id = ev.id

        # Global ranks for click/skip signals
        display_results = best_results + other_results
        for i, r in enumerate(display_results):
            r["rank"] = i

        # Log impressions so clicks can mark "skipped above"
        SearchImpression.objects.bulk_create(
            [
                SearchImpression(
                    event=ev,
                    living_option=r["option"],
                    rank_shown=r["rank"],
                )
                for r in display_results
            ],
            ignore_conflicts=True,
        )
    else:
        pass


    for i, r in enumerate(display_results):
        r["rank"] = i

    impressions = [
        SearchImpression(event=ev, living_option=r["option"], rank_shown=r["rank"])
        for r in display_results
    ]


    context = {
        "query": query,
        "ui_lang": ui_lang,
        "search_lang": search_lang,
        "language_filter": language_filter,
        "care_target": care_target_key,
        "wheelchair": wheelchair_raw,
        "results": results,
        "best_results": best_results,
        "other_results": other_results,
        "search_event_id": search_event_id,
        "display_results":display_results,
    }

    partial = request.headers.get("X-Partial")

    if partial == "page":
        return render(request, "core/_page_partial.html", context)

    if partial == "results":
        return render(request, "core/_results_container.html", context)

    return render(request, "core/search.html", context)


def set_ui_language(request):
    if request.method != "POST":
        return JsonResponse({"ok": False, "error": "POST required"}, status=405)

    lang = (request.POST.get("ui_lang") or "de").lower()
    if lang.startswith("en"):
        lang = "en"
    elif lang.startswith("de"):
        lang = "de"
    elif lang.startswith("fr"):
        lang = "fr"
    elif lang.startswith("it"):
        lang = "it"
    else:
        lang = "de"

    request.session["ui_lang"] = lang
    translation.activate(lang)

    resp = JsonResponse({"ok": True, "ui_lang": lang})
    resp.set_cookie("django_language", lang)  # optional but helpful
    return resp

@require_POST
def track_click(request):
    try:
        event_id = int(request.POST.get("event_id"))
        option_id = int(request.POST.get("option_id"))
        rank = int(request.POST.get("rank"))
    except (TypeError, ValueError):
        return JsonResponse({"ok": False, "error": "bad params"}, status=400)

    # verify objects exist
    if not SearchEvent.objects.filter(id=event_id).exists():
        return JsonResponse({"ok": False, "error": "event not found"}, status=404)
    if not LivingOption.objects.filter(id=option_id).exists():
        return JsonResponse({"ok": False, "error": "option not found"}, status=404)

    SearchClick.objects.create(event_id=event_id, living_option_id=option_id, rank_shown=rank)

    SearchImpression.objects.filter(
        event_id=event_id,
        living_option_id=option_id
    ).update(clicked=True)

    # Mark skipped impressions: anything ranked ABOVE the clicked item
    SearchImpression.objects.filter(
        event_id=event_id,
        rank_shown__lt=rank,
    ).exclude(
        living_option_id=option_id
    ).update(skipped=True)

    return JsonResponse({"ok": True})

def provider_detail(request, pk: int):
    provider = get_object_or_404(Provider, pk=pk)

    # Simple helpers for display
    support_levels = []
    if getattr(provider, "support_level_low", False):
        support_levels.append("Low")
    if getattr(provider, "support_level_medium", False):
        support_levels.append("Medium")
    if getattr(provider, "support_level_high", False):
        support_levels.append("High")

    context = {
        "provider": provider,
        "support_levels": support_levels,
    }
    return render(request, "core/provider_detail.html", context)

def saved_list(request):
    ids_str = request.GET.get("ids", "").strip()
    ids = []
    if ids_str:
        for part in ids_str.split(","):
            part = part.strip()
            if part.isdigit():
                ids.append(int(part))

    lang = (get_language() or "de")[:2]

    qs = (
        LivingOption.objects
        .filter(id__in=ids)
        .select_related("provider")
        .prefetch_related("translations")
    )

    # Preserve order
    options_by_id = {o.id: o for o in qs}
    ordered = [options_by_id[i] for i in ids if i in options_by_id]

    return render(request, "core/saved.html", {"options": ordered, "ids": ids, "ui_lang": lang})

def provider_register(request):
    if request.method == "POST":
        form = ProviderRegistrationForm(request.POST)
        if form.is_valid():
            provider = form.save(commit=False)
            provider.self_registered = True
            provider.verified = False
            provider.status = "pending"  # key: must be reviewed
            provider.save()
            send_mail(
                subject="New provider submission",
                message=(
                    f"A new provider has submitted a listing.\n\n"
                    f"Name: {provider.name}\n"
                    f"Canton: {provider.canton}\n"
                    f"Self-registered: Yes\n\n"
                    f"Review in admin."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.PROVIDER_NOTIFICATION_EMAIL],
            )
            return redirect("provider_register_thanks")
    else:
        form = ProviderRegistrationForm()

    return render(request, "core/provider_register.html", {"form": form})

def provider_register_thanks(request):
    return render(request, "core/provider_register_thanks.html")

def provider_manage_search(request):
    q = (request.GET.get("q") or "").strip()
    canton = (request.GET.get("canton") or "").strip()

    providers = Provider.objects.all().order_by("name")

    if q:
        providers = providers.filter(name__icontains=q)

    if canton:
        providers = providers.filter(canton__iexact=canton)

    # Keep it lightweight (avoid huge lists)
    providers = providers[:30] if (q or canton) else []

    return render(request, "core/provider_manage_search.html", {
        "q": q,
        "canton": canton,
        "providers": providers,
    })

def provider_manage_request(request, pk: int):
    provider = get_object_or_404(Provider, pk=pk)

    if request.method == "POST":
        email = (request.POST.get("email") or "").strip()

        # MVP: just store a note for admin review (no email sending yet)
        if email:
            # If you added review_notes/status earlier:
            note = f"Manage request from: {email}"
            if getattr(provider, "review_notes", None) is not None:
                provider.review_notes = (provider.review_notes + "\n" + note).strip()
                provider.save(update_fields=["review_notes"])
            # You can also create a separate model later (ProviderManageRequest)
            admin_url = f"https://www.roman-wyss.com/admin/yourapp/provider/{provider.id}/change/"
            send_mail(
                subject="Provider access request",
                message=(
                    f"A provider has requested access to manage a listing.\n\n"
                    f"Provider: {provider.name}\n"
                    f"Canton: {provider.canton}\n"
                    f"Requested by: {email}\n\n"
                    f"Review in admin.\n"
                    f"Admin link:\n"
                    f"{admin_url}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.PROVIDER_NOTIFICATION_EMAIL],
            )
            return redirect("provider_register_thanks")  # reuse a thanks page for now

    return render(request, "core/provider_manage_request.html", {"provider": provider})

SESSION_KEY_PROVIDER_ID = "provider_edit_provider_id"
SESSION_KEY_EXPIRES = "provider_edit_expires_at"

def provider_manage_request(request, pk: int):
    provider = get_object_or_404(Provider, pk=pk)

    if request.method == "POST":
        email = (request.POST.get("email") or "").strip().lower()

        provider_email = (provider.contact_email or "").strip().lower()

        if not provider_email:
            # Provider has no email on file → manual review only
            return render(request, "core/provider_manage_request.html", {
                "provider": provider,
                "error": _("This listing does not have a contact email on file. Please contact us directly."),
            })

        if email != provider_email:
            return render(request, "core/provider_manage_request.html", {
                "provider": provider,
                "error": _("Please use the email address associated with this organization."),
            })

        # Create and send magic link (1 hour)
        raw_token, _obj = ProviderMagicLink.create_link(provider=provider, email=email, ttl_minutes=60)
        link = f"{settings.SITE_URL}/providers/magic/{raw_token}/"

        # Email to provider
        send_mail(
            subject="Access link to manage your listing",
            message=(
                f"Here is your secure link to update your listing for:\n"
                f"{provider.name}\n\n"
                f"Open this link (valid for 60 minutes):\n{link}\n\n"
                f"If you did not request this, you can ignore this email."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )

        # Optional: notify you too
        if getattr(settings, "PROVIDER_NOTIFICATION_EMAIL", ""):
            send_mail(
                subject="Provider magic-link sent",
                message=f"Magic-link sent to {email} for provider {provider.name} (id={provider.id}).",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.PROVIDER_NOTIFICATION_EMAIL],
            )

        return redirect("provider_register_thanks")

    return render(request, "core/provider_manage_request.html", {"provider": provider})

def provider_magic_enter(request, token: str):
    token_hash = ProviderMagicLink.hash_token(token)
    link_obj = get_object_or_404(ProviderMagicLink, token_hash=token_hash)

    if not link_obj.is_valid():
        return render(request, "core/provider_magic_invalid.html", status=400)

    # Mark used (one-time)
    link_obj.used_at = timezone.now()
    link_obj.save(update_fields=["used_at"])

    # Start edit session (60 minutes)
    request.session[SESSION_KEY_PROVIDER_ID] = link_obj.provider_id
    request.session[SESSION_KEY_EXPIRES] = (timezone.now() + timezone.timedelta(minutes=60)).isoformat()

    return redirect("provider_edit_me")

def provider_edit_me(request):
    provider_id = request.session.get(SESSION_KEY_PROVIDER_ID)
    expires_at = request.session.get(SESSION_KEY_EXPIRES)

    if not provider_id or not expires_at:
        return render(request, "core/provider_magic_invalid.html", status=403)

    try:
        expires_dt = timezone.datetime.fromisoformat(expires_at)
        if timezone.is_naive(expires_dt):
            expires_dt = timezone.make_aware(expires_dt, timezone.get_current_timezone())
    except Exception:
        return render(request, "core/provider_magic_invalid.html", status=403)

    if timezone.now() > expires_dt:
        # expire session
        request.session.pop(SESSION_KEY_PROVIDER_ID, None)
        request.session.pop(SESSION_KEY_EXPIRES, None)
        return render(request, "core/provider_magic_invalid.html", status=403)

    provider = get_object_or_404(Provider, pk=provider_id)

    if request.method == "POST":
        form = ProviderEditForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()

            # Recommended moderation behavior:
            # changes require review again
            if hasattr(provider, "status"):
                provider.status = "pending"
                provider.verified = False
                provider.save(update_fields=["status", "verified"])

            return render(request, "core/provider_edit_done.html", {"provider": provider})
    else:
        form = ProviderEditForm(instance=provider)

    options = provider.living_options.all().order_by("-created_at")
    return render(request, "core/provider_edit.html", {"provider": provider, "form": form, "options": options})

def _get_provider_from_edit_session(request):
    provider_id = request.session.get(SESSION_KEY_PROVIDER_ID)
    expires_at = request.session.get(SESSION_KEY_EXPIRES)

    if not provider_id or not expires_at:
        return None

    try:
        expires_dt = timezone.datetime.fromisoformat(expires_at)
        if timezone.is_naive(expires_dt):
            expires_dt = timezone.make_aware(expires_dt, timezone.get_current_timezone())
    except Exception:
        return None

    if timezone.now() > expires_dt:
        request.session.pop(SESSION_KEY_PROVIDER_ID, None)
        request.session.pop(SESSION_KEY_EXPIRES, None)
        return None

    return Provider.objects.filter(pk=provider_id).first()

def livingoption_create(request):
    provider = _get_provider_from_edit_session(request)
    if not provider:
        return render(request, "core/provider_magic_invalid.html", status=403)

    if request.method == "POST":
        form = LivingOptionCreateForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)
            option.provider = provider
            option.save()

            form.instance = option
            form.save(commit=True)

            if hasattr(provider, "status"):
                provider.status = "pending"
                provider.verified = False
                provider.save(update_fields=["status", "verified"])

            return redirect("provider_detail", pk=provider.id)
    else:
        form = LivingOptionCreateForm()

    return render(request, "core/livingoption_create.html", {"provider": provider, "form": form})

def livingoption_edit(request, pk: int):
    provider = _get_provider_from_edit_session(request)
    if not provider:
        return render(request, "core/provider_magic_invalid.html", status=403)

    option = get_object_or_404(LivingOption, pk=pk, provider=provider)

    if request.method == "POST":
        form = LivingOptionEditForm(request.POST, instance=option)
        if form.is_valid():
            form.save(commit=True)  # updates translations + languages_supported
            # optional: mark provider pending again
            if hasattr(provider, "status"):
                provider.status = "pending"
                provider.verified = False
                provider.save(update_fields=["status", "verified"])
            return redirect("provider_edit_me")
    else:
        form = LivingOptionEditForm(instance=option)

    return render(request, "core/livingoption_edit.html", {"provider": provider, "option": option, "form": form})

def livingoption_delete(request, pk: int):
    provider = _get_provider_from_edit_session(request)
    if not provider:
        return render(request, "core/provider_magic_invalid.html", status=403)

    option = get_object_or_404(LivingOption, pk=pk, provider=provider)

    if request.method == "POST":
        option.delete()

        # Optional: mark provider pending again (content changed)
        if hasattr(provider, "status"):
            provider.status = "pending"
            provider.verified = False
            provider.save(update_fields=["status", "verified"])

        return redirect("provider_edit_me")

    return render(request, "core/livingoption_delete_confirm.html", {
        "provider": provider,
        "option": option,
    })

def extract_age_from_text(q: str):
    if not q:
        return None
    m = re.search(r"(?<!\d)(\d{1,3})(?!\d)", q)  # grabs 15, 37, 75 etc.
    if not m:
        return None
    age = int(m.group(1))
    return age if 0 < age < 120 else None

def how_it_works(request):
    ui_lang = (request.COOKIES.get("django_language") or request.session.get("ui_lang") or "de").lower()
    if ui_lang.startswith("en"):
        ui_lang = "en"
    elif ui_lang.startswith("de"):
        ui_lang = "de"
    elif ui_lang.startswith("fr"):
        ui_lang = "fr"
    elif ui_lang.startswith("it"):
        ui_lang = "it"
    else:
        ui_lang = "de"

    translation.activate(ui_lang)

    context = {
        "ui_lang": ui_lang,
    }

    is_partial = request.headers.get("X-Partial") == "page"
    if is_partial:
        print("is partial")
        return render(request, "core/how_partial.html", context)

    return render(request, "core/how_it_works.html", context)
