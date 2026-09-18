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

## Files

```
app.py                 page layout and flow
ascii_art.py           the text pictures, including the generated spiral
content.py             message text, Japanese vocabulary, quiz questions
styles.py              the washi-paper theme (CSS)
.streamlit/config.toml Streamlit's own colour theme
requirements.txt       one dependency
```

## Things worth changing

- `content.py` → `ORIGINAL_MESSAGE` is the message as sent. Edit it there.
- `content.py` → `INTEREST_CHIPS` if you want different interest options.
- `ascii_art.py` → `KEYWORD_STRING` changes the words the spiral is woven from.
- `ascii_art.py` → `uzumaki_swirl(width=, height=, turns=)` changes its size and
  how many times it winds.
- `styles.py` → the `:root` block holds every colour in one place.

## A note

The three answers on the last page are all treated as real answers, including
the one that says no. That was deliberate — an app that only accepts "yes" is a
worse gift than one that means it.

Naruto is the work of Masashi Kishimoto and Shueisha. This is a personal fan
project and is not affiliated with or endorsed by them.
