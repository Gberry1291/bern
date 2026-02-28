import numpy as np
from core.embeddings import generate_embedding
from core.models import LivingOptionEmbedding
from django.utils.translation import gettext as _
from pgvector.django import CosineDistance
from parler.utils.context import switch_language
import re

SUPPORTED_LANGS = {"de", "fr", "it", "en"}
def _contains_term(t: str, term: str) -> bool:
    """
    Safer matching than `term in t`.
    - For 'word-like' terms: require word boundaries
    - For phrases / terms with spaces/dashes: keep substring match
    """
    term = term.strip().lower()
    if not term:
        return False

    # If it's a single word (letters/numbers only), use word boundaries
    if re.fullmatch(r"[a-z0-9äöüß]+", term):
        return re.search(rf"\b{re.escape(term)}\b", t) is not None

    # Otherwise (phrases like "hard of hearing", "low vision", "24/7") substring is fine
    return term in t
def detect_signals(text: str):
    t = (text or "").lower()

    hearing_terms = [
        "hearing", "hard of hearing", "hearing impairment", "deaf",
        "hör", "gehörlos", "hörbeeinträchtigt",
        "audition", "malentendant", "sourd",
        "udito", "ipoacus", "sordo",
    ]
    vision_terms = [
        "blind", "low vision", "visually impaired",
        "blind", "seh", "sehbehindert","blindheit", "blinde", "blinden", "sehbehinderung", "sehschwäche"
        "malvoyant", "aveugle","cécité",
        "cieco", "ipovision","cecità"
    ]
    independent_terms = [
        "independent", "independence",
        "selbstständig", "selbständ", "autonomie",
        "autonomy",
        "autonome",
        "indipendente",
    ]
    coaching_terms = [
        "coaching", "training", "wohntraining",
        "skills", "budget", "appointments", "termine",
        "behörden", "job", "ausbildung",
        "formation", "emploi",
        "lavoro",
    ]
    guide_dog_terms = [
        "guide dog", "service dog", "assistance dog",
        "führhund", "blindenhund",
        "chien guide", "chien d'assistance",
        "cane guida", "cane d’assistenza",
    ]
    no_supervision_terms = [
        "no supervision", "no help", "fully independent", "independent",
        "keine aufsicht", "keine hilfe", "vollständig selbstständig", "ohne betreuung",
    ]
    needs_24_7_terms = ["24/7", "24-7", "round the clock", "rund um die uhr", "around-the-clock", "constant supervision", "ständige aufsicht"]
    adult_terms = ["adult", "adults", "18+", "erwachsene", "adulte"]
    child_terms = ["child", "children", "kid", "kids", "pediatric", "teen", "teenager", "jugend", "kinder", "enfant", "ado"]
    autism_terms = ["autism", "autismus", "autistic", "asperger", "ass", "autismus-spektrum", "spektrum"]
    dementia_terms = ["dementia", "demenz", "alzheimer"]
    schizophrenia_terms = ["schizophrenia", "schizophren"]
    paralysis_terms = ["paralyzed", "paralys", "quadripleg", "tetrapleg"]
    wheelchair_terms = ["wheelchair", "rollstuhl", "fauteuil", "sedia a rotelle"]
    adl_support_terms = [
    "haushalt", "putzen", "waschen", "kochen",
    "einkaufen", "alltag", "treppe schaffe ich nicht",
    "schaffe", "nicht mehr alleine", "alleine nicht mehr"
]

    return {
        "hearing": any(_contains_term(t, w) for w in hearing_terms),
        "vision": any(_contains_term(t, w) for w in vision_terms),
        "independent_living": any(_contains_term(t, w) for w in independent_terms),
        "skills_coaching": any(_contains_term(t, w) for w in coaching_terms),
        "needs_24_7": any(_contains_term(t, w) for w in needs_24_7_terms),
        "mentions_adult": any(_contains_term(t, w) for w in adult_terms),
        "mentions_child": any(_contains_term(t, w) for w in child_terms),
        "autism": any(_contains_term(t, w) for w in autism_terms),
        "dementia": any(_contains_term(t, w) for w in dementia_terms),
        "schizophrenia": any(_contains_term(t, w) for w in schizophrenia_terms),
        "epilepsy": any(_contains_term(t, w) for w in ["epilepsy", "epileps"]),
        "paralysis": any(_contains_term(t, w) for w in paralysis_terms),
        "guide_dog": any(_contains_term(t, w) for w in guide_dog_terms),
        "wheelchair":any(_contains_term(t, w) for w in wheelchair_terms),
        "no_supervision": any(w in t for w in no_supervision_terms),
        "adl_support": any(_contains_term(t, w) for w in adl_support_terms),
    }
def _has_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text) for p in patterns)
def apply_condition_rules(
    query_text: str,
    signals: dict,
    listing,
    title_text: str = "",
    description_text: str = "",
    age: int | None = None,
):
    """
    Returns (delta_score: float, extra_reasons: list[str])

    Handles:
    - Medical/specific conditions (boost + specialist penalty)
    - Sensory structured flags
    - Mental-health clustering
    - Mobility preferences
    - Independent/coaching bias
    - 24/7 intent
    """

    q = (query_text or "").lower()
    lt = f"{title_text or ''}\n{description_text or ''}".lower()

    def mentions_any(text: str, terms: list[str]) -> bool:
        return any(_contains_term(text, term) for term in terms)

    delta = 0.0
    reasons = []

    #-------------------------
    # Mental Health Cluster
    # -------------------------
    MH_DIAG_QUERY = ["angst", "panik", "ptbs", "trauma", "zwang", "psychose", "depress", "bipolar", "schizo", "borderline"]
    MH_DIAG_LISTING = MH_DIAG_QUERY + ["krisenintervention", "tagesstruktur", "psychiatr", "dbt"]

    if mentions_any(q, MH_DIAG_QUERY) and mentions_any(lt, MH_DIAG_LISTING):
        delta += 0.12
    clinic_terms = ["klinik", "krise", "krisen", "intervention", "psychiatr"]
    if not mentions_any(q, clinic_terms) and mentions_any(lt, clinic_terms):
        delta -= 0.12
    # --------------------
    # Offtopic specialist demotion
    # --------------------
    SPECIALIST_TOPICS = [
        ("eating_disorder", ["eating", "essstör", "essens", "anorex", "bulim"], 0.10),
        ("bipolar", ["bipolar"], 0.10),
        # add more only when you have real data coverage
    ]
    for topic_key, terms, penalty in SPECIALIST_TOPICS:
        user_mentions = mentions_any(q, terms)
        listing_mentions = mentions_any(lt, terms)
        if listing_mentions and not user_mentions:
            delta -= penalty
    # -------------------------
    # Condition Matching Loop
    # -------------------------
    CONDITION_RULES = [
        ("schizophrenia", ["schizophrenia", "schizophren"], 0.35, 0.15, _("Matches schizophrenia support")),
        ("epilepsy", ["epilepsy", "epileps"], 0.42, 0.10, _("Matches epilepsy support")),
        ("autism", ["autism", "autismus", "autistic"], 0.30, 0.08, _("Matches autism support")),
        ("dementia", ["dementia", "demenz", "alzheimer"], 0.30, 0.10, _("Matches dementia support")),
        ("paralysis", ["paralyzed", "paralys", "quadripleg", "tetrapleg", "querschnitt"], 0.25, 0.06, _("Matches paralysis support")),
    ]
    for key, terms, boost, penalty, reason in CONDITION_RULES:
        user_mentions = bool(signals.get(key)) or mentions_any(q, terms)
        listing_mentions = mentions_any(lt, terms)

        if user_mentions and listing_mentions:
            delta += boost
            reasons.append(reason)

        elif listing_mentions and not user_mentions:
            # specialist penalty
            delta -= penalty * 1.4  # slightly stronger demotion for irrelevant specialists
    # -------------------------
    # House-hold cues
    # -------------------------
    adl_query = ["haushalt", "alltag", "putzen", "waschen", "wäsche", "kochen", "einkaufen", "haushaltshilfe","überfordert", "schaffe es nicht mehr" , "komme nicht mehr nach"]
    adl_listing = ["haushalt", "alltag", "haushalts", "alltags", "kochen", "einkaufen", "reinigung", "putz", "wäsche"]

    if mentions_any(q, adl_query):
        care_level = getattr(listing, "care_level", None)

        # Prefer moderate-to-higher support when ADL is mentioned
        if care_level is not None:
            if care_level >= 3:
                delta += 0.18
                reasons.append(_("Help with daily living"))
            elif care_level <= 2:
                delta -= 0.06

        # Extra boost if listing explicitly talks about day-to-day help
        if mentions_any(lt, adl_listing):
            delta += 0.10
            reasons.append(_("Practical household support"))
    #------------------------
    # memory conditions
    #------------------------
    memory_cues = ["vergisst", "vergessen", "gedächtnis", "orientierung", "verwirrt", "memory", "forget"]
    if mentions_any(q, memory_cues):
        if mentions_any(lt, ["demenz", "alzheimer", "mci", "mild cognitive", "gedächtnis", "memory", "orientierungshilfen"]):
            delta += 0.18
            reasons.append(_("Memory/cognitive support"))
    if mentions_any(q, memory_cues):
        if getattr(listing, "care_level", 1) <= 2 and mentions_any(lt, ["selbstmanagement", "wohntraining", "coaching"]):
            delta -= 0.12
    # -------------------------
    # Sensory Structured Fields
    # -------------------------
    vision_terms = ["blind", "low vision", "visually impaired", "sehbehindert", "malvoyant", "aveugle", "cieco"]
    hearing_terms = ["deaf", "hard of hearing", "hör", "gehörlos", "sourd", "malentendant", "sordo"]

    # Vision
    vision_requested = signals.get("vision") or mentions_any(q, vision_terms)
    if vision_requested:
        if getattr(listing, "visual_support", False):
            delta += 0.30
            reasons.append(_("Visual support available"))
        else:
            delta -= 0.20
    elif getattr(listing, "visual_support", False):
        delta -= 0.08  # prevent vision from hijacking queries

    blind_terms = ["blind", "blinden", "sehbehind", "low vision", "malvoy", "aveug", "ciec"]
    if vision_requested and mentions_any(lt, blind_terms):
        delta += 0.18
        reasons.append(_("Vision-focused listing"))

    if vision_requested and mentions_any(lt, ["tactile", "taktil", "orientierung", "leitlinie", "braille", "beschilderung"]):
        delta += 0.12
        reasons.append(_("Orientation/tactile aids"))
    # Hearing
    hearing_requested = signals.get("hearing") or mentions_any(q, hearing_terms)
    if hearing_requested:
        if getattr(listing, "hearing_support", False):
            delta += 0.18
            reasons.append(_("Hearing support available"))
        else:
            delta -= 0.10
    elif getattr(listing, "hearing_support", False):
        delta -= 0.08
    # -------------------------
    # Mobility Logic
    # -------------------------
    wheelchair_requested = (
        signals.get("paralysis") or signals.get("wheelchair")
    )

    if wheelchair_requested:
        if getattr(listing, "wheelchair_accessible", False):
            if listing.care_level is not None and listing.care_level <= 2:
                delta += 0.15  # independent wheelchair housing preference
        else:
            delta -= 0.15

        # discourage sensory specialist bleed
        if getattr(listing, "visual_support", False) and not vision_requested:
            delta -= 0.08
    # -------------------------
    # push down vision if epilepsy
    # -------------------------
    if (signals.get("epilepsy") or "epileps" in q) and getattr(listing, "visual_support", False) and not vision_requested:
        delta -= 0.05
    # -------------------------
    # Guide Dog
    # -------------------------
    guide_terms = ["guide-dog", "guide dog", "führhund", "blindenhund", "chien guide", "cane guida"]
    if (vision_requested or signals.get("guide_dog") or mentions_any(q, guide_terms)) and mentions_any(lt, guide_terms):
        delta += 0.10
        reasons.append(_("Guide-dog friendly"))
    # -------------------------
    # Independent Living Bias
    # -------------------------
    if signals.get("independent_living") or signals.get("skills_coaching"):
        care_level = getattr(listing, "care_level", None)
        if care_level is not None:
            if care_level <= 2:
                delta += 0.18
                reasons.append(_("Independent living focus"))
            elif care_level >= 4:
                delta -= 0.12

        coaching_cues = ["budget", "kochen", "termine", "behörden", "job", "ausbildung", "wohntraining", "coaching"]
        if mentions_any(lt, coaching_cues):
            delta += 0.12
            reasons.append(_("Coaching for daily living"))

        # NEW: if user explicitly wants NO supervision, punish “coaching/support” vibes a bit
        if signals.get("no_supervision"):
            if care_level is not None and care_level >= 2:
                delta -= (listing.care_level - 1) * 0.05  # pushes down “semi-supported” places
            if mentions_any(lt, coaching_cues):
                delta -= 0.10  # coaching is not what they asked for
    # -------------------------
    # push down high carelevel results if independent
    # -------------------------
    if signals.get("no_supervision") or (signals.get("independent_living") and not signals.get("needs_24_7")):
        care_level = getattr(listing, "care_level", None)
        if care_level is not None:
            if care_level >= 4:
                delta -= 0.35   # strong push down
            elif care_level == 3:
                delta -= 0.15   # mild push down
    # -------------------------
    # 24/7 Supervision Intent
    # -------------------------
    if signals.get("needs_24_7"):
        twentyfour_terms = [
            "24/7", "24-7", "around-the-clock",
            "rund-um-die-uhr", "rund um die uhr",
            "constant supervision", "ständige aufsicht"
        ]
        care_level = getattr(listing, "care_level", None)
        if mentions_any(lt, twentyfour_terms):
            delta += 0.25
            reasons.append(_("24/7 support"))
        elif care_level is not None and care_level >= 4:
            delta += 0.10
        else:
            delta -= 0.18
    # --------------------
    # Adult vs child mismatch penalty
    # --------------------
    if signals.get("mentions_adult") and not signals.get("mentions_child"):
        child_markers = [
            "ages", "age restriction", "children", "kids", "pediatric", "teen",
            "jugend", "kinder", "enfants", "ado"
        ]
        if any(m in lt for m in child_markers):
            delta -= 0.35
            reasons.append(_("Not for your age group"))
    # -------------------------
    # Age-restriction soft bias
    # -------------------------
    if age is None:
        age_restricted = False

        # 1️⃣ Structured field check (preferred source of truth)
        if getattr(listing, "min_age", None):
            if listing.min_age >= 55:
                age_restricted = True

        # 2️⃣ Fallback: textual hints
        senior_markers = ["55+", "60+", "65+", "70+"]
        if not age_restricted:  # avoid double-trigger
            if any(marker in lt for marker in senior_markers):
                age_restricted = True

        if age_restricted:
            delta -= 0.05
    # --------------------
    # If user did NOT indicate child intent, softly demote child/teen listings
    # --------------------
    child_markers = ["ages", "age restriction", "children", "kids", "pediatric", "teen", "jugend", "kinder", "enfants", "ado"]
    if not signals.get("mentions_child"):
        if any(m in lt for m in child_markers):
            delta -= 0.22
    # -------------------------
    # Clean Reasons
    # -------------------------
    seen = set()
    unique = []
    for r in reasons:
        if r not in seen:
            unique.append(r)
            seen.add(r)

    return delta, unique[:4]


def search_living_options(
    user_text: str,
    lang: str = "de",
    wheelchair_required=None,
    care_target=None,
    languages=None,
    age=None,
    care_weight: float = 0.15,
    limit: int = 20,
    click_boosts=None,
    skip_penalties=None,
):
    """
    Returns a list of dicts:
      {
        "option": LivingOption,
        "score": float,
        "semantic_score": float,
        "reasons": [str],
        "tier": "best" | "other",
      }
    """
    if lang not in SUPPORTED_LANGS:
        lang = "de"

    q_emb = generate_embedding(user_text)
    if not q_emb:
        return []

    scored = []
    candidate_k = max(limit * 20, 200)  # e.g. if you return ~8 results, pull ~200 candidates

    # IMPORTANT: iterate over per-language embeddings
    age_int = None
    if age is not None:
        try:
            m = re.search(r"\d{1,3}", str(age))
            age_int = int(m.group()) if m else None
        except (TypeError, ValueError):
            age_int = None

    # 2) THEN build queryset
    base_qs = (
        LivingOptionEmbedding.objects
        .select_related("living_option", "living_option__provider")
        .filter(language=lang)
    )

    if age_int is not None:
        base_qs = base_qs.filter(
            living_option__min_age__lte=age_int,
            living_option__max_age__gte=age_int
        )
    if age_int is not None and age_int < 18:
        youth_qs = base_qs.filter(living_option__max_age__lte=17)
        if youth_qs.exists():
            base_qs = youth_qs
        # else: keep age-compatible base_qs (or return none, depending on your policy)

    candidate_count = base_qs.count()

    qs = (
        base_qs
        .annotate(distance=CosineDistance("embedding", q_emb))
        .order_by("distance")[:candidate_k]
    )

    query_l = user_text.lower()
    signals = detect_signals(user_text)

    for e in qs:
        lo = e.living_option
        with switch_language(lo, lang):
            title_l = (lo.title or "").lower()
            desc_l  = (lo.description or "").lower()
        reasons = []

        # --- hard filters ---
        if wheelchair_required is not None:
            if lo.wheelchair_accessible != wheelchair_required:
                continue
            reasons.append(_("Wheelchair accessible"))
        if languages:
            if not any(code in lo.languages_supported for code in languages):
                continue
            reasons.append(_("Supports your language"))
        if age_int is not None:
            if lo.min_age is not None and age_int < lo.min_age:
                continue
            if lo.max_age is not None and age_int > lo.max_age:
                continue
            reasons.append(_("Matches your age range"))

        semantic_score = 1.0 - float(getattr(e, "distance", 1.0))
        semantic_score = max(min(semantic_score, 1.0), -1.0)
        score = semantic_score
        if semantic_score >= 0.85:
            score += 0.10
            reasons.append(_("Very strong match"))
        elif semantic_score >= 0.78:
            score += 0.05
        reasons.append(_("Similar to your description"))

        # --- care fit reranking + tier ---
        BEST_SEM_MIN  = 0.55   # strict-ish
        OTHER_SEM_MIN = 0.30   # permissive-ish

        BEST_SCORE_MIN  = 0.55
        OTHER_SCORE_MIN = 0.35
        if candidate_count < 30:
            OTHER_SEM_MIN *= 0.6   # 0.18
            BEST_SEM_MIN  *= 0.8

        if candidate_count < 10:
            OTHER_SEM_MIN *= 0.5   # very permissive
            BEST_SEM_MIN  *= 0.7
            OTHER_SCORE_MIN = -1.0

        # ... after semantic_score is computed ...

        # Small domain boosts (gentle nudges, not hard filters)
        STOPWORDS = {
            "wohnung","wohnen","wohn","studio","apartment","zimmer","wg","haus","heim",
            "mit","und","für","bei","nach","ohne","oder","etwas","sehr","mehr","weniger",
            "ruhig","nahe","option","hilfe","unterstützung","betreuung",
            "bern","basel","zürich","lausanne","genf","geneva","lugano","winterthur",
        }
        raw_tokens = [
            w.strip(".,:;!?()[]{}\"'").lower()
            for w in query_l.split()
        ]
        tokens = [
            w for w in raw_tokens
            if len(w) >= 6 and w not in STOPWORDS  # 6 cuts most generic German function words
        ]
        hits = [tok for tok in tokens if tok in title_l]
        if len(hits) >= 2:
            score += 0.08
            reasons.append(_("Title matches"))
        elif len(hits) == 1 and len(hits[0]) >= 9:
            score += 0.08
            reasons.append(_("Title matches"))

        # Optional: drop very weak matches entirely
        if semantic_score < OTHER_SEM_MIN:
            continue

        desc_l = (lo.safe_translation_getter("description", language_code=lang, any_language=False) or "").lower()
        title_l = (lo.safe_translation_getter("title", language_code=lang, any_language=False) or "").lower()
        text_l = f"{title_l}\n{desc_l}"

        title_local = lo.safe_translation_getter("title", language_code=lang, any_language=False) or ""
        desc_local  = lo.safe_translation_getter("description", language_code=lang, any_language=False) or ""

        # extra reasons----
        delta, extra_reasons = apply_condition_rules(
            query_text=user_text,
            signals=signals,
            listing=lo,
            title_text=title_local,
            description_text=desc_local,
            age=age_int,
        )
        score += delta
        reasons.extend(extra_reasons)

        # Optional fallback (if missing in that language)
        if not title_local:
            title_local = lo.safe_translation_getter("title", any_language=True) or ""
        if not desc_local:
            desc_local = lo.safe_translation_getter("description", any_language=True) or ""

        if click_boosts:
            b = float(click_boosts.get(lo.id, 0.0))
            if b:
                score += b
                reasons.append(_("Chosen often for similar searches"))
        if skip_penalties:
            p = float(skip_penalties.get(lo.id, 0.0))
            if p:
                score -= p
                reasons.append(_("Often skipped for similar searches"))

        # if user didn't mention any of these, and listing is explicitly about one, penalize a bit
        desc_l = (lo.safe_translation_getter("description", language_code=lang, any_language=False) or "").lower()


        if semantic_score >= BEST_SEM_MIN and score >= BEST_SCORE_MIN:
            tier = "best"
        elif score < OTHER_SCORE_MIN:
            continue

        tier = "other"
        if care_target is not None:
            dist = abs(lo.care_level - care_target)

            # keep your adaptive care penalty
            effective_care_weight = care_weight
            if semantic_score >= 0.80:
                effective_care_weight = care_weight * 0.25
            elif semantic_score >= 0.72:
                effective_care_weight = care_weight * 0.60

            score -= dist * effective_care_weight

            # ✅ gate "best" on BOTH care + semantic
            if dist <= 1 and semantic_score >= BEST_SEM_MIN:
                tier = "best"
                reasons.append(_("Close to your desired support level"))
            else:
                reasons.append(_("Different support level than requested"))
        else:
            # if no care_target, you can still tier best by semantic
            if semantic_score >= BEST_SEM_MIN:
                tier = "best"

        score = max(score, -1.0)

        scored.append({
            "option": lo,
            "title": title_local,
            "description": desc_local,
            "score": score,
            "semantic_score": semantic_score,
            "reasons": reasons[:4],
            "tier": tier,
        })

    # Sort all results by score first
    scored.sort(key=lambda x: x["score"], reverse=True)

    # after: scored.sort(...)
    for i, r in enumerate(scored[:10]):
        print(i, r["option"].id, r["title"], "score=", round(r["score"], 3), "sem=", round(r["semantic_score"], 3))

    # also find the rank of the Basel listing (use ID or slug)
    target_id = 123  # Basel Assisted Mobility Flat ID
    for i, r in enumerate(scored):
        if r["option"].id == target_id:
            print("Basel rank:", i, "score=", r["score"], "sem=", r["semantic_score"])
            break

    seen = set()
    deduped = []
    for r in scored:
        oid = r["option"].id
        if oid in seen:
            continue
        seen.add(oid)
        deduped.append(r)
    scored = deduped

    if care_target is None:
        for r in scored[:5]:
            r["tier"] = "best"
        best_matches = scored[:5]
        other_matches = scored[5:8]
        return best_matches + other_matches

    # Split by tier
    best_matches = [r for r in scored if r["tier"] == "best"][:5]
    other_matches = [r for r in scored if r["tier"] != "best"][:3]

    # Return in display order
    return best_matches + other_matches
