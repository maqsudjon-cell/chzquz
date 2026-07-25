# chiziq — chzq.uz

Veb-studiya sayti. Statik, GitHub Pages'da turadi.

- **Sayt:** https://chzq.uz
- **Monoxrom variant (arxiv):** https://chzq.uz/v2/ — `noindex`
- **Eski manzil:** https://flarestamina.com/chzquz/ — chzq.uz ga yo'naltiriladi

## Tuzilishi

```
CNAME                 custom domen: chzq.uz
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

> Sayt `chzq.uz` domenining ildizida turadi, shuning uchun `robots.txt` va
> `sitemap.xml` qidiruv tizimlari tomonidan o'qiladi.

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

## Domen

`chzq.uz` ulangan: repo ildizidagi `CNAME` fayli orqali. DNS'da apex va `www`
uchun `A` yozuvlari GitHub Pages IP'lariga (`185.199.108–111.153`) ishora qiladi.

Domenni almashtirsangiz: `CNAME` faylini yangilang va `index.html` (canonical,
og:url, og:image, twitter:image, JSON-LD), `v2/index.html`, `robots.txt`,
`sitemap.xml` dagi manzillarni ham moslang.
