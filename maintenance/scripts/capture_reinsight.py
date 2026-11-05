"""Capture the existing local Reinsight application, without changing app code.

Requires Playwright and an installed Chromium browser (Edge is used here).
Start the bundled-data API on port 8000 and Vite on port 8080 first.
"""
from pathlib import Path
import argparse
import asyncio
import json
from urllib.request import urlopen

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "Actuariat_dashboard/screenshots"


async def capture(executable):
    OUT.mkdir(exist_ok=True)
    names = ["profitability-dashboard.png", "cedant-analysis.png"]
    with urlopen("http://127.0.0.1:8000/api/cedants/suggest?q=001&limit=10", timeout=30) as response:
        suggestions = json.load(response)
    assert any(s["id"] == "Cédante 001" for s in suggestions["suggestions"]), "Require the bundled demo cedant"
    print("Confirmed demo cedant Cédante 001 in API suggestions", flush=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=executable, headless=True)
        context = await browser.new_context(viewport={"width": 1600, "height": 1400}, device_scale_factor=1)
        page = await context.new_page()
        api_responses, errors = [], []
        page.on("response", lambda r: api_responses.append({"url": r.url, "status": r.status}) if "/api/" in r.url else None)
        page.on("pageerror", lambda e: (errors.append(str(e)), print("Page error:", str(e), flush=True)))
        page.on("requestfailed", lambda r: print("Failed request:", r.url, r.failure, flush=True))
        page.on("console", lambda m: print("Browser console:", m.text, flush=True) if m.type == "error" else None)
        async with page.expect_response(lambda r: "/api/subscription-data" in r.url and r.status == 200, timeout=90000) as pending:
            await page.goto("http://localhost:8080/subscription", wait_until="domcontentloaded")
        response = await pending.value
        payload = await response.json()
        assert payload["annualPerformance"] and payload["regions"], "Require populated API data"
        await page.get_by_role("heading", name="Rentabilité de la Souscription").wait_for()
        await page.locator(".recharts-surface").first.wait_for(state="visible", timeout=60000)
        # Scroll through the page to render chart containers before full-page capture.
        await page.evaluate("async () => { for(let y=0;y<document.body.scrollHeight;y+=700){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,120));}window.scrollTo(0,0);}")
        await page.evaluate("document.fonts.ready")
        await page.wait_for_timeout(1800)
        chart_count = await page.locator(".recharts-surface").count()
        assert chart_count >= 2, "Require multiple chart panels"
        for name, full in [(names[0], True), ("profitability-overview.png", False)]:
            if not (OUT / name).exists():
                await page.screenshot(path=str(OUT / name), full_page=full, animations="disabled")
            else:
                print("Preserved existing capture:", name)
        print(f"Profitability: {chart_count} chart SVGs; API returned populated annual and regional results")

        await page.goto("http://localhost:8080/cedantes", wait_until="domcontentloaded")
        search = page.locator("input").first
        await search.fill("001")
        # Select the actual option produced by the existing search UI.
        option = page.get_by_role("option").filter(has_text="Cédante 001").first
        await option.wait_for(state="visible", timeout=30000)
        async with page.expect_response(lambda r: "/analytics" in r.url and "segment=FAC" in r.url and r.status == 200, timeout=90000):
            await option.click()
        await page.locator(".recharts-surface").first.wait_for(state="visible", timeout=60000)
        await page.wait_for_function("!document.body.innerText.includes('Chargement des données pour')", timeout=90000)
        await page.evaluate("async () => { for(let y=0;y<document.body.scrollHeight;y+=700){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,120));}window.scrollTo(0,0);}")
        await page.wait_for_timeout(1800)
        assert "Cédante 001" in await page.inner_text("body"), "Selected demo cedant must remain visible"
        await page.keyboard.press("Escape")
        await page.get_by_role("heading", name="Cédantes", exact=True).click()
        chart_count = await page.locator(".recharts-surface").count()
        assert chart_count >= 2, "Require populated cedant charts"
        for name, full in [(names[1], True), ("cedant-overview.png", False)]:
            if not (OUT / name).exists():
                await page.screenshot(path=str(OUT / name), full_page=full, animations="disabled")
            else:
                print("Preserved existing capture:", name)
        print(f"Cedant analysis: Cédante 001 selected; {chart_count} chart SVGs")
        print("API responses:", json.dumps(api_responses, ensure_ascii=True))
        print("Browser page errors:", json.dumps(errors, ensure_ascii=True))
        await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", default="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
    asyncio.run(capture(parser.parse_args().browser))
