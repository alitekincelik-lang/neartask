# Sera Endüstriyel Reklam – İçerik Kütüphanesi

Ali Bey'in 13 Kasım 2026'ya kadar verdiği bilgiler, onayladığı kurallar ve onaylı içerikler. Tüm Sera paylaşım ve tasarım görevleri önce bu dosyayı okur. Yeni bilgi geldikçe buraya eklenir; eski bilgi silinmez, "(eski)" diye işaretlenir.

## 1. Kesin kurallar
- Paylaşım metinleri Türkçe; Ali Bey'e mesajlar Türkçe.
- Onay olmadan hiçbir şey paylaşılmaz. Onaylı dosyalar `social/sera/approved/YYYY-MM-DD.(jpg|mp4|txt)`.
- Onaylı Sera paylaşımı Sera'nın TÜM bağlı hesaplarına gider: Facebook "Sera Endüstriyel Reklam" (page 169637339733957, Zapier bağlantısı Sera Sosyal 02240b1d-2845-8482-b5b7-b55b1f1963c3) + Instagram "Sera Endüstriyel Reklam" (17841401002233810, Zapier Instagram bağlantısı info@serareklam.com.tr #3 02afb368-a03f-8e62-9d50-e0ce995f2abf). Her hesaba günde en fazla 1 gönderi; paylaşmadan önce tekrar kontrolü.
- SADECE gerçek fotoğraf/video (Drive "2 - Sera Reklam ve Derin Led" klasörleri). Yapay zekâ ile üretilmiş/değiştirilmiş görsel ASLA.
- Orijinal logo, şeffaf zemin, renkler değişmez; kırmızı kanatlar tek renge düşürülmez. Logo dosyaları: Drive "Logolar – Vektör (Tüm İşletmeler)/Sera Reklam" (açık zemin / koyu zemin, 4000px PNG + SVG).
- Ücretli hiçbir şey (boost, reklam) yapılmaz. Kişisel hesaplardan Ali Bey adına paylaşım yok.

## 2. Ana mesajlar (Ali Bey'in kelimeleri)
- "Fabrika" değil: **"Akyurt üretim tesislerimiz"**.
- Slogan: **"Tasarlıyor • Üretiyor • Uyguluyoruz"**. "1986'dan beri".
- Hizmet satırları (aynen bu sırayla):
  - TABELA • ATM KABİNİ • ANAHTAR TESLİM BANKA ŞUBESİ
  - MAĞAZA KONSEPTİ • KENT MOBİLYASI • AKARYAKIT İSTASYONLARI
  - PREFABRİK DEPREM YAŞAM SAHALARI
- İletişim: serareklam.com.tr · +90 312 847 50 60 · info@serareklam.com.tr · Akyurt / Ankara.
- Aile Artvinli: haritalı kapanışta Artvin'e daha büyük bir kamyon gider.

## 3. İmza ve hashtag
Metnin sonunda:
```
Sera Şirketler Grubu
Sera Reklamcılık Ltd. Şti. • Derin Led • Turtek İnşaat • Artwin Prefabrik • İskelem Otel • Artwin Dijital
```
Hashtag: önce konu hashtagleri, sonra `#SeraReklam #DerinLed #TurtekInşaat #ArtwinPrefabrik #İskelemOtel #ArtwinDijital`.

## 4. Tasarım şablonu (Ali Bey onaylı, 13 Kasım 2026)
- Post: 1080x1350. Üstte gerçek fotoğraf; aşağıya doğru kayarak krem zemine karışır (keskin sınır yok). Zemin: logo alanında açık krem, fotoğrafa doğru koyulaşan krem/kahve.
- Kırmızı "1986'DAN BERİ" rozeti başlığın ("AKYURT…") ilk harfiyle aynı hizada, hemen üstünde.
- Başlık beyaz "AKYURT ÜRETİM TESİSLERİMİZDE", altında kırmızı "TASARLIYOR • ÜRETİYOR • UYGULUYORUZ"; altında 3 hizmet satırı. Çizgi yok.
- Yazı karakteri: **Raleway** (5 seçenekten Ali Bey 5'i seçti).
- Footer (değişmez): solda Sera logosu (açık zemin), ortada orijinal renkli Facebook / Instagram / LinkedIn / YouTube ikonları, sağda serareklam.com.tr ve kırmızı telefon.
- Video: başta Sera logosu krem alanda küçükten büyüğe çoğalır (ilk karede de görünür), sonra yazılar belirir; fotoğraf hafifçe yaklaşır.
- Kapanış (tüm Sera tasarımlarında standart): krem zemin, "1986'DAN BERİ / AKYURT'TAN TÜRKİYE'NİN DÖRT BİR YANINA", kırmızı Türkiye haritası çizilir ve dolar, Akyurt'tan 12 büyük şehre (İstanbul, Bursa, İzmir, Antalya, Konya, Adana, Gaziantep, Diyarbakır, Van, Erzurum, Trabzon, Samsun) yavaş kamyonlar gider, en son büyük kamyon Artvin'e gider; logo animasyonla en alt sola yerleşir; son sayfa 3–4 sn durur.
- Müzik: Ali Bey Atabarı istiyor (sözsüz, kısık). Kendi ürettiğimiz "halk havası" taklidi kabul edilmedi. Telifsiz/kendi kaydı yoksa Ali Bey müziği telefonda kendisi ekleyebilir (14 Kasım videosunda öyle yaptı).
- Kaynaklar: `template/src/post.html` (post), `template/src/outro.html` (kapanış animasyonu, R(t) ile kare kare), `render.py`, `tr.json` + `cities.json` (harita, d3 Mercator 900x420), `template/logo_*.png`. Fontlar: @fontsource raleway.

## 5. Fotoğraf/video kütüphanesi (gerçek)
- Drive "Sera – Fabrika ve üretim" (1TWIwdb0vLTCoalWSt-xEZmudKmuekn7E): Akyurt drone (dji_fly_20230323…, kullanıldı → `photos/akyurt-tesis-drone-2023.jpg`), konteyner üretim holü (DJI_20230220…), CNC/alüminyum makine (IMG_20211104_1639xx, 2021, maskeli), metal atölye (IMG_2550), otomasyon hattı (IMG_2663), videolar IMG_2699–2709.MOV.
- Drive "Sera – Tabela, perakende ve stand", "Sera – Kent mobilyası ve büfe", "Sera – Bankacılık ve ATM", "Derin Led" – sonraki haftalık planda kullanılacak.

## 6. Onaylı paylaşımlar
| Tarih | İçerik | Dosya | Hesaplar |
|---|---|---|---|
| 14 Kas 2026 10:47 (Londra) | Akyurt üretim tesisleri – müzikli video (29 sn) | approved/2026-11-14.mp4 + .txt (+ .jpg kapak) | Facebook + Instagram (görev trig_01CiqSvxycngSKjQgkRZusYk) |
Daha önce: 10 Kasım Atatürk anma postu.

## 7. Sıradaki
- Haftalık Sera planı: Fabrika/üretim, Tabela ve mağaza, Kent mobilyası ve büfe, Bankacılık ve ATM (Ali Bey: "Tümü önümüzdeki haftalık planlamada geçerli olsun").
- Sera'nın LinkedIn / YouTube / TikTok hesapları otomatik sisteme bağlı değil.
