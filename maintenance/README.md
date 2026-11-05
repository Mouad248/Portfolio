# Supporting tools and optional demos

These files support maintenance. Start with the [portfolio](../README.md) or
[repository guide](../portfolio-guide/README.md) to review the projects themselves.

| Folder | Contents | When needed |
| --- | --- | --- |
| [scripts/](scripts/) | Documentation link checker and Reinsight screenshot capture | Updating documentation or refreshing local captures |
| [live-demos/](live-demos/README.md) | Existing browser adaptations, data-export helper and interaction checks | Maintaining the optional demos |

The demo sources, hosting metadata and build archives are preserved here. Moving
them did not redeploy or change the hosted sites. Generated deployment archives
remain ignored by the demo folder's existing `.gitignore`.

## Commands

From the portfolio root:

```powershell
# Check local documentation links
python maintenance/scripts/check_portfolio_docs.py

# Capture the existing Reinsight app after starting its frontend and demo-data API
python maintenance/scripts/capture_reinsight.py

# Check the existing browser-demo interactions without deploying
node --experimental-vm-modules maintenance/live-demos/check-demos.mjs
```

Screenshot capture requires Playwright and an installed Chromium browser; see the
[capture instructions](../Actuariat_dashboard/screenshots/README.md#reproduce-locally).
The [demo README](live-demos/README.md) explains its separate export workflow.
Clinical's SQL companion stays inside the Clinical project because it is part of
that project's implementation evidence.
