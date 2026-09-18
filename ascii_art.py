"""
ascii_art.py
------------
Every picture in this app is drawn with nothing but text.

IMPORTANT RULE FOR THIS FILE: only plain 7-bit ASCII (space through ~).
Block characters, box-drawing characters and kanji are NOT reliably the same
width as ASCII in browser monospace fonts, which is what makes text art shear
apart. Staying inside ASCII guarantees every character occupies exactly one
cell, so the art lines up everywhere.

The centrepiece (the Uzumaki swirl) is generated, not hard-coded: it walks an
Archimedean spiral and stamps Naruto keywords along the path, so the shape is
literally made out of words.
"""

import math

# The words the big swirl is woven from.
KEYWORD_STRING = (
    "NARUTO UZUMAKI KONOHA RASENGAN HOKAGE ICHIRAKU RAMEN SHINOBI KURAMA "
    "SASUKE SAKURA KAKASHI JIRAIYA HINATA SHIKAMARU CHAKRA SHARINGAN "
    "BYAKUGAN DATTEBAYO NINDO SANNIN GENIN CHUNIN JONIN KAGEBUNSHIN "
    "SENNIN AKATSUKI TAIJUTSU NINJUTSU GENJUTSU KUNAI SHURIKEN KIZUNA "
    "TOMODACHI NAKAMA WILLOFFIRE NEVERGIVEUP BELIEVEIT "
)

# Characters are about twice as tall as they are wide, so horizontal
# distances get multiplied by this to keep circles looking like circles.
CHAR_ASPECT = 0.5


# ----------------------------------------------------------- block lettering
# A 7-row, 7-column ASCII font. Building words from these guarantees the
# letters stay in step with each other, instead of counting spaces by hand.
GLYPH_ROWS = 7

GLYPHS = {
    "A": ["  ###  ",
          " ## ## ",
          "##   ##",
          "##   ##",
          "#######",
          "##   ##",
          "##   ##"],
    "E": ["#######",
          "##     ",
          "##     ",
          "#####  ",
          "##     ",
          "##     ",
          "#######"],
    "H": ["##   ##",
          "##   ##",
          "##   ##",
          "#######",
          "##   ##",
          "##   ##",
          "##   ##"],
    "N": ["##   ##",
          "###  ##",
          "#### ##",
          "## ####",
          "##  ###",
          "##   ##",
          "##   ##"],
    "O": [" ##### ",
          "##   ##",
          "##   ##",
          "##   ##",
          "##   ##",
          "##   ##",
          " ##### "],
    "R": ["###### ",
          "##   ##",
          "##   ##",
          "###### ",
          "##  ## ",
          "##   ##",
          "##   ##"],
    "S": [" ##### ",
          "##   ##",
          "##     ",
          " ##### ",
          "     ##",
          "##   ##",
          " ##### "],
    "T": ["#######",
          "  ###  ",
          "  ###  ",
          "  ###  ",
          "  ###  ",
          "  ###  ",
          "  ###  "],
    "U": ["##   ##",
          "##   ##",
          "##   ##",
          "##   ##",
          "##   ##",
          "##   ##",
          " ##### "],
    "Y": ["##   ##",
          "##   ##",
          " ## ## ",
          "  ###  ",
          "  ###  ",
          "  ###  ",
          "  ###  "],
    " ": ["       "] * GLYPH_ROWS,
}


def block_text(word, gap=1):
    """Render a word in the 7-row ASCII font. Unknown letters become blanks."""
    spacer = " " * gap
    return "\n".join(
        spacer.join(GLYPHS.get(ch.upper(), GLYPHS[" "])[r] for ch in word)
        for r in range(GLYPH_ROWS)
    )


LOGO = block_text("NARUTO")
SHREYA = block_text("SHREYA")


# ------------------------------------------------------------- the big swirl
def _blank(width, height):
    return [[" "] * width for _ in range(height)]


def _stamp(grid, col, row, ch):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        grid[row][col] = ch


def uzumaki_swirl(width=90, height=40, turns=2.25, tail=True):
    """Draw the Uzumaki / Konoha swirl out of keyword letters.

    Returns one string of ASCII, ready to drop inside a <pre> block.
    """
    grid = _blank(width, height)
    # The swirl sits up and to the right so the leaf tail has room to sweep
    # away towards the bottom-left corner.
    cx, cy = width * 0.58, height * 0.44

    # Largest radius that still fits the canvas in every direction.
    max_r = min(cx * CHAR_ASPECT, (width - cx) * CHAR_ASPECT, cy, height - cy) - 1.0
    t_end = 2 * math.pi * turns
    a = max_r / t_end

    letters = list(KEYWORD_STRING.replace(" ", "."))
    state = {"i": 0, "last": None}

    def plot(x, y):
        """x, y are in aspect-corrected space; convert back to grid cells."""
        col = int(round(cx + x / CHAR_ASPECT))
        row = int(round(cy + y))
        if state["last"] == (col, row):
            return
        state["last"] = (col, row)
        i = state["i"]
        # Two cells wide so the stroke reads evenly at this aspect ratio.
        _stamp(grid, col, row, letters[i % len(letters)])
        _stamp(grid, col + 1, row, letters[(i + 1) % len(letters)])
        state["i"] = i + 2

    # Step along the curve by arc length so the stroke never breaks up,
    # however far from the centre it gets.
    step = 0.35
    t = 0.0
    while t <= t_end:
        r = a * t
        plot(r * math.cos(t), r * math.sin(t))
        t += step / max(a * math.sqrt(1 + t * t), 1e-6)

    # The leaf tail hooking off the outer end.
    if tail:
        ex, ey = max_r * math.cos(t_end), max_r * math.sin(t_end)
        p0 = (ex, ey)
        p1 = (ex - max_r * 0.55, ey + max_r * 0.25)
        p2 = (ex - max_r * 1.45, ey - max_r * 0.15)
        for i in range(4001):
            t = i / 4000
            u = 1 - t
            plot(
                u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1],
            )

    lines = ["".join(row).rstrip() for row in grid]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)


# ------------------------------------------------------------- hand-drawn art
FACE = r"""
       \\       \\       ||       //       //
        \\       \\      ||      //       //
    _______________________________________________
   |                                               |
   | ####  ####  ####  ( @ )  ####  ####  ####     |
   |_______________________________________________|
      |                                          |
      |     __________          __________       |
      |    /          \        /          \      |
      |   |    (o)     |      |     (o)    |     |
      |    \__________/        \__________/      |
   ___|                                          |___
  /   |    ===  ===                   ===  ===   |   \
 |  o |    ===  ===          /\       ===  ===   | o  |
 |    |    ===  ===          \/       ===  ===   |    |
  \___|                                          |___/
      |                                          |
      |             \                  /         |
      |              \________________/          |
       \                                        /
        \______________________________________/
"""

RAMEN = r"""
        ~     ~      ~     ~
         ~      ~      ~
    _________________________________
    \    ~~~~   ####   ~~~~   ####  /
     \    ####   ~~~~   ####   ~~~ /
      \_____________________________/
        \_________________________/
          \_____________________/
"""

HEADBAND = r"""
   ==============================================
   ||||||||||||||||||  ( @ )  ||||||||||||||||||
   ==============================================
"""


def rasengan(frame=0):
    """A small spinning orb of chakra. Pass an increasing frame number."""
    pairs = [("\\", "/"), ("|", "|"), ("/", "\\"), ("-", "-")]
    left, right = pairs[frame % 4]
    return "\n".join(
        [
            "     .   *   .",
            "   *   " + left + " | " + right + "   *",
            "  .  - ( @ ) -  .",
            "   *   " + right + " | " + left + "   *",
            "     .   *   .",
        ]
    )


def keyword_banner(words, width=64):
    """Wrap a list of words into a neat centred block of text."""
    lines, line = [], ""
    for w in words:
        candidate = (line + " . " + w) if line else w
        if len(candidate) > width:
            lines.append(line.center(width))
            line = w
        else:
            line = candidate
    if line:
        lines.append(line.center(width))
    return "\n".join(lines)


def is_pure_ascii(text):
    """Guard against anyone pasting in a character that breaks alignment."""
    return all(c == "\n" or 32 <= ord(c) <= 126 for c in text)


ALL_ART = {
    "LOGO": LOGO,
    "SHREYA": SHREYA,
    "FACE": FACE,
    "RAMEN": RAMEN,
    "HEADBAND": HEADBAND,
}


if __name__ == "__main__":
    pieces = dict(ALL_ART)
    pieces["SWIRL"] = uzumaki_swirl()
    pieces["RASENGAN"] = rasengan(1)
    for name, piece in pieces.items():
        assert is_pure_ascii(piece), f"{name} contains a non-ASCII character"
        widest = max(len(line) for line in piece.split("\n"))
        print(f"--- {name}  (widest line: {widest} chars)")
        print(piece)
