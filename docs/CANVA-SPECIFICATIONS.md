# Edge21 editorial carousel: Canva specifications

## Canvas and formats

Master: **1080 × 1440 px, 3:4**, ten separate pages. This is the preferred file for a direct upload through Instagram's app. Alternative: **1080 × 1350 px, 4:5**, provided for publishing tools using Meta's documented API ratio range.

The 4:5 export removes 45 px from the top and bottom of the master. It does not stretch the artwork or reflow the text. For a manual Canva rebuild on the 4:5 canvas, keep each X coordinate and width unchanged, subtract 45 from every Y coordinate, and extend the page background to the new edges.

Instagram's Help Center lists photo ratios through 3:4. Meta's media-publishing reference lists 4:5 through 1.91:1. Choose the set matching the publishing route. All ten images in a post should use the same set and ratio. Specs checked October 21, 2026.

## Canva setup, step by step

1. Create a design with custom dimensions. Enter width **1080**, height **1440**, units **px**.
2. Create ten pages. Enter the page background colors listed in the slide data.
3. Open **File > Rulers and guides > Show rulers and guides**. Menu wording varies by editor version. Add individual guides from the rulers and lock them.
4. For vertical guides, use these positions along the **top horizontal ruler**: **90, 96, 540, 984, 990**. The content edges are 96 and 984. The center is 540. The outer 90 and 990 guides mark the wider safety boundary.
5. For horizontal guides, use these positions down the **left vertical ruler**: **45, 170, 180, 244, 1260, 1312, 1395**. The shared critical-text region is y 180 to 1260. The 45 and 1395 guides show the optional 4:5 crop.
6. Add the headline, emphasis, body, rules, and cards using the exact per-slide layer references. Use **Position** controls to set X, Y and width where available. Preserve the supplied line breaks.
7. Place the approved Edge21 logo from your Brand Kit in the header. The supplied HTML uses a text brand label because an official logo file was not supplied. Keep Midland Luxury in the brand system. The portable typefaces below are an editorial pairing for this template.
8. Duplicate a matching page to reuse a layout. Replace the copy, then recheck the supplied line lengths and the shared critical-text region.

## Spacing and crop logic

| Element | Master position or size |
| --- | --- |
| Main left / right text edges | x 96 / 984 |
| Main text width | 888 px |
| Shared critical-text area | x 90–990, y 180–1260 |
| Header brand label | x 96, y 100 |
| Slide number | Right edge x 984, y 110 |
| Header rule | x 96, y 170, width 888, thickness 2 |
| Main headline default top | y 244, exceptions in layer reference |
| Footer row | x 96–984, y 1312 |
| Two-column card starts | x 96 and 552 |
| Two-column rule width / gutter | 432 / 24 px |
| Card inner padding | Usually 32 or 36 px, see layers |
| Baseline spacing rhythm | 8 px, with optical adjustments for type |

The master matches a 3:4 portrait tile. For the 4:5 version, a centered 3:4 tile would show 1012.5 px of its width, trimming approximately 33.75 px from each side. This is geometry, not a guaranteed Instagram crop. The 96 px text margin leaves about 62 px beyond such a crop. The y 180–1260 region also keeps the core story inside a centered square preview of the master. Header and footer are secondary and need not survive every alternate preview. Check the actual account preview before publishing. These guides are design allowances, not official platform safe-zone measurements.

## Palette and type hierarchy

| Role | Value | Use |
| --- | --- | --- |
| Navy | #00306C | Primary text and dark pages |
| Light teal | #D2F2FB | Process pages and example panels |
| Warm cream | #FFF0CD | Editorial page background and reverse text |
| Soft gold | #FFE7AF | Selective emphasis and CTA panel |
| White | #FFFFFF | Breathing room on evidence and check pages |

Use navy text on teal, cream, gold, or white. Use cream, teal, or gold on navy. Avoid light-on-light text. Do not add gradients, glows, shadows, stock AI icons, or texture overlays.

| Role | Font and weight | Source size | Line height | Tracking |
| --- | --- | --- | --- | --- |
| Hero headline | Barlow Condensed Bold 700 | 138–148 px | 0.99 | -0.012 em |
| Interior headline | Barlow Condensed Bold 700 | 108–130 px | 0.99 | -0.012 em |
| Editorial emphasis | Libre Baskerville Italic 400 | 52–100 px | 1.14–1.16 | -0.035 em when emphasis class |
| Body | DM Sans Medium 500 | 34–43 px, selected 28–30 px notes | 1.20–1.25 | 0 |
| Card lead | Barlow Condensed Bold 700 | 48–58 px | 1.00–1.05 | 0 |
| Section label | DM Sans Bold 700 | 24 px | 1.15 | +0.055 em |
| CTA URL | Barlow Condensed Bold 700 | 52 px | 1.00 | 0 |
| Secondary footer | DM Sans Bold 700 | 21–23 px | Normal | 0 |

Font sizes in the layer reference are **rendered CSS pixels**, not a claim of exact equivalence with Canva's font-size field. If the editor uses points, px × 0.75 is a starting conversion at 96 dpi. Set the exact text-box width and match the reference line breaks and overall rendered height. The exported images are the visual reference. Set letter spacing using the equivalent em value when supported, or visually match the reference. Do not stretch text to fit.

The fonts are embedded in the standalone HTML for offline rendering. Original font files and their OFL licenses are included in the repository. Libre Baskerville is a selective accent, never the small body face.

## Slide structure

| Page | Background | Purpose | Source relationship |
| --- | --- | --- | --- |
| 01 | Navy | Service-business hook | Replaces generic AI status claim |
| 02 | Cream | Unowned inquiry example | Replaces unsupported percentage |
| 03 | Teal | Document the workflow | Preserves systems idea |
| 04 | White | Reuse a real buyer question | Preserves content reuse |
| 05 | Navy | Quote follow-up fields | Preserves lead handling |
| 06 | Cream | Define meaningful measures | Preserves decision support |
| 07 | Teal | Bound the AI drafting task | Replaces output multiplier |
| 08 | White | Five-record spot check | Replaces generic results |
| 09 | Cream | Current positioning | Rewrites brand promise |
| 10 | Navy | One services CTA | Removes unverified cadence |

## Export and publishing

1. Export all ten pages as separate **PNG** images at **1×** for the master archive and direct app upload. Opaque backgrounds, no bleed, crop marks, animation, or transparency.
2. For the API route, use the supplied **1080 × 1350 JPG** files. They use sRGB, quality 95, and remain below Meta's documented 8 MB per-image limit. A scheduler should preserve their dimensions rather than add bars.
3. Keep order **edge21-01** through **edge21-10**. Select slide 01 first. Use a consistent ratio across all ten.
4. Inspect the carousel feed preview and the cover's profile-grid preview. Confirm the entire headline and URL remain visible. Do not crop each slide separately.
5. For Canva exports, use 1× and verify the downloaded dimensions. DPI does not add pixels to an Instagram export. The review PDF is for reading and reference, not the image upload set.
6. Treat the example cards as examples. Add real results only when supported by a documented baseline, date range, and source.

## Reuse the HTML

Open `carousel-ai-edge21.html` in a current desktop browser. It needs no server or font connection. Use **Edit copy**, finish editing, then **Save template** to download the edited standalone HTML. Changes are not automatically saved by the browser. Keep replacements within existing line lengths. The save button preserves the HTML, not the JSON source or exported PNGs. The format selector and guides are preview controls.

**Print 3:4 PDF** always prints the full 3:4 master, even when the preview selector shows 4:5. Choose no margins and enable background graphics if your browser asks. The included PDF was generated at exact page proportions. For deterministic image export from the saved HTML, the repository includes `scripts/export-slides.cjs`. To preserve visual edits in that export, point the script to the saved file by replacing the original HTML file first. Running the Python builder instead regenerates from the Python source and overwrites visual copy edits.

For programmatic edits, change `scripts/build_carousel.py`, run the builder, then run the export script. `slide-specifications.json` stores every layer's X, Y, width, font, size, line height, weight, color and exact text. The generated layer reference below is the manual Canva blueprint.

## Sources

- Historical HTML: https://github.com/cgmdigital18-alt/Ai-Conversion-Engine/pull/1
- Instagram Help Center, photo resolution: https://help.instagram.com/1631821640426723/
- Meta, IG User Media: https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media
- Canva, guides: https://www.canva.com/help/adding-and-removing-guides/

The creative and spacing choices are design recommendations. The cited platform documents support the format and editor guidance, not claims of reach, engagement, or sales performance.
