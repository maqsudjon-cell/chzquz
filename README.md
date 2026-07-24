# chiziq — chzq.uz

Veb-studiya sayti. Bitta fayl (`index.html`), statik, GitHub Pages'da turadi.

- **Hozirgi manzil:** https://flarestamina.com/chzquz/
- **Kelajakdagi manzil:** https://chzq.uz

## Tuzilishi

```
index.html            butun sayt (HTML + CSS + JS bitta faylda)
404.html              xato sahifasi
favicon.svg/.ico      brend belgisi (kod bilan yaratilgan)
site.webmanifest      PWA manifest
robots.txt            sitemap.xml
assets/og.png         ijtimoiy tarmoq rasmi 1200x630 (kod bilan yaratilgan)
assets/icon-*.png     favicon o'lchamlari
assets/shots/         real loyihalarning haqiqiy skrinshotlari
build/                brend va skrinshot generatorlari (deploy qilinmaydi)
```

## Nimani qayerdan o'zgartirish kerak

Hammasi `index.html` ichida:

| Nima | Qayerda |
|---|---|
| Narxlar | `.ptable` bo'limi + `T.uz/ru/en` dagi `pl*`, `ex*`, `s*_` kalitlari |
| Loyihalar (portfolio) | JS'dagi `var WORKS=[...]` |
| Savol-javob | JS'dagi `var FAQ=[...]` |
| Tarjimalar | JS'dagi `var T={uz:{...},ru:{...},en:{...}}` |
| Telefon / Telegram / email | HTML'da `tel:`, `t.me/mrbmp13`, `mailto:` havolalari |

Yangi matn qo'shsangiz — uchala tilga ham qo'shing, aks holda til almashganda bo'sh qoladi.

## Brend fayllarini qayta yaratish

```bash
cd build
npm install
node brand.mjs      # favicon + og.png
node shoot.mjs      # portfolio skrinshotlari
```

Keyin PNG'larni siqish:

```bash
cd assets/shots
for f in *-desk.png; do magick "$f" -resize 1400x -quality 84 -strip "${f%.png}.jpg"; done
```

## chzq.uz ga o'tkazish

1. Repo ildiziga `CNAME` fayli qo'shing, ichida bitta qator: `chzq.uz`
2. Domen registratorida DNS yozuvlari:
   - `A` → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - yoki `CNAME` (www uchun) → `maqsudjon-cell.github.io`
3. GitHub → Settings → Pages → Custom domain: `chzq.uz` → Enforce HTTPS
4. `index.html` ichidagi `https://flarestamina.com/chzquz/` manzillarini `https://chzq.uz/` ga almashtiring
   (canonical, og:url, og:image, twitter:image), shuningdek `robots.txt` va `sitemap.xml` da.
