"""
Portofolio Azzah Lutfiyah - Flask Web Application
Web Developer & Content Creator
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ─── DATA PORTOFOLIO ───────────────────────────────────────────────────────────

PROFILE = {
    "name": "Azzah Lutfiyah, S.Kom., Gr.",
    "title": "Web Developer & Content Creator",
    "tagline": "Web programmer yang fokus pada performa, kualitas, dan keberlanjutan kode.",
    "motto": "Code. Build. Improve.",
    "email": "azzahlutfiyah8@gmail.com",
    "address": "Jl. Sambeng Kulon, Kembaran, Banyumas",
    "photo": "https://myazzahlutfiah.netlify.app/dist/img/Azzah.png",
    "social": {
        "youtube":   "https://www.youtube.com/@azzahlutfiyah",
        "instagram": "https://instagram.com/alfinita__",
        "threads":   "https://threads.com/alfinita__",
        "tiktok":    "https://tiktok.com/@myloopy___",
        "linkedin":  "https://linkedin.com/in/azzahlutfiyah99/",
    }
}

SKILLS = [
    {"name": "Python",        "level": 85, "color": "#3b82f6"},
    {"name": "JavaScript",    "level": 90, "color": "#f59e0b"},
    {"name": "HTML & CSS",    "level": 95, "color": "#ec4899"},
    {"name": "PHP / Laravel", "level": 80, "color": "#8b5cf6"},
    {"name": "React.js",      "level": 75, "color": "#06b6d4"},
    {"name": "MySQL",         "level": 82, "color": "#10b981"},
]

PROJECTS = [
    {
        "id": 1,
        "title": "Aplikasi Surat Menyurat",
        "category": "Web App",
        "tag": "Laravel",
        "desc": "Platform digital untuk mempermudah pengelolaan surat masuk dan surat keluar secara efektif, cepat, dan terorganisir.",
        "url": "https://smpump.sch.id/suratku",
        "image": "https://myazzahlutfiah.netlify.app/dist/img/portfolio/surat.png",
        "tech": ["Laravel", "MySQL", "Bootstrap"],
        "color": "#3b82f6",
    },
    {
        "id": 2,
        "title": "Website SMP UMP",
        "category": "Company Profile",
        "tag": "Web",
        "desc": "Menyajikan informasi lengkap seputar profil sekolah, kegiatan akademik & non-akademik, pengumuman, dan layanan pendidikan digital.",
        "url": "https://smpump.sch.id",
        "image": "https://myazzahlutfiah.netlify.app/dist/img/portfolio/smpump.jpeg",
        "tech": ["HTML", "CSS", "JavaScript", "PHP"],
        "color": "#10b981",
    },
    {
        "id": 3,
        "title": "Nova Library",
        "category": "Web App",
        "tag": "Fullstack",
        "desc": "Aplikasi Perpustakaan digital dan fisik SMP UMP sebagai pusat sumber belajar bagi siswa, guru, dan civitas sekolah.",
        "url": "https://smpump.sch.id/novalibrary",
        "image": "https://myazzahlutfiah.netlify.app/dist/img/portfolio/novalibrary.jpeg",
        "tech": ["Laravel", "MySQL", "Tailwind"],
        "color": "#8b5cf6",
    },
    {
        "id": 4,
        "title": "Flappy Bird Game",
        "category": "Game",
        "tag": "JavaScript",
        "desc": "Game klasik Flappy Bird — pemain mengendalikan burung melewati pipa-pipa hijau menggunakan JavaScript murni.",
        "url": "https://gameazzah.netlify.app/",
        "image": "https://myazzahlutfiah.netlify.app/dist/img/portfolio/flappybird.png",
        "tech": ["JavaScript", "Canvas API", "HTML5"],
        "color": "#f59e0b",
    },
    {
        "id": 5,
        "title": "Jurnal Mengajar Guru",
        "category": "Web App",
        "tag": "Fullstack",
        "desc": "Sistem digital untuk mencatat dan memantau kegiatan pembelajaran guru secara terstruktur dan terintegrasi.",
        "url": "#",
        "image": "https://myazzahlutfiah.netlify.app/dist/img/portfolio/jurnalmengajar.png",
        "tech": ["PHP", "MySQL", "Bootstrap"],
        "color": "#ec4899",
    },
    {
        "id": 6,
        "title": "E-Learning SMP UMP",
        "category": "Platform",
        "tag": "LMS",
        "desc": "Platform pembelajaran digital untuk mendukung proses belajar mengajar secara daring maupun blended learning.",
        "url": "#",
        "image": "https://myazzahlutfiah.netlify.app/dist/img/portfolio/elearning.png",
        "tech": ["Laravel", "Vue.js", "MySQL"],
        "color": "#06b6d4",
    },
    {
        "id": 7,
        "title": "Company Profile Bit Indonesia",
        "category": "Company Profile",
        "tag": "Web",
        "desc": "Website perusahaan PT BIT Indonesia yang bergerak di bidang pengelolaan dan budidaya tumbuhan berbasis teknologi.",
        "url": "#",
        "image": "https://myazzahlutfiah.netlify.app/dist/img/portfolio/Bit.png",
        "tech": ["HTML", "CSS", "JavaScript"],
        "color": "#10b981",
    },
    {
        "id": 8,
        "title": "Aplikasi Chat Multiplatform",
        "category": "Web App",
        "tag": "Realtime",
        "desc": "Platform komunikasi digital untuk menghubungkan anggota komunitas dalam satu ruang yang aman, cepat, dan mudah digunakan.",
        "url": "https://skripsi-chat-app.netlify.app/",
        "image": "https://myazzahlutfiah.netlify.app/dist/img/portfolio/chat.png",
        "tech": ["React", "Firebase", "Node.js"],
        "color": "#8b5cf6",
    },
]

BLOGS = [
    {
        "title": "Transformasi Digital: Peran Teknologi dalam Membentuk Masa Depan",
        "excerpt": "Era digital membawa dampak transformasional dalam setiap aspek kehidupan kita.",
        "url": "https://azzahlutfiah.blogspot.com/2024/01/transformasi-digital-peran-teknologi.html",
        "date": "Januari 2024",
        "tag": "Teknologi",
    },
    {
        "title": "Multimedia dalam Pembelajaran: Meningkatkan Pengalaman Siswa",
        "excerpt": "Teknologi multimedia tidak hanya memperkaya pengalaman belajar, tetapi juga meningkatkan pemahaman siswa.",
        "url": "https://azzahlutfiah.blogspot.com/2024/01/multimedia-dalam-pembelajaran.html",
        "date": "Januari 2024",
        "tag": "Pendidikan",
    },
    {
        "title": "Masa Depan Teknologi: Antisipasi Perubahan yang Akan Datang",
        "excerpt": "Teknologi terus mengalami kemajuan pesat, membawa inovasi dan transformasi yang luar biasa.",
        "url": "https://azzahlutfiah.blogspot.com/2024/01/masa-depan-teknologi-antisipasi.html",
        "date": "Januari 2024",
        "tag": "Future Tech",
    },
    {
        "title": "Cara Siswa agar Paham Teknologi",
        "excerpt": "Strategi dan pendekatan yang dapat diadopsi oleh pendidik dan siswa untuk memahami teknologi.",
        "url": "https://azzahlutfiah.blogspot.com/2024/01/cara-siswa-agar-paham-teknologi.html",
        "date": "Januari 2024",
        "tag": "Pendidikan",
    },
]

CLIENTS = ["Google", "Gojek", "Tokopedia", "Traveloka"]

STATS = [
    {"label": "Proyek Selesai", "value": "8+",   "icon": "💼"},
    {"label": "Tahun Pengalaman","value": "3+",   "icon": "⭐"},
    {"label": "Klien Puas",     "value": "10+",  "icon": "🤝"},
    {"label": "Blog Artikel",   "value": "20+",  "icon": "✍️"},
]

# ─── ROUTES ──────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        projects=PROJECTS,
        blogs=BLOGS,
        clients=CLIENTS,
        stats=STATS,
        year=datetime.now().year,
    )

@app.route("/api/contact", methods=["POST"])
def contact():
    """Endpoint untuk form kontak (demo)"""
    data = request.get_json()
    name    = data.get("name", "").strip()
    email   = data.get("email", "").strip()
    message = data.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({"success": False, "msg": "Semua field wajib diisi!"}), 400

    # Di production: kirim email dengan smtplib atau SendGrid
    print(f"[KONTAK] {name} <{email}>: {message}")
    return jsonify({"success": True, "msg": f"Terima kasih {name}! Pesan Anda telah diterima."})

@app.route("/api/projects")
def api_projects():
    return jsonify(PROJECTS)

# ─── MAIN ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
