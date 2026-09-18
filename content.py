"""
content.py
----------
All the words the app uses: the original message, Japanese study material,
quiz questions and the little ninja-way lines that rotate on the home page.
"""

# ---------------------------------------------------------------- the message
ORIGINAL_MESSAGE = """Hi Shreya,

How are you?

I thought of reaching out because you seem like a very interesting and nice
person, and would like to build a friendship with you.

What are your interests, and I'm curious to know what sparked your interest
in Japanese language and culture?"""


# ------------------------------------------------- ninja-way lines (original)
# Written for this app in the spirit of the series, not quoted from it.
NINJA_WAY = [
    "A bond starts with one person deciding to speak first.",
    "Strength is showing up again tomorrow.",
    "The long road is still the road.",
    "Nobody becomes anything alone.",
    "Say the honest thing, even when your voice shakes.",
    "Patience is a technique too.",
    "Learn a language and you inherit a way of seeing.",
    "A friend is someone who remembers your good days back to you.",
]


# ------------------------------------------------------------ Japanese corner
GREETINGS = [
    ("こんにちは", "konnichiwa", "Hello / good afternoon"),
    ("はじめまして", "hajimemashite", "Nice to meet you (first time)"),
    ("よろしくお願いします", "yoroshiku onegaishimasu", "Please treat me well — said when starting anything together"),
    ("お元気ですか", "ogenki desu ka", "How are you?"),
    ("ありがとう", "arigatou", "Thank you"),
    ("また明日", "mata ashita", "See you tomorrow"),
]

FRIENDSHIP_WORDS = [
    ("友達", "tomodachi", "Friend"),
    ("絆", "kizuna", "A bond between people"),
    ("仲間", "nakama", "Comrades — the people you belong with"),
    ("一期一会", "ichigo ichie", "One meeting, one chance — treat every encounter as unrepeatable"),
    ("木の葉", "konoha", "Leaf of a tree — the village Naruto comes from"),
    ("渦巻き", "uzumaki", "Spiral — also Naruto's family name"),
    ("忍道", "nindou", "Ninja way — the rule you refuse to break"),
    ("頑張って", "ganbatte", "Do your best / hang in there"),
]

# Katakana is the script used for foreign names.
NAME_IN_KATAKANA = [
    ("シュ", "shu"),
    ("レ", "re"),
    ("ヤ", "ya"),
]

KANA_QUIZ = [
    ("あ", "a"),
    ("き", "ki"),
    ("す", "su"),
    ("ね", "ne"),
    ("ほ", "ho"),
    ("ん", "n"),
]


# ------------------------------------------------------------- the chunin exam
QUIZ = [
    {
        "q": "Naruto's home village is Konohagakure. What does the name mean?",
        "options": ["Village hidden in the sand", "Village hidden in the leaves",
                    "Village hidden in the mist", "Village hidden in the clouds"],
        "answer": 1,
        "note": "隠れ (kakure) means hidden, 木の葉 (konoha) means leaf.",
    },
    {
        "q": "What is the Rasengan made of?",
        "options": ["Fire released through hand signs", "Spinning, concentrated chakra",
                    "Borrowed lightning", "Compressed wind from a fan"],
        "answer": 1,
        "note": "It needs no hand signs — just rotation, power and control.",
    },
    {
        "q": "Which title does the leader of Naruto's village hold?",
        "options": ["Kazekage", "Mizukage", "Hokage", "Raikage"],
        "answer": 2,
        "note": "影 (kage) means shadow, so a Kage is the shadow over the village.",
    },
    {
        "q": "Ichiraku is famous for serving what?",
        "options": ["Ramen", "Dango", "Takoyaki", "Onigiri"],
        "answer": 0,
        "note": "ラーメン — and Naruto's order is basically a personality trait.",
    },
    {
        "q": "The swirl on the back of Naruto's jacket is the crest of which clan?",
        "options": ["Uchiha", "Hyuga", "Nara", "Uzumaki"],
        "answer": 3,
        "note": "渦巻き (uzumaki) literally means spiral.",
    },
    {
        "q": "Kage Bunshin no Jutsu creates what?",
        "options": ["An illusion in the enemy's mind", "Solid copies of the caster",
                    "A wall of shadow", "A trade of places with an object"],
        "answer": 1,
        "note": "分身 (bunshin) = body split. They're real enough to fight.",
    },
]

RANKS = [
    (0, "Academy student", "Everyone starts here. Come back and try again."),
    (2, "Genin", "Solid. Team assignment pending."),
    (4, "Chunin", "You can lead a squad now."),
    (6, "Jonin", "Frankly, you could be teaching this."),
]


# --------------------------------------------------------------- the interests
INTEREST_CHIPS = [
    "Anime & manga", "Japanese language", "Books", "Music", "Films",
    "Art & drawing", "Photography", "Cooking", "Travel", "Hiking",
    "Gaming", "Coding", "Dance", "Fitness", "Coffee", "Tea",
    "Writing", "History", "Astronomy", "Cats", "Dogs", "Plants",
]

WHY_JAPANESE = [
    "An anime I couldn't stop watching",
    "The way the writing looks",
    "Music — city pop, J-rock, something else",
    "Food",
    "A trip I want to take",
    "It just sounded beautiful",
]
