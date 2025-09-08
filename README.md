# Lucille’s BBQ — Fort Wayne (Static Site)

A single‑file static website tailored for GitHub Pages with strong SEO, accessibility, and performance.

## Quick Start (GitHub Pages)
1. Create a new **public** repository, e.g. `lucilles-bbq` under your GitHub account.
2. Upload everything in this folder (including `sitemap.xml` and `robots.txt`).
3. In the repo settings → **Pages**, choose the `main` branch and `/root` for the site. Save.
4. Your site will be live at `https://<YOUR_GITHUB_USERNAME>.github.io/lucilles-bbq/`.

## Notes
- The gallery *hotlinks* to publicly available images of Lucille’s BBQ (Fort Wayne). You may replace them under `/assets/img/` in the future to self‑host.
- Business details: 9011 Lima Rd, Fort Wayne, IN 46818 • (260) 203‑3937 • Open Daily 11 AM – 9 PM.
- Online ordering via Toast: https://www.toasttab.com/local/order/lucilles-bbq-lima-9011-lima-rd/r-d5450df7-166c-45e3-9289-df195a475493

## Customize
- Update the `<YOUR_GITHUB_USERNAME>` placeholder in `index.html`, `sitemap.xml`, and `robots.txt`.
- Swap the favicon in `<head>` with your own SVG/PNG.
- If you have official logo files/brand colors, add them in `assets/css/styles.css` and replace the badge.



## Self‑Host the Photos (Optional)
> Only if you have rights/permission to host these images.

1. Ensure you have Python 3 (or use the included Bash script).
2. Run one of:
   - `python3 scripts/fetch_images.py`
   - `bash scripts/fetch_images.sh`
3. Commit & push the downloaded files under `assets/images/lucilles/` to your repo.
4. The site points to local files first and falls back to public URLs if a file is missing.

### Credits
See `ATTRIBUTIONS.md` and `photos.html` for source pages.
