# The anthem

The cover carries a small player wired to one file:

```
whistling-straits/audio/swingtown.mp3
```

Drop that file in and the player appears on its own. Until it exists, the cover
shows a single quiet credit line instead — *Anthem — Swingtown, Steve Miller
Band* — so the page still looks finished either way. Nothing breaks.

## Adding it

Open this folder on GitHub, choose **Add file → Upload files**, drag the MP3
in, and commit. The site redeploys by itself. The filename must match exactly,
in lower case.

## Notes

- MP3 is the safe format; every phone browser plays it. M4A also works if that
  is what you have — rename the `src` in `index.html` to match.
- Keep it under about 10 MB so the page still opens quickly on cell service.
- The player never autoplays. Phone browsers block that anyway, and a page that
  starts making noise on its own is exactly the thing this design is avoiding.
- Use a copy you own. Don't commit anything you wouldn't be comfortable having
  sitting in a public repository — GitHub Pages sites are public, and this one
  is shared by link.
