"""Uji satu konsep produk ke synthetic persona dan ekstrak insight terstruktur.

Pakai:  .venv/bin/python test_konsep.py [--persona julia|sabila|fransiska] "deskripsi konsep"
Hasil ke output/konsep-<persona>-<timestamp>.json
"""
import os, sys, json, argparse, datetime, pathlib

from dotenv import load_dotenv
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    sys.exit("OPENAI_API_KEY belum di-set. Salin .env.example jadi .env lalu isi key-nya.")

from personas import PERSONAS
from tinytroupe.extraction import ResultsExtractor

KONSEP_DEFAULT = (
    "Talentlytica berencana menambah fitur 'Report Perpanjangan Otomatis': setiap bulan sistem "
    "mengirim email PDF berisi pemakaian token tahun berjalan vs tahun lalu, sisa kuota, rata-rata "
    "pemakaian per bulan, proporsi lulus vs tidak lulus, serta tanggal PO, tanggal approval, dan "
    "tanggal efektif masa aktif, siap dilampirkan ke procurement untuk audit perpanjangan."
)

ap = argparse.ArgumentParser()
ap.add_argument("--persona", choices=list(PERSONAS), default="julia")
ap.add_argument("konsep", nargs="?", default=KONSEP_DEFAULT)
args = ap.parse_args()

p = PERSONAS[args.persona]
agent = p["build"]()
nama = p["name"]

agent.listen_and_act(
    f"Tim produk Talentlytica: 'Kami mau minta pendapat soal rencana fitur ini: {args.konsep} "
    "Menurut Anda gimana? Apakah membantu pekerjaan Anda, apa yang kurang, dan apakah mau pakai?'"
)
agent.listen_and_act("Kalau boleh tahu, apa kekhawatiran terbesar Anda soal fitur ini, dan apa yang harus ada supaya benar-benar dipakai?")

extractor = ResultsExtractor()
hasil = extractor.extract_results_from_agent(
    agent,
    extraction_objective=(
        f"Rangkum reaksi {nama} terhadap konsep yang diuji: sentimen keseluruhan, "
        "alasan utama, kekhawatiran, syarat adopsi, dan fitur tambahan yang diminta."
    ),
    fields=["sentimen", "alasan", "kekhawatiran", "syarat_adopsi", "permintaan_tambahan"],
)

pathlib.Path("output").mkdir(exist_ok=True)
fname = f"output/konsep-{args.persona}-{datetime.datetime.now():%Y%m%d-%H%M%S}.json"
with open(fname, "w") as f:
    json.dump({"persona": args.persona, "konsep": args.konsep, "hasil": hasil}, f, ensure_ascii=False, indent=2)
print(f"\n=== Insight terstruktur ({nama}) ===\n{json.dumps(hasil, ensure_ascii=False, indent=2)}")
print(f"\nDisimpan ke {fname}")
