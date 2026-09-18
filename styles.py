"""
styles.py
---------
One place for the look of the app: a washi-paper scroll, sumi ink,
a vermilion seal, and Naruto orange used only where it earns attention.
"""

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&family=IBM+Plex+Mono:wght@400;600&display=swap');

:root {
  --washi:       #F2E7D0;
  --washi-deep:  #E7D7B6;
  --sumi:        #241E18;
  --sumi-soft:   #5C5145;
  --kyara:       #E1651B;   /* Naruto orange */
  --vermilion:   #B3322A;   /* seal red */
  --ai:          #22364F;   /* indigo */
  --leaf:        #4F7A45;
}

/* --- page ------------------------------------------------------------- */
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

/* --- text pictures ----------------------------------------------------- */
.art {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  white-space: pre;
  overflow-x: auto;
  line-height: 1.02;
  letter-spacing: .02em;
  margin: 0;
}
.art-swirl {
  font-size: clamp(3.4px, 1.02vw, 11px);
  color: var(--kyara);
  text-align: center;
  font-weight: 600;
}
.art-logo   { font-size: clamp(3.6px, 1.06vw, 12px); color: var(--vermilion); text-align: center; }
.art-plain  { font-size: clamp(4px, 1.1vw, 12px);   color: var(--sumi-soft); text-align: center; }
.art-blue   { font-size: clamp(4px, 1.1vw, 12px);   color: var(--ai);        text-align: center; }
.art-mini   { font-size: 9px; color: var(--ai); text-align: center; }

/* --- scroll panel ------------------------------------------------------ */
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

/* --- small pieces ------------------------------------------------------ */
.seal {
  display: inline-block;
  background: var(--vermilion);
  color: #FBF3E2;
  font-family: 'Shippori Mincho', serif;
  padding: .45rem .6rem;
  border-radius: 4px;
  writing-mode: vertical-rl;
  letter-spacing: .3em;
}
.kanji-big {
  font-family: 'Shippori Mincho', serif;
  font-size: clamp(2.6rem, 7vw, 4.4rem);
  color: var(--ai);
  line-height: 1;
}
.romaji { color: var(--sumi-soft); font-size: .95rem; }
.rule {
  height: 1px;
  background: linear-gradient(90deg, var(--kyara), transparent);
  border: 0; margin: 1.6rem 0;
}
.caption { color: var(--sumi-soft); font-size: .88rem; }

/* --- streamlit widgets ------------------------------------------------- */
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


def inject_css():
    st.markdown(CSS, unsafe_allow_html=True)


def art(text, kind="art-plain"):
    """Render a block of text art."""
    import html as _html

    st.markdown(
        f'<pre class="art {kind}">{_html.escape(text)}</pre>',
        unsafe_allow_html=True,
    )
