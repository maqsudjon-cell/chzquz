# chiziq — chzq.uz

Veb-studiya sayti. Statik, GitHub Pages'da turadi.

- **Sayt:** https://flarestamina.com/chzquz/
- **Monoxrom variant (arxiv):** https://flarestamina.com/chzquz/v2/ — `noindex`
- **Kelajakdagi manzil:** https://chzq.uz

## Tuzilishi

```
index.html            butun sayt (HTML + CSS + JS bitta faylda)
404.html              xato sahifasi
favicon.svg/.ico      brend belgisi — monoxrom
site.webmanifest      PWA manifest
robots.txt sitemap.xml
assets/og.png/.jpg    ijtimoiy tarmoq rasmi 1200x630
assets/icon-*.png     favicon o'lchamlari
assets/shots/         real loyihalarning haqiqiy skrinshotlari (1400x875)

v2/                   monoxrom variant — to'liq ishlaydigan arxiv nusxasi
                      o'z assets/ va tools/ papkalari bilan
                      (qidiruvda raqobat qilmasligi uchun noindex)
```

> Diqqat: sayt domenning ildizida emas, `/chzquz/` yo'lida turadi. Shuning uchun
> `robots.txt` ni qidiruv tizimlari o'qimaydi — u faqat `flarestamina.com/robots.txt`
> dan o'qiladi. Bu fayllar chzq.uz ga o'tgandan keyin kuchga kiradi.

## Dizayn

Yorug'/qorong'i mavzu, lime aksent (`#CFF54A`), Unbounded sarlavha + Inter matn.
Mavzu tugma orqali almashadi va `localStorage`da saqlanadi.

Marketing bo'limlari: hero (mokap + ishonch chiplari), xizmatlar, jonli ishlar,
nega biz, taqqoslash jadvali, jarayon, narxlar, kafolat, savol-javob, brif formasi.
FAQ uchun `FAQPage` structured data JS orqali hosil qilinadi.

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

Asosiy saytning brend fayllari qo'lda tayyorlangan. Monoxrom variantning
generatori `v2/tools/brand.py` da:

```bash
pip install pillow
CHZQ_FONTS=/shriftlar/papkasi python3 v2/tools/brand.py
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
   `robots.txt` va `sitemap.xml` da. `v2/index.html` da esa `/chzquz/v2/` → `/v2/`.
