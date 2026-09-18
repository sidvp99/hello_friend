"""
preview_art.py
--------------
Writes art_preview.html — every piece of text art, rendered with exactly the
same markup the app uses. Open it in a browser to check alignment without
starting Streamlit.

    python preview_art.py && open art_preview.html      # macOS
    python preview_art.py && start art_preview.html     # Windows
    python preview_art.py && xdg-open art_preview.html  # Linux

It also asserts that nothing has crept in outside plain ASCII, which is the
single most common cause of text art falling apart in a browser.
"""

import ascii_art as A
from render import art_markup

PIECES = [
    ("NARUTO logo", A.LOGO, "art-logo"),
    ("Uzumaki swirl, woven from keywords", A.uzumaki_swirl(), "art-swirl"),
    ("SHREYA", A.SHREYA, "art-blue"),
    ("Naruto", A.FACE, "art-face"),
    ("Ichiraku", A.RAMEN, "art-plain"),
    ("Headband", A.HEADBAND, "art-plain"),
    ("Rasengan, frame 0", A.rasengan(0), "art-mini"),
]

PAGE = """<!doctype html>
<html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Text art preview</title>
<style>
  body {{ background:#F2E7D0; color:#241E18; margin:0; padding:2rem 1rem;
         font-family:system-ui, sans-serif; }}
  .wrap {{ max-width:1080px; margin:0 auto; }}
  h2 {{ font-size:.95rem; font-weight:600; color:#5C5145; margin:2.4rem 0 .4rem; }}
</style></head>
<body><div class="wrap">
<p>If every picture below lines up here, it will line up in the app.</p>
{blocks}
</div></body></html>
"""


def main():
    blocks = []
    for label, text, kind in PIECES:
        assert A.is_pure_ascii(text), f"{label} contains a non-ASCII character"
        blocks.append(f"<h2>{label}</h2>\n{art_markup(text, kind)}")
    with open("art_preview.html", "w", encoding="utf-8") as fh:
        fh.write(PAGE.format(blocks="\n".join(blocks)))
    print("Wrote art_preview.html — open it in a browser.")


if __name__ == "__main__":
    main()
