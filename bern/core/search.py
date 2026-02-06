import numpy as np
from core.embeddings import generate_embedding
from core.models import LivingOptionEmbedding
from django.utils.translation import gettext as _

SUPPORTED_LANGS = {"de", "fr", "it", "en"}

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
        "blind", "seh", "sehbehindert",
        "vision", "malvoyant", "aveugle",
        "cieco", "ipovision",
    ]

    return {
        "hearing": any(w in t for w in hearing_terms),
        "vision": any(w in t for w in vision_terms),
    }



def search_living_options(
    user_text: str,
    lang: str = "de",
    wheelchair_required=None,
    care_target=None,
    languages=None,
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

    query_vec = np.array(q_emb, dtype=np.float32)
    q_norm = np.linalg.norm(query_vec)
    if q_norm == 0:
        return []

    scored = []

    # IMPORTANT: iterate over per-language embeddings
    qs = (
        LivingOptionEmbedding.objects
        .select_related("living_option", "living_option__provider")
        .filter(language=lang)
    )

    for e in qs:
        lo = e.living_option
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


        lo_vec = np.array(e.embedding, dtype=np.float32)
        lo_norm = np.linalg.norm(lo_vec)
        if lo_norm == 0:
            continue

        semantic_score = float(np.dot(query_vec, lo_vec) / (q_norm * lo_norm))
        score = semantic_score
        if semantic_score >= 0.85:
            score += 0.10
            reasons.append(_("Very strong match"))
        elif semantic_score >= 0.78:
            score += 0.05
        reasons.append(_("Similar to your description"))

        signals = detect_signals(user_text)
        # Small domain boosts (gentle nudges, not hard filters)
        if signals["hearing"]:
            if lo.hearing_support:
                score += 0.22
                reasons.append(_("Hearing support available"))
            else:
                score -= 0.10

        if signals["vision"]:
            if lo.visual_support:
                score += 0.18
                reasons.append(_("Visual support available"))
            else:
                score -= 0.08

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

        # --- care fit reranking + tier ---
        tier = "other"
        if care_target is not None:
            dist = abs(lo.care_level - care_target)

            # Adaptive care penalty: reduce penalty for strong semantic matches
            effective_care_weight = care_weight
            if semantic_score >= 0.80:
                effective_care_weight = care_weight * 0.25  # much less important
            elif semantic_score >= 0.72:
                effective_care_weight = care_weight * 0.60  # somewhat less important

            score -= dist * effective_care_weight

            if dist <= 1:
                tier = "best"
                reasons.append(_("Close to your desired support level"))
            else:
                reasons.append(_("Different support level than requested"))

        score = max(score, -1.0)

        scored.append({
            "option": lo,
            "score": score,
            "semantic_score": semantic_score,
            "reasons": reasons[:4],
            "tier": tier,
        })

    # Sort all results by score first
    scored.sort(key=lambda x: x["score"], reverse=True)

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
