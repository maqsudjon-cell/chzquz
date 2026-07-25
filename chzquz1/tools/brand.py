#!/usr/bin/env python3
"""chiziq v2 — monoxrom brend fayllari (favicon, ikonkalar, og.png)."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Sarlavha uchun istalgan grotesk, meta uchun mono TTF yo'lini ko'rsating
FONTS = os.environ.get("CHZQ_FONTS", "/mnt/skills/examples/canvas-design/canvas-fonts")
SANS_B = os.path.join(FONTS, "InstrumentSans-Bold.ttf")
MONO_R = os.path.join(FONTS, "JetBrainsMono-Regular.ttf")

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

SS = 8  # supersampling


def mark(size, radius_ratio=10 / 48, bg=BLACK, pad=0.0):
    """48x48 viewBox'dagi belgini `size` px'da chizadi."""
    S = size * SS
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    inset = S * pad
    box = [inset, inset, S - inset, S - inset]
    r = (S - 2 * inset) * radius_ratio
    if r > 0:
        d.rounded_rectangle(box, radius=r, fill=bg)
    else:
        d.rectangle(box, fill=bg)

    # 48-birlik koordinatalarni ichki maydonga moslash
    inner = S - 2 * inset
    k = inner / 48.0
    def P(x, y):
        return (inset + x * k, inset + y * k)

    # pastdagi xira chiziq (2.4 qalinlik, dumaloq uchlar)
    lw = 2.4 * k
    d.line([P(6, 32.5), P(42, 32.5)], fill=(255, 255, 255, 77), width=int(round(lw)))
    for cx, cy in (P(6, 32.5), P(42, 32.5)):
        d.ellipse([cx - lw / 2, cy - lw / 2, cx + lw / 2, cy + lw / 2], fill=(255, 255, 255, 77))

    # asosiy oq qiyshiq chiziq
    d.polygon([P(12.5, 34.5), P(20.7, 34.5), P(37, 11.5), P(28.8, 11.5)], fill=WHITE)

    return im.resize((size, size), Image.LANCZOS)


def save(im, name):
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path)
    print("→", name, im.size)


# ---- favicon.ico ----
ico = mark(256)
ico.save(os.path.join(OUT, "favicon.ico"),
         sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
print("→ favicon.ico")

# ---- PNG ikonkalar ----
for s in (16, 32, 48, 180, 192, 512):
    save(mark(s), f"assets/icon-{s}.png")

# maskable: to'liq to'ldirilgan fon + kichikroq belgi (safe zone)
mask = Image.new("RGBA", (512, 512), BLACK)
inner = mark(512, radius_ratio=0, bg=(0, 0, 0, 0), pad=0.0)
inner = inner.resize((int(512 * 0.62), int(512 * 0.62)), Image.LANCZOS)
mask.paste(inner, ((512 - inner.width) // 2, (512 - inner.height) // 2), inner)
save(mask, "assets/icon-maskable-512.png")

# ---- og.png (1200x630) ----
W, H = 1200, 630
og = Image.new("RGB", (W, H), (0, 0, 0))
d = ImageDraw.Draw(og)

hair = (28, 28, 30)
# ramka + vertikal panjara (saytdagi hairline-grid kabi)
d.rectangle([64, 48, W - 64, H - 48], outline=hair, width=1)
for i in range(1, 6):
    x = 64 + (W - 128) * i / 6
    d.line([(x, 48), (x, H - 48)], fill=(18, 18, 20), width=1)

f_mark = mark(76)
og.paste(f_mark, (104, 92), f_mark)

f_mono = ImageFont.truetype(MONO_R, 21)
f_word = ImageFont.truetype(SANS_B, 128)
f_lead = ImageFont.truetype(SANS_B, 40)
f_meta = ImageFont.truetype(MONO_R, 22)

d.text((200, 118), "CHZQ.UZ", font=f_mono, fill=(150, 150, 155))
d.text((104, 214), "chiziq", font=f_word, fill=(255, 255, 255))
d.text((104, 396), "Biznesingiz uchun sayt.", font=f_lead, fill=(255, 255, 255))
d.text((104, 450), "1–3 kunda ishga tushadi.", font=f_lead, fill=(105, 105, 110))

d.line([(104, 512), (W - 104, 512)], fill=hair, width=1)
d.text((104, 534), "SAYT  ·  TELEGRAM BOT  ·  MINI APP", font=f_meta, fill=(150, 150, 155))
d.text((W - 104 - d.textlength("TOSHKENT", font=f_meta), 534), "TOSHKENT",
       font=f_meta, fill=(150, 150, 155))

og.save(os.path.join(OUT, "assets/og.png"), optimize=True)
print("→ assets/og.png", og.size)

og.convert("RGB").save(os.path.join(OUT, "assets/og.jpg"), quality=88, optimize=True)
print("→ assets/og.jpg")
