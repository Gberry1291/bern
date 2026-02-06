import numpy as np
from core.models import SearchEvent, SearchClick
from core.models import SearchImpression

def _cosine(a, b) -> float:
    a = np.array(a, dtype=np.float32)
    b = np.array(b, dtype=np.float32)
    an = np.linalg.norm(a)
    bn = np.linalg.norm(b)
    if an == 0 or bn == 0:
        return 0.0
    return float(np.dot(a, b) / (an * bn))

def get_click_boosts(query_embedding, lang: str, max_events: int = 250):
    """
    Returns dict: {living_option_id: boost_float}
    Boost is based on clicks from similar past searches.
    """
    if not query_embedding:
        return {}

    # pull recent events with embeddings (keep it small; prototype-friendly)
    events = list(
        SearchEvent.objects
        .filter(lang=lang, query_embedding__isnull=False)
        .order_by("-created_at")[:max_events]
    )

    # weight events by similarity
    similar = []
    for ev in events:
        sim = _cosine(query_embedding, ev.query_embedding)
        if sim >= 0.78:
            similar.append((ev.id, sim))

    if not similar:
        return {}

    # build click weights: higher similarity + higher rank (rank 0 is strongest)
    boosts = {}
    event_ids = [eid for eid, _ in similar]
    sim_map = dict(similar)

    clicks = (
        SearchClick.objects
        .filter(event_id__in=event_ids)
        .values("living_option_id", "event_id", "rank_shown")
    )

    for c in clicks:
        sim = sim_map.get(c["event_id"], 0.0)
        rank = c["rank_shown"]

        # Rank discount: top clicks count more
        rank_weight = 1.0 / (1.0 + rank)

        # Similarity weight: very similar searches count more
        weight = sim * rank_weight

        boosts[c["living_option_id"]] = boosts.get(c["living_option_id"], 0.0) + weight

    # Normalize into a small, safe boost range
    # (Keeps “feedback” from overpowering relevance)
    if boosts:
        max_w = max(boosts.values())
        for k in list(boosts.keys()):
            boosts[k] = 0.15 * (boosts[k] / max_w)  # 0..0.15

    return boosts


def get_feedback_adjustments(query_embedding, lang: str, max_events: int = 250):
    """
    Returns (boosts, penalties):
      boosts:    {living_option_id: +0..+0.15}
      penalties: {living_option_id: -0..-0.10}
    """
    if not query_embedding:
        return {}, {}

    events = list(
        SearchEvent.objects
        .filter(lang=lang, query_embedding__isnull=False)
        .order_by("-created_at")[:max_events]
    )

    similar = []
    for ev in events:
        sim = _cosine(query_embedding, ev.query_embedding)
        if sim >= 0.78:
            similar.append((ev.id, sim))

    if not similar:
        return {}, {}

    event_ids = [eid for eid, _ in similar]
    sim_map = dict(similar)

    # --- positives (clicks) ---
    boosts = {}
    clicks = (
        SearchClick.objects
        .filter(event_id__in=event_ids)
        .values("living_option_id", "event_id", "rank_shown")
    )

    for c in clicks:
        sim = sim_map.get(c["event_id"], 0.0)
        rank = c["rank_shown"]
        rank_weight = 1.0 / (1.0 + rank)
        weight = sim * rank_weight
        boosts[c["living_option_id"]] = boosts.get(c["living_option_id"], 0.0) + weight

    # --- negatives (skips) ---
    penalties = {}
    skips = (
        SearchImpression.objects
        .filter(event_id__in=event_ids, skipped=True)
        .values("living_option_id", "event_id", "rank_shown")
    )

    for s in skips:
        sim = sim_map.get(s["event_id"], 0.0)
        rank = s["rank_shown"]
        # Top skips matter most
        rank_weight = 1.0 / (1.0 + rank)
        weight = sim * rank_weight
        penalties[s["living_option_id"]] = penalties.get(s["living_option_id"], 0.0) + weight

    # Normalize into safe ranges
    if boosts:
        max_b = max(boosts.values())
        for k in list(boosts.keys()):
            boosts[k] = 0.15 * (boosts[k] / max_b)

    if penalties:
        max_p = max(penalties.values())
        for k in list(penalties.keys()):
            penalties[k] = 0.10 * (penalties[k] / max_p)  # 0..0.10

    return boosts, penalties
