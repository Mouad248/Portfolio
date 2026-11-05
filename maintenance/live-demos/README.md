# Public portfolio demos

Optional browser-demo sources, kept separately from the four original projects.
[Folder guide](../README.md) · [Portfolio](../../README.md)

These browser adaptations are independent of the original projects. They require no
Power BI licence, Python server, account or data upload to explore.

- [NorthPeak live demo](https://northpeak-analytics-mouade.appreciativebow.chatgpt.site)
- [Reinsight live demo](https://reinsight-analytics-mouade.appreciativebow.chatgpt.site)

Both Sites are deployed with public access enabled.

- `northpeak/dist/`: interactive views of the existing synthetic SaaS model outputs.
- `reinsight/dist/`: browser aggregation of the existing anonymised reinsurance demo data.

Regenerate data from the repository root:

```powershell
Actuariat_dashboard/venv/Scripts/python.exe maintenance/live-demos/export_data.py
```

After changing `shared.css` or `shared.js`, copy each into both `dist` directories
(renaming `shared.css` to `styles.css`). All site files are plain HTML, CSS and ES modules.

The Sites manifests preserve each demo's hosting identity. The original Python,
React and Power BI implementations remain in their project directories.

Interaction checks:

```powershell
node --experimental-vm-modules maintenance/live-demos/check-demos.mjs
```

These checks exercise the JavaScript through a DOM harness; a visual browser review
was not available in the publishing session.
