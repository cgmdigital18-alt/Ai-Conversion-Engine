# Edge21 editorial carousel

A reusable ten-slide Instagram carousel adapted from the source in [historical PR #1](https://github.com/cgmdigital18-alt/Ai-Conversion-Engine/pull/1), commit `8162b1d810c540fedd7bbf207d158bd15eee2276`.

Open **carousel-ai-edge21.html** in a desktop browser. The file is self-contained, includes licensed offline fonts, and provides copy editing, save-as-HTML, design guides, 3:4/4:5 preview switching, and 3:4 PDF printing.

- [Canva specifications](docs/CANVA-SPECIFICATIONS.md): dimensions, guide positions, type hierarchy, spacing, reuse, and exports.
- [Exact layer reference](docs/LAYER-REFERENCE.md): every text and shape coordinate.
- [Content review](docs/CONTENT-REVIEW.md): all ten original slides, retain/remove decisions and rationale.
- `slide-specifications.json`: machine-readable layer geometry and copy.
- `assets/fonts`: source fonts and OFL licenses. Fonts are also embedded in the HTML.

## Export

```sh
npm install --no-save playwright
npx playwright install chromium
node scripts/export-slides.cjs
```

This creates ten 1080 x 1440 PNGs, ten 1080 x 1350 PNGs, a 3:4 review PDF, and a QA report under ignored `exports/`. It checks text bounds, shared critical-text margins, dimensions, browser errors, editing, guides, and saved HTML.

To rebuild after changing `scripts/build_carousel.py`:

```sh
python3 scripts/build_carousel.py
node scripts/export-slides.cjs
```

The builder overwrites the HTML and generated layer data. Browser copy edits persist only in a saved HTML download until that file replaces the original. Rebuilding from Python does not incorporate browser edits.

No merge, publishing schedule, approved campaign status, client result, or automated DM flow is implied by this template or the status of the historical PR.
