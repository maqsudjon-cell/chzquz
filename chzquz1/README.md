# chiziq v2 — `/chzquz1`

Veb-studiya saytining **noldan yozilgan yangi dizayni**. Eski versiya (`/chzquz`) o'z joyida
tegilmagan holda qoladi — bu mustaqil, alohida sayt.

- **Manzil (bu repo ichida):** https://flarestamina.com/chzquz/chzquz1/
- **Mo'ljallangan manzil:** https://flarestamina.com/chzquz1/ — buning uchun quyidagi
  "Alohida manzilga chiqarish" bo'limiga qaraganda.

## Dizayn

x.ai uslubidagi **monoxrom, hairline-grid** tizim:

| Nima | Qanday |
|---|---|
| Rang | Faqat qora va oq. Aksent rang yo'q. Standart holat — qorong'i |
| Chiziqlar | Butun sahifa 1px `rgba(255,255,255,.08)` to'r ustida quriladi (`.mesh`, `.shell` relslari) |
| Shrift | Sarlavha va matn — Inter; raqam, yorliq va meta — JetBrains Mono |
| Burchak | Deyarli to'g'ri (`--r: 3px`) |
| Soya / gradient | Yo'q. Faqat chiziq va fon farqi |
| Animatsiya | Faqat scroll-reveal va hover — 0.2–0.7s, `cubic-bezier(.16,1,.3,1)` |
| Yorug' rejim | Bor (oq fon, qora matn) — bosh tugma orqali, `localStorage`da saqlanadi |

## Tuzilishi

```
index.html            butun sayt (HTML + CSS + JS bitta faylda)
404.html              xato sahifasi
favicon.svg/.ico      brend belgisi — monoxrom
site.webmanifest      PWA manifest
robots.txt sitemap.xml
assets/og.png/.jpg    ijtimoiy tarmoq rasmi 1200x630
assets/icon-*.png     favicon o'lchamlari
assets/shots/         real loyihalarning haqiqiy skrinshotlari (1400x875, faqat desktop)
tools/brand.py        favicon / ikonka / og.png generatori
```

## Nimani qayerdan o'zgartirish kerak

Hammasi `index.html` ichida:

| Nima | Qayerda |
|---|---|
| Ranglar, o'lchamlar | CSS boshidagi `:root` va `html[data-theme="light"]` |
| Xizmatlar | JS'dagi `var SVC=[...]` + `T` dagi `s1_*`…`s6_*` kalitlari |
| Loyihalar (portfolio) | JS'dagi `var WORKS=[...]` |
| Savol-javob | JS'dagi `var FAQ=[...]` |
| Narxlar | `#pricing` HTML'i + `T` dagi `pl*`, `ex*`, `mln` kalitlari |
| Tarjimalar | JS'dagi `var T={uz:{...},ru:{...},en:{...}}` |
| Telefon / Telegram / email | HTML'da `tel:`, `t.me/mrbmp13`, `mailto:` havolalari |

Yangi matn qo'shsangiz — uchala tilga ham qo'shing, aks holda til almashganda bo'sh qoladi.

## Alohida manzilga chiqarish (`flarestamina.com/chzquz1/`)

GitHub Pages'da yo'l repo nomidan kelib chiqadi, shuning uchun aynan `/chzquz1/` manzili
uchun `chzquz1` nomli alohida repo kerak:

1. GitHub'da `chzquz1` nomli yangi repo yarating.
2. Shu papkaning **ichidagi hamma narsani** repo ildiziga ko'chiring
   (`index.html` ildizda turishi kerak, `chzquz1/index.html` emas).
3. Settings → Pages → Source: `main` branch, `/ (root)`.
4. Hech qanday havolani o'zgartirish shart emas — sayt ichidagi barcha yo'llar nisbiy
   (`./`, `assets/...`), faqat SEO teglari allaqachon `/chzquz1/` ga qaratilgan.

## chzq.uz ga o'tkazish

1. Repo ildiziga `CNAME` fayli qo'shing, ichida bitta qator: `chzq.uz`
2. Domen registratorida DNS yozuvlari:
   - `A` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - yoki `CNAME` (www uchun) → `maqsudjon-cell.github.io`
3. GitHub → Settings → Pages → Custom domain: `chzq.uz` → Enforce HTTPS
4. `index.html` ichidagi `https://flarestamina.com/chzquz1/` manzillarini `https://chzq.uz/` ga
   almashtiring (canonical, og:url, og:image, twitter:image va JSON-LD), shuningdek
   `robots.txt` va `sitemap.xml` da.

## Brend fayllarini qayta yaratish

`favicon.ico`, `assets/icon-*.png` va `assets/og.png` kod bilan yaratilgan:

```bash
pip install pillow
CHZQ_FONTS=/shriftlar/papkasi python3 tools/brand.py
```

`CHZQ_FONTS` ichida `InstrumentSans-Bold.ttf` (sarlavha) va `JetBrainsMono-Regular.ttf`
(meta) bo'lishi kerak; boshqa shrift ishlatsangiz `tools/brand.py` boshidagi `SANS_B` /
`MONO_R` nomlarini o'zgartiring.

Belgining manbasi — `favicon.svg`: qora kvadrat, oq qiyshiq chiziq va pastda xira gorizontal
chiziq. Generator ham aynan shu 48×48 viewBox koordinatalaridan foydalanadi, shuning uchun
SVG'ni o'zgartirsangiz `tools/brand.py` dagi koordinatalarni ham moslang.
