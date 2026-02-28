(function () {
  const KEY = "saved_options_v1";

  function loadSavedSet() {
    try {
      const arr = JSON.parse(localStorage.getItem(KEY) || "[]");
      return new Set(arr.map(String));
    } catch {
      return new Set();
    }
  }

  function persistSavedSet(savedSet) {
    localStorage.setItem(KEY, JSON.stringify([...savedSet]));
  }

  function setBtnState(btn, isSaved) {
    btn.classList.toggle("is-saved", isSaved);
    btn.setAttribute("aria-pressed", isSaved ? "true" : "false");

    // Default English; you can localize via data attributes later if you want
    const labelSaved = btn.dataset.labelSaved || "Saved";
    const labelSave = btn.dataset.labelSave || "Save";
    btn.textContent = isSaved ? labelSaved : labelSave;
  }

  function updateSavedNav(savedSet) {
    const countEl = document.getElementById("saved-count");
    if (countEl) countEl.textContent = String(savedSet.size);

    const savedLink = document.getElementById("saved-link");
    if (savedLink) {
      const ids = [...savedSet].join(",");
      savedLink.setAttribute("href", `/saved/?ids=${encodeURIComponent(ids)}`);
    }
  }

  function bindSaveButtons(savedSet) {
    document.querySelectorAll(".save-btn").forEach((btn) => {
      const optionId = String(btn.dataset.optionId || "");
      if (!optionId) return;

      // initial state
      setBtnState(btn, savedSet.has(optionId));

      btn.addEventListener("click", () => {
        if (savedSet.has(optionId)) savedSet.delete(optionId);
        else savedSet.add(optionId);

        persistSavedSet(savedSet);
        setBtnState(btn, savedSet.has(optionId));
        updateSavedNav(savedSet);

        // If we're on the saved page, remove card immediately when unsaving
        if (document.body.classList.contains("saved-page") && !savedSet.has(optionId)) {
          const card = btn.closest(".card");
          if (card) card.remove();
        }
      });
    });
  }

  function ensureSavedPageHasIds(savedSet) {
    // If user directly visits /saved/ without ids, redirect to include ids
    if (!document.body.classList.contains("saved-page")) return;

    const params = new URLSearchParams(window.location.search);
    const idsParam = params.get("ids");

    // If ids missing but we have saved items, redirect to populate server-rendered list
    if ((!idsParam || idsParam.trim() === "") && savedSet.size > 0) {
      const ids = [...savedSet].join(",");
      window.location.replace(`/saved/?ids=${encodeURIComponent(ids)}`);
    }
  }

  function init() {
    const savedSet = loadSavedSet();
    updateSavedNav(savedSet);
    ensureSavedPageHasIds(savedSet);
    bindSaveButtons(savedSet);
  }

  document.addEventListener("DOMContentLoaded", init);
})();
