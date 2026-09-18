"""
A friendship scroll for Shreya.

Run it with:  streamlit run app.py
"""

import random
import time
from datetime import date

import streamlit as st

import ascii_art as A
import content as C
from styles import art, caption, inject_css, rule, scroll_panel

st.set_page_config(
    page_title="A scroll for Shreya",
    page_icon="🍥",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_css()


# --------------------------------------------------------------------- state
def init_state():
    defaults = {
        "visited": set(),
        "quiz_score": None,
        "kana_score": 0,
        "answer": None,
        "interests": [],
        "spark": [],
        "note_back": "",
    }
    for k, v in defaults.items():
        st.session_state.setdefault(k, v)


init_state()


# ------------------------------------------------------------------ helpers
def typewriter(text, key, speed=0.012):
    """Write text out one character at a time — but only the first time."""
    box = st.empty()
    if st.session_state.get(f"typed_{key}"):
        scroll_panel(text, container=box)
        return
    shown = ""
    for ch in text:
        shown += ch
        scroll_panel(shown, cursor="|", container=box)
        time.sleep(speed)
    scroll_panel(text, container=box)
    st.session_state[f"typed_{key}"] = True


def line_of_the_day():
    # Stable for the whole day so it doesn't flicker on every rerun.
    return random.Random(date.today().toordinal()).choice(C.NINJA_WAY)


def word_card(kanji, romaji, meaning):
    st.markdown(
        f'<div class="kanji-big">{kanji}</div>'
        f'<div class="romaji">{romaji}</div>',
        unsafe_allow_html=True,
    )
    st.write(meaning)


# -------------------------------------------------------------------- pages
def page_home():
    art(A.LOGO, "art-logo")
    caption("Every picture here is built out of text. There is not one image file in this app.")

    art(A.uzumaki_swirl(width=90, height=40), "art-swirl")
    caption(
        "The Uzumaki spiral, drawn by walking a curve and laying the words "
        "NARUTO . KONOHA . RASENGAN . RAMEN . KIZUNA along the path."
    )

    rule()

    left, right = st.columns([3, 2], gap="large")
    with left:
        st.markdown("## For Shreya")
        st.write(
            "I made this instead of sending another text. It is a very small "
            "village: five sections, one honest question at the end of it."
        )
        st.write(
            "Use the sidebar to walk through it, or start with the scroll — "
            "that is the message I actually sent you, set down properly."
        )
        st.markdown(f"**Ninja way for today.** {line_of_the_day()}")
    with right:
        art(A.SHREYA, "art-blue")
        caption("シュレヤ &middot; Shureya")


def page_scroll():
    st.markdown("## The scroll")
    st.write("The message, unrolled.")
    typewriter(C.ORIGINAL_MESSAGE, key="scroll")
    rule()

    left, right = st.columns([3, 2], gap="large")
    with left:
        st.markdown("### What I meant by it")
        st.write(
            "Nothing complicated. You came across as someone worth knowing, and "
            "the interest in Japanese made me curious, because picking up a "
            "language is a slow, stubborn thing to do — people only do it when "
            "something really caught them."
        )
        st.write("So the rest of this is me being curious out loud, and then asking properly.")
    with right:
        art(A.RAMEN, "art-plain")
        caption("Ichiraku rules: one bowl, no agenda.")


def page_japanese():
    st.markdown("## 日本語 · the Japanese corner")
    st.write(
        "Built around your interest rather than mine. Everything below is real "
        "vocabulary, and the last tab is a quick check."
    )

    cols = st.columns(len(C.NAME_IN_KATAKANA) + 1)
    with cols[0]:
        st.markdown("**Your name in katakana**")
        st.markdown(
            '<p class="caption">Katakana is the script Japanese uses for names '
            "from other languages.</p>",
            unsafe_allow_html=True,
        )
    for col, (kana, roma) in zip(cols[1:], C.NAME_IN_KATAKANA):
        with col:
            st.markdown(
                f'<div class="kanji-big">{kana}</div>'
                f'<div class="romaji">{roma}</div>',
                unsafe_allow_html=True,
            )

    rule()
    t1, t2, t3 = st.tabs(["Greetings", "Words for a bond", "Kana check"])

    with t1:
        for kana, roma, meaning in C.GREETINGS:
            a, b = st.columns([1, 2])
            with a:
                st.markdown(
                    '<div style="font-family:Shippori Mincho,serif;font-size:1.9rem">'
                    f"{kana}</div>"
                    f'<div class="romaji">{roma}</div>',
                    unsafe_allow_html=True,
                )
            with b:
                st.write(meaning)

    with t2:
        grid = st.columns(2, gap="large")
        for i, (kanji, roma, meaning) in enumerate(C.FRIENDSHIP_WORDS):
            with grid[i % 2]:
                word_card(kanji, roma, meaning)

    with t3:
        st.write("Six kana. Type the sound each one makes.")
        with st.form("kana"):
            guesses = []
            row = st.columns(len(C.KANA_QUIZ))
            for col, (kana, _) in zip(row, C.KANA_QUIZ):
                with col:
                    st.markdown(
                        f'<div class="kanji-big" style="font-size:2.6rem">{kana}</div>',
                        unsafe_allow_html=True,
                    )
                    guesses.append(
                        st.text_input(kana, key=f"kana_{kana}", label_visibility="collapsed")
                    )
            checked = st.form_submit_button("Check my answers")
        if checked:
            right = sum(
                1 for g, (_, ans) in zip(guesses, C.KANA_QUIZ)
                if g.strip().lower() == ans
            )
            st.session_state.kana_score = right
            st.success(f"{right} of {len(C.KANA_QUIZ)}.")
            st.write("Answers: " + " · ".join(f"{k} = {v}" for k, v in C.KANA_QUIZ))

    rule()
    st.markdown("### The question I actually wanted to ask")
    st.write("What sparked it for you? Pick anything that fits.")
    st.session_state.spark = st.multiselect(
        "What sparked your interest in Japanese",
        C.WHY_JAPANESE,
        default=st.session_state.spark,
        label_visibility="collapsed",
    )
    if st.session_state.spark:
        st.info("Noted. I want the long version of this in person, though.")


def page_exam():
    st.markdown("## 中忍試験 · the chunin exam")
    st.write("Six questions. No pressure, there is a rank for everyone.")

    with st.form("exam"):
        picks = []
        for i, item in enumerate(C.QUIZ):
            st.markdown(f"**{i + 1}. {item['q']}**")
            picks.append(
                st.radio(
                    item["q"],
                    item["options"],
                    index=None,
                    key=f"q{i}",
                    label_visibility="collapsed",
                )
            )
        submitted = st.form_submit_button("Submit answers")

    if not submitted:
        return

    score = sum(
        1 for pick, item in zip(picks, C.QUIZ)
        if pick == item["options"][item["answer"]]
    )
    st.session_state.quiz_score = score
    rank, blurb = C.RANKS[0][1], C.RANKS[0][2]
    for threshold, name, note in C.RANKS:
        if score >= threshold:
            rank, blurb = name, note

    rule()
    a, b = st.columns([1, 2])
    with a:
        st.metric("Score", f"{score} / {len(C.QUIZ)}")
        st.metric("Rank", rank)
    with b:
        st.write(blurb)
        for pick, item in zip(picks, C.QUIZ):
            correct = item["options"][item["answer"]]
            mark = "○" if pick == correct else "×"
            st.markdown(f"{mark} **{correct}** — {item['note']}")
    if score == len(C.QUIZ):
        st.balloons()
    art(A.HEADBAND, "art-plain")


def page_bond():
    st.markdown("## 絆 · the bond")
    art(A.FACE, "art-face")
    caption("Drawn in text, badly, with real affection.")
    rule()

    st.markdown("### First, the part I asked about")
    st.write("Tap whatever you're into. This is the bit I'm actually curious about.")
    st.session_state.interests = st.multiselect(
        "Your interests",
        C.INTEREST_CHIPS,
        default=st.session_state.interests,
        label_visibility="collapsed",
    )
    st.session_state.note_back = st.text_area(
        "Anything the list missed",
        value=st.session_state.note_back,
        placeholder="The thing you'd talk about for an hour without noticing.",
        height=90,
    )

    rule()
    st.markdown("### And the ask")
    st.write(
        "No cleverness here. I'd like to be friends — the ordinary kind, where "
        "we talk about whatever, at whatever pace suits you. Whichever you pick "
        "below is completely fine by me."
    )

    choice = st.radio(
        "Your answer",
        [
            "Yes — let's be friends.",
            "Let's keep talking and see how it goes.",
            "I'd rather not, thanks.",
        ],
        index=None,
        label_visibility="collapsed",
    )

    if st.button("Send my answer"):
        if choice is None:
            st.warning("Pick one of the three first.")
        else:
            st.session_state.answer = choice

    answer = st.session_state.answer
    if answer is None:
        return

    rule()
    if answer.startswith("Yes"):
        st.balloons()
        st.success("Friendship accepted. Ichiraku is on me.")
        art(A.HEADBAND, "art-plain")
    elif answer.startswith("Let's keep"):
        st.info("That's the sensible answer, and it works for me.")
    else:
        st.write(
            "Understood, and thank you for saying so plainly. No hard feelings "
            "at all — take care, Shreya."
        )
        return

    interests = list(st.session_state.interests)
    if st.session_state.note_back.strip():
        interests.append(st.session_state.note_back.strip())

    scroll = "\n".join(
        [
            "FRIENDSHIP SCROLL - KONOHAGAKURE",
            "",
            f"Issued: {date.today().isoformat()}",
            f"Answer: {answer}",
            "Interests on record: " + (", ".join(interests) if interests else "to be discovered"),
            "What sparked the Japanese: "
            + (", ".join(st.session_state.spark) if st.session_state.spark
               else "still to be told properly"),
            "Chunin exam: "
            + (str(st.session_state.quiz_score) if st.session_state.quiz_score is not None
               else "not attempted"),
            "",
            "Terms: talk when you feel like it, ignore me when you don't,",
            "one bowl of ramen owed indefinitely.",
        ]
    )
    st.download_button(
        "Save the scroll",
        data=scroll,
        file_name="friendship-scroll.txt",
        mime="text/plain",
    )


PAGES = {
    "🍥 The summoning": page_home,
    "📜 The scroll": page_scroll,
    "🇯🇵 Japanese corner": page_japanese,
    "🥋 Chunin exam": page_exam,
    "🤝 The bond": page_bond,
}


# ------------------------------------------------------------------ sidebar
with st.sidebar:
    st.markdown(
        '<div style="font-family:Shippori Mincho,serif;font-size:1.5rem">木ノ葉隠れ</div>'
        '<div class="romaji">Konohagakure — hidden in the leaves</div>',
        unsafe_allow_html=True,
    )
    st.markdown('<hr class="rule">', unsafe_allow_html=True)
    page = st.radio("Sections", list(PAGES), label_visibility="collapsed")
    st.session_state.visited.add(page)

    st.markdown('<hr class="rule">', unsafe_allow_html=True)
    st.markdown("**Chakra gathered**")
    st.progress(len(st.session_state.visited) / len(PAGES))
    st.markdown(
        f'<p class="caption">{len(st.session_state.visited)} of {len(PAGES)} sections</p>',
        unsafe_allow_html=True,
    )
    art(A.rasengan(len(st.session_state.visited)), "art-mini")

PAGES[page]()

st.markdown('<hr class="rule">', unsafe_allow_html=True)
st.markdown(
    '<p class="caption">Made with Streamlit, a spiral of text, and reasonable hope. '
    "Naruto belongs to Masashi Kishimoto and Shueisha; this is a personal fan "
    "project, not affiliated with them.</p>",
    unsafe_allow_html=True,
)
