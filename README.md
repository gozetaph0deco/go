# QR Redirect / Coming Soon Page

This is the page your printed QR code points to. The QR encodes:

    https://gozetaph0deco.github.io/go/

**Never reprint the QR.** This one page does two jobs:

- **Now:** shows a "Coming Soon" page (because `DESTINATION` is empty).
- **Later:** auto-redirects to your real site (once you fill `DESTINATION` in).

## First-time setup

1. Create a new GitHub repo named **`go`** (Public).
2. Upload `index.html` (and this README) into it.
3. Go to repo **Settings -> Pages**.
4. Build and deployment: **Source = Deploy from a branch**,
   **Branch = main**, folder **/(root)**, then Save.
5. Wait 1-2 minutes. Your Coming Soon page is live at:

       https://gozetaph0deco.github.io/go/

## When your website is ready (flip to redirect)

1. Open `index.html` on GitHub, click the pencil (Edit) icon.
2. Find this line near the top:

       var DESTINATION = "";

3. Put your new site URL inside the quotes, e.g.:

       var DESTINATION = "https://gozetaph0deco.github.io/mysite/";

4. Click **Commit changes**.
5. Wait ~1 minute. The same QR now leads straight to your site.

To go back to Coming Soon, just empty it again: `var DESTINATION = "";`

## Regenerate the QR (only if the github.io URL ever changes)

    python make_qr.py
