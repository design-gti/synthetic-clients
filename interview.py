"""Interview interaktif dengan synthetic persona klien.

Pakai:  .venv/bin/python interview.py [--persona julia|sabila|fransiska]
Ketik 'exit' untuk berhenti. Transkrip disimpan ke output/.
"""
import os, sys, argparse, datetime, pathlib

from dotenv import load_dotenv
load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    sys.exit("OPENAI_API_KEY belum di-set. Salin .env.example jadi .env lalu isi key-nya.")

from personas import PERSONAS

ap = argparse.ArgumentParser()
ap.add_argument("--persona", choices=list(PERSONAS), default="julia")
args = ap.parse_args()

p = PERSONAS[args.persona]
agent = p["build"]()
print(f"=== Interview dengan synthetic {p['name']} — {p['title']} (ketik 'exit' untuk selesai) ===\n")

asked = False
while True:
    try:
        q = input("Kamu> ").strip()
    except (EOFError, KeyboardInterrupt):
        break
    if not q or q.lower() in ("exit", "quit", "keluar"):
        break
    agent.listen_and_act(q)
    asked = True

if asked:
    pathlib.Path("output").mkdir(exist_ok=True)
    fname = f"output/interview-{args.persona}-{datetime.datetime.now():%Y%m%d-%H%M%S}.md"
    with open(fname, "w") as f:
        f.write(f"# Interview synthetic {p['name']}\n\n")
        f.write(agent.pretty_current_interactions(simplified=True))
    print(f"\nTranskrip disimpan ke {fname}")
