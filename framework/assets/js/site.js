(() => {
  const root = document.documentElement;
  const button = document.querySelector("[data-theme-toggle]");
  const saved = localStorage.getItem("course-theme");
  const preferred = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  const setTheme = (theme) => {
    root.dataset.theme = theme;
    if (button) {
      button.setAttribute("aria-label", `Switch to ${theme === "dark" ? "light" : "dark"} mode`);
      button.textContent = theme === "dark" ? "Light mode" : "Dark mode";
    }
  };
  setTheme(saved || preferred);
  button?.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    localStorage.setItem("course-theme", next);
    setTheme(next);
  });
})();
