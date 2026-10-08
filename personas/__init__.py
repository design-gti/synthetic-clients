"""Registry persona klien Talentlytica."""
from . import julia, sabila, fransiska

PERSONAS = {
    "julia": {
        "build": julia.build,
        "name": "Bu Julia",
        "title": "Manager HR · PT Matra Unikatama",
        "company": "PT Matra Unikatama",
        "initial": "BJ",
        "color": "#0b6e75",
        "desc": "Jasa migas. Tegas, budget-conscious, pegang HR sendirian. Pain: kamus kompetensi & bukti untuk procurement.",
        "profile_rows": [
            {"icon": "🏢", "text": "PT Matra Unikatama — jasa migas (mud engineering, lab, HSE, logistik)"},
            {"icon": "👤", "text": "Manager HR generalis — pegang seluruh fungsi HR + 2 staf"},
            {"icon": "📋", "text": "Pakai Talentlytica Persona untuk rekrutmen (mandatori). Sisa 64 token; PO sudah expired."},
            {"icon": "🔑", "text": "Atasan: Direktur HR/IT berlatar GA — keputusan assessment jatuh ke Bu Julia"},
        ],
        "pain_points": [
            "Kamus kompetensi teknis tidak mau dibagikan user teknis",
            "Sulit justify perpanjangan ke procurement tanpa laporan pemakaian",
            "Tidak bisa jelaskan ke user KENAPA kandidat gagal — hanya angka",
            "Career path belum bisa dibuat (jabatan belum terstandar)",
        ],
        "suggestions": [
            "Kalau kami tambah report perpanjangan otomatis, membantu nggak Bu?",
            "Apa pain point terbesar Ibu soal standar kompetensi teknis?",
            "Reaksi Ibu kalau Kelola ditawarkan mulai 25 juta per tahun?",
            "Gimana proses Ibu justify perpanjangan ke procurement?",
            "Fitur apa yang paling Ibu butuhkan dari Talentlytica tahun depan?",
        ],
    },
    "sabila": {
        "build": sabila.build,
        "name": "Sabila",
        "title": "HR · POMI",
        "company": "POMI",
        "initial": "SA",
        "color": "#7c4dbe",
        "desc": "Fokus IDP & profiling internal. Antusias, banyak bertanya, cari aturan hitung sederhana. Keputusan akhir di atasan.",
        "profile_rows": [
            {"icon": "🏢", "text": "POMI — HR fokus IDP & profiling (rekrutmen eksternal sudah jarang)"},
            {"icon": "👤", "text": "Kontak utama Talentlytica di POMI; keputusan akhir di Pak Rohman & Pak Hardy"},
            {"icon": "📋", "text": "Pakai Persona & Q-Test sebagai supporting data IDP; trial Kelola setahun lalu"},
            {"icon": "🗓️", "text": "Sedang prepare IDP sebelum akhir tahun; 44 posisi tanpa suksesor siap"},
        ],
        "pain_points": [
            "Hasil Persona deskriptif — sulit bedakan orang satu dengan lainnya",
            "Bingung baca Q-Test tanpa aturan hitung yang jelas",
            "Suksesi: banyak posisi 1 kandidat saja, leveling belum matang",
            "Peluang lintas departemen belum terpetakan",
        ],
        "suggestions": [
            "Mbak Sabila, gimana progress persiapan IDP-nya?",
            "Kalau hasil Persona kami kelompokkan otomatis jadi high-middle-low, membantu?",
            "Apa yang bikin bingung waktu baca laporan Q-Test kemarin?",
            "Kalau kami buatkan daftar key position yang urgent, formatnya mau seperti apa?",
            "Apa yang perlu kami siapkan supaya Pak Rohman yakin di demo berikutnya?",
        ],
    },
    "fransiska": {
        "build": fransiska.build,
        "name": "Bu Siska",
        "title": "Pimpinan HR · Raja Gadai",
        "company": "Raja Gadai",
        "initial": "FS",
        "color": "#b05c1a",
        "desc": "Rekrut ~100 orang/bulan di kota kecil. Pragmatis, volume-first, data masih Excel dan belum dianalisis.",
        "profile_rows": [
            {"icon": "🏢", "text": "Raja Gadai — gadai segmen menengah ke bawah, ekspansi kota kecil & kabupaten"},
            {"icon": "👤", "text": "Pimpinan HR Level 7 — lapor langsung ke owner (Level 8)"},
            {"icon": "📋", "text": "Pakai psikotes Talentlytica 13 aspek ~2 tahun; belum di-adjust dari default"},
            {"icon": "📊", "text": "Data potensi-performa-kompetensi ada di Excel, belum pernah dianalisis"},
        ],
        "pain_points": [
            "Kandidat tipis: kalah banding pinjol, lokasi jauh, gaji di bawah UMR",
            "~100 posisi/bulan harus terisi — standar IQ terpaksa diturunkan (90→75)",
            "SOP dipahami tapi tidak dijalankan: dari 10 SOP bisa 1 terlewat",
            "Data banyak tapi belum pernah dianalisis — tidak tahu caranya",
        ],
        "suggestions": [
            "Bu Siska, gimana kondisi rekrutmen bulan ini?",
            "Kalau data Excel Ibu kami analisis dan visualisasikan, mau mulai dari data apa?",
            "Standar IQ 90 yang sering ditoleransi itu, mau kami bantu validasi dengan data performa?",
            "Apa yang paling sering bikin SOP terlewat di cabang menurut Ibu?",
            "Soal quotation perpanjangan, apa yang Ibu tunggu dari kami?",
        ],
    },
}
