# chiziq — chzq.uz

Veb-studiya sayti. Statik, GitHub Pages'da turadi.

- **Sayt:** https://flarestamina.com/chzquz/ — v2, monoxrom dizayn
- **Eski versiya (arxiv):** https://flarestamina.com/chzquz/v1/ — o'zgarishsiz saqlanib turadi
- **Kelajakdagi manzil:** https://chzq.uz

## Tuzilishi

```
index.html            v2 — butun sayt (HTML + CSS + JS bitta faylda)
404.html              xato sahifasi
favicon.svg/.ico      brend belgisi — monoxrom
site.webmanifest      PWA manifest
robots.txt sitemap.xml
assets/og.png/.jpg    ijtimoiy tarmoq rasmi 1200x630
assets/icon-*.png     favicon o'lchamlari
assets/shots/         real loyihalarning haqiqiy skrinshotlari (1400x875)
tools/brand.py        favicon / ikonka / og.png generatori

v1/                   birinchi versiya — to'liq ishlaydigan arxiv nusxasi
                      (qidiruvda raqobat qilmasligi uchun noindex)
```

> Diqqat: sayt domenning ildizida emas, `/chzquz/` yo'lida turadi. Shuning uchun
> `robots.txt` ni qidiruv tizimlari o'qimaydi — u faqat `flarestamina.com/robots.txt`
> dan o'qiladi. Bu fayllar chzq.uz ga o'tgandan keyin kuchga kiradi.

## Dizayn (v2)

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

## Brend fayllarini qayta yaratish

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

## chzq.uz ga o'tkazish

1. Repo ildiziga `CNAME` fayli qo'shing, ichida bitta qator: `chzq.uz`
2. Domen registratorida DNS yozuvlari:
   - `A` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - yoki `CNAME` (www uchun) → `maqsudjon-cell.github.io`
3. GitHub → Settings → Pages → Custom domain: `chzq.uz` → Enforce HTTPS
4. `index.html` ichidagi `https://flarestamina.com/chzquz/` manzillarini `https://chzq.uz/` ga
   almashtiring (canonical, og:url, og:image, twitter:image va JSON-LD), shuningdek
   `robots.txt` va `sitemap.xml` da. `v1/index.html` da esa `/chzquz/v1/` → `/v1/`.
