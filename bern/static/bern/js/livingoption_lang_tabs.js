(function () {
  function setActiveLang(lang) {
    document.querySelectorAll(".lang-tab").forEach((btn) => {
      const isActive = btn.dataset.lang === lang;
      btn.classList.toggle("active", isActive);
      btn.setAttribute("aria-selected", isActive ? "true" : "false");
    });

    document.querySelectorAll(".lang-pane").forEach((pane) => {
      pane.classList.toggle("show", pane.dataset.lang === lang);
    });
  }

  function syncCheckbox(lang, hasText) {
    const cb = document.getElementById(`lang_check_${lang}`);
    if (cb) cb.checked = hasText;
  }

  function init() {
    // Tabs
    document.querySelectorAll(".lang-tab").forEach((btn) => {
      btn.addEventListener("click", () => setActiveLang(btn.dataset.lang));
    });

    // Textareas: update checkbox based on content
    const map = {
      de: document.querySelector('[data-lang="de"] textarea'),
      fr: document.querySelector('[data-lang="fr"] textarea'),
      it: document.querySelector('[data-lang="it"] textarea'),
      en: document.querySelector('[data-lang="en"] textarea'),
    };

    Object.entries(map).forEach(([lang, ta]) => {
      if (!ta) return;

      const update = () => syncCheckbox(lang, ta.value.trim().length > 0);

      ta.addEventListener("input", update);
      update(); // initial state on load
    });

    // Default tab
    setActiveLang("de");
  }

  document.addEventListener("DOMContentLoaded", init);
})();
