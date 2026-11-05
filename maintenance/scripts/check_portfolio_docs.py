"""Check local Markdown targets and anchors in the portfolio presentation files."""
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
PROJECTS = ["Consommation_Maroc", "Actuariat_dashboard", "northpeak-fpna-main", "Clinical-KPI-Dashboard-main"]
FILES = [ROOT / "README.md", *sorted((ROOT / "portfolio-guide").glob("*.md"))]
FILES.extend([ROOT / "maintenance/README.md", ROOT / "maintenance/live-demos/README.md"])
for project in PROJECTS:
    FILES.extend(ROOT / project / name for name in ["README.md", "CASE_STUDY.md", "screenshots/README.md"])
FILES.extend([ROOT / "Clinical-KPI-Dashboard-main/sql/README.md", ROOT / "Clinical-KPI-Dashboard-main/docs/README_technical.md"])


def anchors(path):
    counts, result = {}, set()
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not re.match(r"^#{1,6}\s", line):
            continue
        title = re.sub(r"^#{1,6}\s+", "", line).strip().rstrip("#").strip()
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        index = counts.get(slug, 0)
        counts[slug] = index + 1
        result.add(slug + (f"-{index}" if index else ""))
    return result


def main():
    failures, checked, images = [], 0, set()
    for doc in FILES:
        content = doc.read_text(encoding="utf-8-sig")
        # Ignore fenced examples rather than interpreting sample Markdown as links.
        content = re.sub(r"```.*?```", "", content, flags=re.S)
        for match in re.finditer(r"(!?)\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", content):
            image, raw = match.groups()
            target = raw.strip("<>")
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue  # External URLs are outside this local-link check.
            path = (doc.parent / unquote(url.path)).resolve() if url.path else doc
            checked += 1
            if not path.exists():
                failures.append(f"{doc.relative_to(ROOT)}: missing {target}")
            elif url.fragment and path.is_file() and path.suffix.lower() == ".md":
                if unquote(url.fragment) not in anchors(path):
                    failures.append(f"{doc.relative_to(ROOT)}: missing anchor {target}")
            if image:
                images.add(path)
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"PASS: {checked} local link/image targets across {len(FILES)} Markdown files, including linked Markdown anchors")
    print(f"Representative linked images: {len(images)} unique files; external URLs were not fetched")


if __name__ == "__main__":
    main()
