(function () {
  function initLanguageMultiSelect() {
    const select = document.getElementById("language");
    const chips = document.getElementById("language-selected");
    if (!select || !chips) return;

    // Avoid binding twice (important because you use partial swaps)
    if (select.dataset.bound === "1") return;
    select.dataset.bound = "1";

    function getSelectedValues() {
      return Array.from(select.selectedOptions).map((o) => o.value);
    }

    function setSelected(values) {
      Array.from(select.options).forEach((opt) => {
        opt.selected = values.includes(opt.value);
      });
    }

    function renderChips() {
      const selected = Array.from(select.selectedOptions);

      // If "Any" selected or nothing selected, show a single chip
      const anyOpt = selected.find((o) => o.value === "");
      if (anyOpt || selected.length === 0) {
        chips.innerHTML = `<span class="chip">${anyOpt ? anyOpt.textContent : "Any"}</span>`;
        return;
      }

      chips.innerHTML = "";
      selected.forEach((opt) => {
        const chip = document.createElement("span");
        chip.className = "chip";
        chip.innerHTML = `
          <span>${opt.textContent}</span>
          <button type="button" aria-label="Remove ${opt.textContent}">&times;</button>
        `;

        chip.querySelector("button").addEventListener("click", () => {
          // Remove that option
          opt.selected = false;

          // If nothing left, fall back to Any
          const remaining = getSelectedValues().filter((v) => v !== "");
          if (remaining.length === 0) {
            setSelected([""]);
          }
          renderChips();
        });

        chips.appendChild(chip);
      });
    }

    // Behavior rule:
    // - If user selects any specific language, unselect "Any"
    // - If user selects "Any", clear others
    select.addEventListener("change", () => {
      console.log(select.selectedOptions)
      const selectedValues = getSelectedValues();
      if (selectedValues.includes("") && selectedValues.length > 1) {
        // If "Any" plus others, keep only others (prefer specificity)
        setSelected(selectedValues.filter((v) => v !== ""));
      } else if (selectedValues.includes("") && selectedValues.length === 1) {
        // "Any" alone: clear others (already)
      } else if (selectedValues.length === 0) {
        // Nothing selected: treat as Any
        setSelected([""]);
      }

      renderChips();
    });

    // Initial render (handles pre-filled GET params)
    // If nothing selected, default to Any
    if (getSelectedValues().length === 0) setSelected([""]);
    renderChips();
  }

  // Run on initial load
  document.addEventListener("DOMContentLoaded", initLanguageMultiSelect);

  // If you swap page content via X-Partial, re-run after swaps
  // (Custom event hook: you can dispatch this after swapping HTML if you want)
  document.addEventListener("page:updated", initLanguageMultiSelect);

})();
