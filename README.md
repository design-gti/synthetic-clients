# Synthetic Klien Talentlytica (TinyTroupe + Web UI)

Digital twin 3 persona klien Talentlytica, di-ground dari transkrip & meeting notes nyata.

| Persona | Perusahaan | Karakter singkat |
|---|---|---|
| **Bu Julia** | PT Matra Unikatama (migas) | Tegas, budget-conscious, pegang HR sendirian. Pain: kamus kompetensi, bukti procurement |
| **Sabila** | POMI | IDP & profiling internal. Antusias, banyak bertanya, cari aturan hitung sederhana |
| **Bu Siska** (Fransiska) | Raja Gadai | Rekrut ~100 orang/bulan, volume-first, data Excel belum dianalisis |

Setiap persona membawa transkrip meeting + notes lengkap sebagai ground truth (folder `personas/sources/`).

## Setup (sekali saja)
1. Salin `.env.example` jadi `.env`, isi `OPENAI_API_KEY`.
2. Virtualenv sudah ada di `.venv/` (TinyTroupe + Flask).

## Web UI — 3 chat room

```bash
.venv/bin/python app.py
```

Buka `http://localhost:8018` (tim satu WiFi: `http://<ip-laptop>:8018`). Tab atas untuk pindah room; tiap room punya thread dan sesi sendiri. Reply THINK/TALK/DONE tampil terpisah.

## Terminal

```bash
.venv/bin/python interview.py --persona sabila
.venv/bin/python test_konsep.py --persona fransiska "konsep yang mau diuji"
```

Default persona: julia. Hasil ke folder `output/`.

## Struktur
- `personas/` — registry + definisi per persona (`julia.py`, `sabila.py`, `fransiska.py`, helper `_base.py`)
- `personas/sources/` — transkrip & meeting notes asli (ground truth, ikut masuk prompt)
- `app.py`, `templates/index.html` — server & UI
- `config.ini` — model gpt-5-mini, cache aktif

## Catatan
- Directional insight, bukan pengganti validasi ke klien nyata.
- Transkrip penuh ikut di prompt → request pertama per sesi lebih berat (puluhan ribu token input). Cache aktif membantu.
- Transkrip ASR labelnya rusak; persona sudah diberi tahu soal ini.
