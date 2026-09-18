# A scroll for Shreya 🍥

A small Naruto-themed Streamlit app. Five sections, one honest question at the
end. Every picture in it is made of text — there are no image files in this
repository.

## What's inside

| Section | What it does |
| --- | --- |
| The summoning | A large Uzumaki spiral generated at runtime out of the words NARUTO, KONOHA, RASENGAN, RAMEN and friends |
| The scroll | The original message, typed out character by character on a washi-paper scroll |
| Japanese corner | Her name in katakana, greetings, words for friendship, and a six-kana check |
| Chunin exam | A six-question Naruto quiz that hands out a ninja rank |
| The bond | Interest picker, the friendship question, and a downloadable "friendship scroll" |

The spiral is not ASCII art pasted from somewhere. `ascii_art.py` walks an
Archimedean spiral by arc length and stamps keyword letters along the path, then
adds a quadratic Bézier tail for the leaf hook, so the shape is literally drawn
out of words.

## Run it locally

```bash
git clone <your-repo-url>
cd <your-repo>
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

It opens at http://localhost:8501.

## Put it online (free)

1. Push this folder to a public GitHub repository.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **New app**, pick the repo, set the main file to `app.py`, deploy.
4. Send her the link.

## Checking the art without running the app

```bash
python preview_art.py
```

That writes `art_preview.html` with every picture rendered using the exact
markup the app uses. Open it in a browser — if it lines up there, it lines up in
the app. The script also fails loudly if any art contains a non-ASCII character.

## Why the text art stays aligned

Text art is whitespace that means something, and three ordinary things destroy
it. All three are handled:

1. **`st.markdown` reflows whitespace.** It runs input through a Markdown parser
   before the HTML reaches the browser. Art goes through `st.html` instead,
   which passes markup straight through, with a fallback to `st.markdown` on
   Streamlit older than 1.33.
2. **Stylesheet rules lose to Streamlit's own CSS.** Every property the art
   depends on — font, size, line-height, letter-spacing, `white-space` — is set
   inline on the `<pre>`, where nothing can override it.
3. **Not every character is one cell wide.** Block characters, box-drawing
   characters and kanji (`#`, `|` are fine; `█`, `═`, `卍`, `●` are not) render
   at different widths in browser monospace fonts, which shears rows apart.
   `ascii_art.py` is plain 7-bit ASCII only, and `is_pure_ascii()` enforces it.

The block lettering is built from a 7-row ASCII font in `GLYPHS` rather than
spaces counted by hand, so words like NARUTO and SHREYA cannot drift out of
step.

## Files

```
app.py                 page layout and flow
ascii_art.py           the text pictures, including the generated spiral
render.py              turns text art into HTML that keeps its alignment
styles.py              the washi-paper theme, and the Streamlit-side rendering
content.py             message text, Japanese vocabulary, quiz questions
preview_art.py         writes art_preview.html to check the art in a browser
.streamlit/config.toml Streamlit's own colour theme
requirements.txt       one dependency
```

## Things worth changing

- `content.py` → `ORIGINAL_MESSAGE` is the message as sent. Edit it there.
- `content.py` → `INTEREST_CHIPS` if you want different interest options.
- `ascii_art.py` → `KEYWORD_STRING` changes the words the spiral is woven from.
  Keep any edit inside plain ASCII.
- `ascii_art.py` → `uzumaki_swirl(width=, height=, turns=)` changes its size and
  how many times it winds.
- `styles.py` → the `:root` block holds every colour in one place.

## A note

The three answers on the last page are all treated as real answers, including
the one that says no. That was deliberate — an app that only accepts "yes" is a
worse gift than one that means it.

Naruto is the work of Masashi Kishimoto and Shueisha. This is a personal fan
project and is not affiliated with or endorsed by them.
