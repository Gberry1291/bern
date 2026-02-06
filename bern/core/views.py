from django.shortcuts import render, redirect
from core.forms import LivingOptionSearchForm
from core.search import search_living_options
from django.utils import translation
from django.http import JsonResponse
from core.embeddings import generate_embedding
from core.feedback import get_click_boosts, get_feedback_adjustments
from django.views.decorators.http import require_POST
from core.models import SearchClick, SearchEvent, LivingOption, SearchImpression
from core.feedback import get_feedback_adjustments


CARE_TARGET_MAP = {
    "low": 1,
    "medium": 3,
    "high": 5,
}

def livingoption_search(request):
    lang = (request.COOKIES.get("django_language") or request.session.get("ui_lang") or "de").lower()
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

    translation.activate(lang)


    is_partial = request.headers.get("X-Partial") == "results"
    query = request.GET.get("q", "").strip()
    wheelchair_raw = request.GET.get("wheelchair")
    care_target_key = request.GET.get("care_target")
    language_filter = request.GET.getlist("language")
    if not language_filter:
        language_filter = None
    print(language_filter)

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
        boosts, penalties = get_feedback_adjustments(query_embedding, lang=lang)

        results = search_living_options(
            user_text=query,
            lang=lang,
            wheelchair_required=wheelchair_required,
            care_target=care_target,
            languages=language_filter,
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
                lang=lang,
                wheelchair_required=((wheelchair_raw.lower() in ("true","1","on","yes")) if wheelchair_raw else None),
                care_target=care_target,
                language_filter=language_filter,
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
        "ui_lang": lang,
        "care_target": care_target_key,
        "wheelchair": wheelchair_raw,
        "language_filter": language_filter,
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
