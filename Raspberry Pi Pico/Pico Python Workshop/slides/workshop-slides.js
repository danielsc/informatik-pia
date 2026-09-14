Reveal.initialize({
  hash: true,
  history: true,
  controlsTutorial: false,
  progress: true,
  slideNumber: "c/t",
  transition: "slide",
  backgroundTransition: "fade",
  pdfSeparateFragments: false,
  center: false,
  width: 1280,
  height: 720,
  margin: 0.04,
  plugins: [RevealNotes, RevealHighlight]
});

const fullscreenButton = document.querySelector("#fullscreen-button");

if (!document.fullscreenEnabled) {
  fullscreenButton.hidden = true;
} else {
  fullscreenButton.addEventListener("click", () => {
    if (document.fullscreenElement) {
      document.exitFullscreen();
    } else {
      document.documentElement.requestFullscreen();
    }
  });

  document.addEventListener("fullscreenchange", () => {
    const active = Boolean(document.fullscreenElement);
    fullscreenButton.textContent = active ? "Exit full screen" : "Full screen";
    fullscreenButton.title = active ? "Exit fullscreen (F)" : "Enter fullscreen (F)";
  });
}
