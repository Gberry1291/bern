(function () {
  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
    return null;
  }

  async function fetchPagePartial() {
    const url = new URL(window.location.href);
    const resp = await fetch(url.toString(), {
      headers: { "X-Partial": "page" },
    });

    if (!resp.ok) {
      const txt = await resp.text().catch(() => "");
      console.error("page partial failed:", resp.status, txt);
      throw new Error("Failed to fetch page partial");
    }
    return resp.text();
  }

  async function postLanguage(lang) {
    // Prefer navbar form URL; fallback to select URL
    const form = document.getElementById("lang-form");
    const select = document.getElementById("uiLangSelect");

    const setLangUrl =
      (form && form.dataset.setLangUrl) ||
      (select && select.getAttribute("data-set-lang-url"));

    if (!setLangUrl) {
      throw new Error("Missing set language URL (data-set-lang-url / data-set-lang-url attr)");
    }

    const csrfToken = getCookie("csrftoken");
    if (!csrfToken) throw new Error("Missing csrftoken cookie");

    const body = new URLSearchParams();
    body.set("ui_lang", lang);

    const resp = await fetch(setLangUrl, {
      method: "POST",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrfToken,
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: body.toString(),
    });

    if (!resp.ok) {
      const txt = await resp.text().catch(() => "");
      console.error("set_ui_language failed:", resp.status, txt);
      throw new Error("Failed to set language");
    }
  }

  function setLoading(isLoading) {
    const container = document.getElementById("page-container");
    if (!container) return;

    if (isLoading) {
      container.style.opacity = "0.6";
      container.style.pointerEvents = "none";
    } else {
      container.style.opacity = "1";
      container.style.pointerEvents = "";
    }
  }

  // Optional: immediate visual feedback before re-render
  function setActiveLangButton(lang) {
    document.querySelectorAll(".lang-btn").forEach((b) => b.classList.remove("active"));
    const btn = document.querySelector(`.lang-btn[data-lang="${lang}"]`);
    if (btn) btn.classList.add("active");
  }

  async function applyLanguage(lang) {
    setLoading(true);
    try {
      setActiveLangButton(lang); // optional instant feedback
      await postLanguage(lang);

      const html = await fetchPagePartial();
      const container = document.getElementById("page-container");
      if (container) container.innerHTML = html;
      document.dispatchEvent(new Event("page:updated"))

      // Re-bind select listener if select exists inside swapped HTML
      bindSelect();
    } catch (err) {
      console.error("Language switch failed:", err);
      alert("Could not change language. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  // Navbar buttons: event delegation (survives swaps)
  function bindNavbarButtons() {
    document.addEventListener("click", (e) => {
      const btn = e.target.closest(".lang-btn[data-lang]");
      if (!btn) return;

      // ignore already-active button
      if (btn.classList.contains("active")) return;

      e.preventDefault();
      applyLanguage(btn.dataset.lang);
    });
  }

  // Optional select support (if you still have one somewhere)
  function bindSelect() {
    const select = document.getElementById("uiLangSelect");
    if (!select) return;

    // Avoid double-binding if bindSelect is called after swaps
    if (select.dataset.langBound === "1") return;
    select.dataset.langBound = "1";

    select.addEventListener("change", () => {
      applyLanguage(select.value);
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    bindNavbarButtons();
    bindSelect();
  });
})();
