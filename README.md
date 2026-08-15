# Golf Trip Itineraries 🏌️

Two trips, two pages, one repo.

| Trip | Page | Link |
| --- | --- | --- |
| **Forest Dunes Cup 2026** — Golf Boyz, Michigan | `index.html` | [/](https://jkalson11.github.io/forest-dunes-cup-2026/) |
| **The Kalson Cup 2026** — Father & Son, Whistling Straits | `whistling-straits/index.html` | [/whistling-straits/](https://jkalson11.github.io/forest-dunes-cup-2026/whistling-straits/) |

## The Kalson Cup — Whistling Straits, 20–23 August 2026

Kohler, Wisconsin. Four players, six rounds, five Pete Dye courses. The page
covers the field, the full itinerary with real tee times and dinner
confirmations, course profiles, the Straits scorecard, the match format, and
the running record of past editions.

Open items are marked in the page with a small **To confirm** chip — search
`whistling-straits/index.html` for `class="tbd"` to find every one at once.

Photographs go in `whistling-straits/img/` — see the README in that folder for
the filenames the page looks for. Until a file exists, the page falls back to
its own engraved artwork, so nothing breaks.

## Forest Dunes Cup 2026

The Golf Boyz Michigan Trip 2026 itinerary — a single, self-contained web page
(`index.html`) with all images baked in, so it looks great on any phone.

## 📱 The shareable link

Once GitHub Pages is turned on (one-time, see below), the page is live at:

**https://jkalson11.github.io/forest-dunes-cup-2026/**

Text that link to the boyz — it opens instantly in any phone browser, no app or
download needed.

## ✅ One-time setup (turn the link on)

This only has to be done once:

1. Go to the repo on GitHub → **Settings** → **Pages** (left sidebar).
2. Under **Build and deployment → Source**, choose **GitHub Actions**.
3. That's it. The included workflow (`.github/workflows/deploy.yml`) publishes the
   site automatically. Give it about a minute, then open the link above.

> Prefer not to use Actions? You can instead pick **Deploy from a branch → `main` →
> `/ (root)` → Save**. The page is served the same way either way.

## ✏️ Updating the page

Edit `index.html`, commit to `main`, and the site re-deploys automatically.
