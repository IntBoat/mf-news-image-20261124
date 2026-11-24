"""Draw the 24 November 2026 world-news poster (1024x1024 PNG).

Stories are the day's top reported events, each with a short headline
and a one-line label. All text is drawn with PIL from strings below.
"""
from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
BOLD = FONT_DIR + "DejaVuSans-Bold.ttf"
REG = FONT_DIR + "DejaVuSans.ttf"

W, H = 1024, 1024
BG = (247, 243, 234)
NAVY = (20, 33, 61)
GOLD = (201, 162, 39)
INK = (24, 24, 24)
MUTED = (90, 90, 90)
WHITE = (255, 255, 255)

STORIES = [
    ("MIDDLE EAST", (150, 40, 40),
     "Three oil tankers catch fire in Strait of Hormuz",
     "Iran's Revolutionary Guards blame naval mines for the blasts."),
    ("SPACE", (30, 80, 160),
     "Allies warn of Russian nuclear space weapon",
     "NATO vows space defence after reports of a launch within weeks."),
    ("KOREA", (160, 90, 20),
     "Russian aircraft enters South Korean airspace",
     "Evacuation warning briefly issued for Ulleung island."),
    ("TECH", (30, 80, 160),
     "US states sue Musk firms over Grok images",
     "Lawsuits allege the chatbot made sexualised images of people."),
    ("UKRAINE WAR", (150, 40, 40),
     "Russian death toll in Ukraine put near 500,000",
     "New hacked data underpins the estimate, reports say."),
    ("AI", (31, 120, 90),
     "UN chief urges AI risk rules within a year",
     "Call for a global framework to manage artificial intelligence."),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 190], fill=NAVY)
    d.rectangle([0, 190, W, 198], fill=GOLD)
    f_small = font(BOLD, 26)
    f_date = font(BOLD, 66)
    f_sub = font(REG, 25)
    d.text((512, 34), "THE WORLD IN ONE DAY", font=f_small,
           fill=GOLD, anchor="ma")
    d.text((512, 66), "24 NOVEMBER 2026", font=f_date,
           fill=WHITE, anchor="ma")
    d.text((512, 148), "TUESDAY  -  THE DAY'S NEWS IN ONE IMAGE",
           font=f_sub, fill=(200, 205, 220), anchor="ma")

    # Story blocks
    f_tag = font(BOLD, 21)
    f_head = font(BOLD, 30)
    f_label = font(REG, 24)
    y = 214
    block_h, gap = 116, 8
    for tag, colour, head, label in STORIES:
        d.rectangle([40, y, W - 40, y + block_h], fill=WHITE)
        d.rectangle([40, y, 52, y + block_h], fill=colour)
        d.text((72, y + 12), tag, font=f_tag, fill=colour)
        lines = wrap(d, head, f_head, W - 140)
        hy = y + 40
        for ln in lines[:2]:
            d.text((72, hy), ln, font=f_head, fill=INK)
            hy += 34
        d.text((72, y + block_h - 32), label, font=f_label, fill=MUTED)
        y += block_h + gap

    # Footer
    f_foot = font(REG, 21)
    d.text((512, 986), "All stories as reported on 24 November 2026.",
           font=f_foot, fill=MUTED, anchor="ma")

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
