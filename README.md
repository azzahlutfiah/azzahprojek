# 🌸 Portofolio Azzah Lutfiyah — Python Flask

Website portofolio **Azzah Lutfiyah S.Kom.** berbasis **Python Flask** dengan desain premium.

---

## 📁 Struktur Proyek

```
azzah_portfolio/
├── app.py                  ← Main Flask application (semua data di sini)
├── requirements.txt        ← Dependensi Python
├── README.md
├── templates/
│   └── index.html          ← Template HTML Jinja2
└── static/
    ├── css/
    │   └── style.css       ← Styling lengkap
    └── js/
        └── main.js         ← Interaktivitas: cursor, typewriter, filter, dll
```

---

## 🚀 Cara Menjalankan

### 1. Install dependensi
```bash
pip install -r requirements.txt
```

### 2. Jalankan server
```bash
python app.py
```

### 3. Buka di browser
```
http://localhost:5000
```

---

## ✨ Fitur

| Fitur | Keterangan |
|-------|-----------|
| 🎯 Custom Cursor | Cursor animasi dengan lingkaran merah bata |
| ✍️ Typewriter | Animasi teks berganti otomatis |
| 📊 Skill Bars | Bar animasi saat scroll ke section |
| 🔢 Count-Up | Angka statistik animasi naik |
| 🔍 Filter Portfolio | Filter proyek berdasarkan kategori |
| 📱 Responsive | Tampil sempurna di mobile & desktop |
| 📨 Form Kontak | API POST /api/contact (Flask) |
| 🔄 Marquee Clients | Scroll otomatis nama klien |
| 🌊 Scroll Reveal | Elemen muncul saat discroll |
| ↑ Back to Top | Tombol kembali ke atas |

---

## 🎨 Teknologi

- **Backend**: Python 3.x + Flask
- **Template**: Jinja2 (HTML)
- **Styling**: CSS3 (tanpa framework eksternal)
- **Script**: Vanilla JavaScript
- **Font**: Playfair Display + Plus Jakarta Sans

---

## 📝 Kustomisasi

Edit bagian **DATA PORTOFOLIO** di `app.py`:

```python
PROFILE = { ... }      # Info pribadi
SKILLS  = [ ... ]      # Keahlian & persentase
PROJECTS = [ ... ]     # Daftar proyek
BLOGS   = [ ... ]      # Artikel blog
```

---

## 🌐 Deploy ke Hosting

### Heroku / Railway / Render:
```bash
# Tambahkan Procfile
echo "web: python app.py" > Procfile
```

### Vercel / Netlify (Serverless):
Gunakan `flask` + adapter serverless.

---

Dibuat dengan ❤️ oleh Azzah Lutfiyah | Python Flask
