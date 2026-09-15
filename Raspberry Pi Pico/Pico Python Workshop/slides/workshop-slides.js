const slideLanguage = document.documentElement.lang.startsWith("de")
  ? "de"
  : "en";
const daysOverviewLink = document.createElement("a");

daysOverviewLink.className = "days-overview-link";
daysOverviewLink.href = `../../${slideLanguage}/`;
daysOverviewLink.textContent =
  slideLanguage === "de" ? "← Tagesübersicht" : "← Days overview";
document.body.append(daysOverviewLink);

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
