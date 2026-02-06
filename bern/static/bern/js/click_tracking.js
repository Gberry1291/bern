(function () {
  function getCSRFToken() {
    const el = document.querySelector("[name=csrfmiddlewaretoken]");
    return el ? el.value : null;
  }

  function getEventId() {
    const container = document.getElementById("results-container");
    if (!container) return null;
    const v = container.getAttribute("data-search-event-id");
    return v ? parseInt(v, 10) : null;
  }

  async function postClick(eventId, optionId, rank, csrfToken) {
    const fd = new FormData();
    fd.append("event_id", String(eventId));
    fd.append("option_id", String(optionId));
    fd.append("rank", String(rank));

    // Use relative URL so it works in any environment
    const resp = await fetch("/track-click/", {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
        "X-Requested-With": "XMLHttpRequest",
      },
      body: fd,
    });

    // Don't block UX if it fails; just log
    if (!resp.ok) {
      console.warn("track-click failed", resp.status);
    }
  }

  function init() {
    const csrfToken = getCSRFToken();
    if (!csrfToken) return;

    // Event delegation so it still works after partial swaps
    document.addEventListener("click", function (e) {
      const card = e.target.closest(".card[data-option-id][data-rank]");
      if (!card) return;

      const eventId = getEventId();
      if (!eventId) return; // no query yet

      const optionId = parseInt(card.getAttribute("data-option-id"), 10);
      const rank = parseInt(card.getAttribute("data-rank"), 10);

      if (!Number.isFinite(optionId) || !Number.isFinite(rank)) return;

      // Fire-and-forget
      postClick(eventId, optionId, rank, csrfToken);
    });
  }

  document.addEventListener("DOMContentLoaded", init);
})();
