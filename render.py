"""
render.py
---------
Turns a block of text art into HTML. No Streamlit import here on purpose, so
preview_art.py can use exactly the same markup to check alignment in a plain
browser, without starting the app.

Everything the art depends on is set inline on the <pre>. Stylesheet rules can
be overridden by Streamlit's own CSS; inline styles cannot.
"""

import html as _html

# System monospace only. A webfont can fail to load, or lack one glyph and fall
# back to a proportional face for just that character, which shears the art.
MONO = (
    "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
    "'Liberation Mono', 'DejaVu Sans Mono', 'Courier New', monospace"
)

# kind -> (colour, font-size, weight). Sizes are clamped so a wide picture
# shrinks on a phone instead of wrapping, and never gets silly on a big screen.
ART_KINDS = {
    "art-swirl": ("#E1651B", "clamp(4.4px, 1.22vw, 12px)", "700"),
    "art-logo":  ("#B3322A", "clamp(5.5px, 1.55vw, 17px)", "700"),
    "art-blue":  ("#22364F", "clamp(5.5px, 1.55vw, 17px)", "700"),
    "art-plain": ("#5C5145", "clamp(5.5px, 1.45vw, 15px)", "400"),
    "art-face":  ("#241E18", "clamp(5px, 1.4vw, 15px)",    "400"),
    "art-mini":  ("#22364F", "11px",                       "400"),
}


def art_markup(text, kind="art-plain"):
    """Wrap text art in a <pre> that keeps its alignment."""
    colour, size, weight = ART_KINDS.get(kind, ART_KINDS["art-plain"])
    body = _html.escape(text.strip("\n"))
    return (
        '<div style="width:100%;overflow-x:auto;text-align:center;'
        'margin:.35rem 0 .2rem 0">'
        "<pre style="
        f'"display:inline-block;text-align:left;margin:0;padding:0;'
        f"font-family:{MONO};"
        f"font-size:{size};line-height:1.16;letter-spacing:0;word-spacing:0;"
        f"white-space:pre;tab-size:4;font-variant-ligatures:none;"
        f'font-weight:{weight};color:{colour};background:none;border:0">'
        f"{body}</pre></div>"
    )
