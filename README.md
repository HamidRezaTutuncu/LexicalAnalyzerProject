# Lexical Analyzer Project

**BLG306 – Biçimsel Diller ve Otomatlar** dersi dönem projesi.  
Kullanıcıdan alınan bir metnin geçerli bir değişken ismi (identifier) olup olmadığını kontrol eden basit bir **sözcüksel çözümleyici (lexical analyzer)**.

> **Ders Sorumlusu:** Dr. Öğr. Üyesi Somaiyeh Dehghan  
> **Öğrenci:** Hamidreza Toutounchi  
> **Üniversite:** İstanbul Rumeli Üniversitesi – Bilgisayar Mühendisliği

---

## 📌 Proje Amacı

Derleyici tasarımının ilk aşaması olan **lexical analysis** sürecini uygulamalı olarak göstermektir. Program, kullanıcının girdiği bir string'i karakter karakter inceleyerek belirli kurallara göre geçerli bir değişken ismi olup olmadığına karar verir.

---

## 📌 Geçerli Değişken Kuralları

Bir değişken adı:

- ✅ Harf ile başlamalıdır (`a-z` veya `A-Z`)
- ✅ Sadece harf, rakam ve alt çizgi (`_`) içerebilir
- ❌ Boşluk içeremez
- ❌ Özel karakter içeremez (`@`, `#`, `!`, `-` vb.)
- ❌ Anahtar kelime (keyword) olamaz (`int`, `for`, `while`, `class`, `def`, ...)

---

## 🛠️ Kullanılan Teknolojiler

- **Dil:** Python 3
- **GUI:** Tkinter (Python standart kütüphanesi)
- **Harici kütüphane:** YOK — tüm karakter kontrolleri (harf, rakam, alt çizgi, boşluk) elle yazılmıştır. `re` veya benzeri modüller kullanılmamıştır.

---

## 📂 Proje Yapısı

```
LexicalAnalyzerProject/
├── analyzer.py      # Sözcüksel çözümleme mantığı (LexicalAnalyzer sınıfı)
├── main.py          # Tkinter GUI (LexicalGui sınıfı)
└── README.md
```

### `analyzer.py`
Çekirdek mantık burada. `LexicalAnalyzer` sınıfı şu metodları içerir:

| Metod | Görevi |
|-------|--------|
| `is_letter(char)` | Karakter harf mi? |
| `is_digit(char)` | Karakter rakam mı? |
| `is_underscore(char)` | Karakter alt çizgi mi? |
| `is_space(char)` | Karakter boşluk mu? |
| `check_variable(s)` | Stringi kurallara göre denetler, `(bool, mesaj)` döner |

### `main.py`
Tkinter ile yazılmış basit ve şık bir arayüz. Kullanıcı bir değişken ismi girer, **ANALYZE** butonuna basar, sonuç pop-up olarak gösterilir.

---

## 🚀 Çalıştırma

```bash
python main.py
```

Ek bir kurulum gerekmiyor — Tkinter Python ile birlikte gelir.

---

## 🧪 Test Senaryoları

### ✅ Geçerli Örnekler

| Input | Sonuç |
|-------|-------|
| `x` | Geçerli bir değişken ismidir |
| `sayi` | Geçerli bir değişken ismidir |
| `toplam_deger` | Geçerli bir değişken ismidir |
| `kullanici1` | Geçerli bir değişken ismidir |
| `MyVariable` | Geçerli bir değişken ismidir |

### ❌ Geçersiz Örnekler

| Input | Hata Mesajı |
|-------|-------------|
| *(boş)* | Input boş olamaz |
| `1abc` | Değişken ismi harf ile başlamalıdır |
| `_test` | Değişken ismi harf ile başlamalıdır |
| `degisken adi` | Değişken ismi boşluk içeremez |
| `user@name` | `'@'` geçersiz bir karakterdir |
| `fiyat-tl` | `'-'` geçersiz bir karakterdir |
| `int` | `'int'` bir anahtar kelimedir, değişken olamaz |
| `for` | `'for'` bir anahtar kelimedir, değişken olamaz |
| `class` | `'class'` bir anahtar kelimedir, değişken olamaz |

---

## 📜 Lisans

Bu proje akademik bir ödev olarak hazırlanmıştır.
