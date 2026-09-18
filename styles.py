"""
styles.py
---------
The look of the app, and — more importantly — the one function that renders
text art without Streamlit chewing it up.

Why the art broke before, and what fixes it:

1. st.markdown() runs its input through a Markdown parser before the HTML
   reaches the browser. That parser re-indents and re-wraps whitespace, which
   destroys anything whose meaning IS its whitespace. Fix: render through
   st.html(), which passes the HTML straight through. Older Streamlit versions
   fall back to st.markdown.

2. Styling art from a stylesheet is fragile, because Streamlit's own CSS can
   land after yours. Fix: every property the art depends on (font, size,
   line-height, letter-spacing, white-space) is set inline on the <pre>.

3. A webfont like IBM Plex Mono may not have finished loading, or may lack a
   glyph and silently fall back to a proportional face for that one character.
   Fix: art uses the system monospace stack only. Webfonts are for prose.

4. Non-ASCII characters are not one cell wide. See the note in ascii_art.py.
"""

import html as _html

import streamlit as st

from render import art_markup

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap');

:root {
  --washi:       #F2E7D0;
  --washi-deep:  #E7D7B6;
  --sumi:        #241E18;
  --sumi-soft:   #5C5145;
  --kyara:       #E1651B;   /* Naruto orange */
  --vermilion:   #B3322A;   /* seal red */
  --ai:          #22364F;   /* indigo */
}

.stApp {
  background-color: var(--washi);
  background-image:
    radial-gradient(circle at 18% 12%, rgba(179,50,42,.05) 0 38%, transparent 38%),
    radial-gradient(circle at 82% 78%, rgba(34,54,79,.05) 0 42%, transparent 42%);
  color: var(--sumi);
}
.block-container { padding-top: 2.2rem; max-width: 1080px; }

html, body, [class*="css"], .stMarkdown, p, li, label {
  font-family: 'Zen Kaku Gothic New', system-ui, sans-serif;
  color: var(--sumi);
}
p, li { line-height: 1.75; max-width: 68ch; }

h1, h2, h3 {
  font-family: 'Shippori Mincho', Georgia, serif;
  color: var(--sumi);
  letter-spacing: .01em;
}
h1 { font-size: clamp(1.8rem, 4.4vw, 3rem); line-height: 1.15; }
h2 { font-size: clamp(1.3rem, 2.6vw, 1.9rem); margin-top: 1.6rem; }

.scroll {
  background: linear-gradient(180deg, #FBF3E2 0%, #F3E5C9 100%);
  border-left: 6px solid var(--vermilion);
  border-radius: 2px 10px 10px 2px;
  padding: 1.6rem 1.8rem;
  box-shadow: inset 0 0 0 1px rgba(36,30,24,.08);
}
.scroll .brush {
  font-family: 'Shippori Mincho', serif;
  font-size: 1.12rem;
  line-height: 2;
  white-space: pre-wrap;
}

.kanji-big {
  font-family: 'Shippori Mincho', serif;
  font-size: clamp(2.6rem, 7vw, 4.4rem);
  color: var(--ai);
  line-height: 1.1;
}
.romaji { color: var(--sumi-soft); font-size: .95rem; }
.rule {
  height: 1px;
  background: linear-gradient(90deg, var(--kyara), transparent);
  border: 0; margin: 1.6rem 0;
}
.caption { color: var(--sumi-soft); font-size: .88rem; }

section[data-testid="stSidebar"] {
  background: var(--washi-deep);
  border-right: 1px solid rgba(36,30,24,.12);
}
.stButton > button {
  font-family: 'Zen Kaku Gothic New', sans-serif;
  font-weight: 700;
  background: var(--kyara);
  color: #FFF7EC;
  border: 0;
  border-radius: 6px;
  padding: .55rem 1.2rem;
}
.stButton > button:hover { background: #C9550F; color: #FFF7EC; }
.stButton > button:focus-visible { outline: 3px solid var(--ai); outline-offset: 2px; }

div[data-testid="stMetricValue"] { font-family: 'Shippori Mincho', serif; }

@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
</style>
"""

def _write_html(markup, container=None):
    """Emit raw HTML, preferring st.html so Markdown never touches it."""
    target = container if container is not None else st
    if hasattr(target, "html"):
        target.html(markup)
    else:  # Streamlit < 1.33
        target.markdown(markup, unsafe_allow_html=True)


def inject_css():
    # A <style> block is not whitespace-sensitive, so plain markdown is fine
    # here and works on every Streamlit version.
    st.markdown(CSS, unsafe_allow_html=True)


def art(text, kind="art-plain", container=None):
    """Render a block of text art with its alignment intact."""
    _write_html(art_markup(text, kind), container)


def scroll_panel(text, cursor="", container=None):
    """The washi scroll used for the message."""
    body = _html.escape(text) + cursor
    _write_html(
        f'<div class="scroll"><div class="brush">{body}</div></div>', container
    )


def caption(text):
    _write_html(f'<p class="caption" style="text-align:center">{text}</p>')


def rule():
    _write_html('<hr class="rule">')
