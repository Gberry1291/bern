(function () {
  function autoGrow(el) {
    el.style.height = "auto";
    el.style.height = el.scrollHeight + "px";
  }

  document.addEventListener("input", function (e) {
    if (e.target.tagName === "TEXTAREA") {
      autoGrow(e.target);
    }
  });

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("textarea").forEach(autoGrow);
  });
})();


document.querySelectorAll(".example-chip").forEach(btn => {
  btn.addEventListener("click", () => {
    const textarea = document.querySelector("#q");
    textarea.value = btn.textContent.trim();
    textarea.focus();
    textarea.dispatchEvent(new Event("input"));
  });
});
