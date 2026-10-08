"""
Web server multi-persona: chat dengan synthetic klien Talentlytica (TinyTroupe).

Jalankan: .venv/bin/python app.py
Akses lokal: http://localhost:8018
Akses teman (satu WiFi): http://<ip-laptopmu>:8018
"""
import os
import json
import time
import threading
import uuid
from dotenv import load_dotenv

load_dotenv()
if not os.getenv("OPENAI_API_KEY"):
    raise SystemExit("OPENAI_API_KEY belum di-set. Salin .env.example jadi .env lalu isi key-nya.")

from flask import Flask, request, jsonify, render_template, Response, stream_with_context

app = Flask(__name__)

from personas import PERSONAS  # noqa: E402

# Dict {f"{persona_id}:{session_id}": {"agent": TinyPerson, "lock": Lock}}
sessions: dict = {}
sessions_lock = threading.Lock()


def get_or_create_session(persona_id: str, session_id: str):
    key = f"{persona_id}:{session_id}"
    with sessions_lock:
        if key not in sessions:
            sessions[key] = {
                "agent": PERSONAS[persona_id]["build"](),
                "lock": threading.Lock(),
            }
        return sessions[key]


def sse_event(data: dict) -> str:
    return f"data: {json.dumps(data, ensure_ascii=False)}\n\n"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/personas")
def personas_list():
    return jsonify([
        {
            "id": pid,
            "name": p["name"],
            "title": p["title"],
            "company": p.get("company", ""),
            "initial": p["initial"],
            "color": p["color"],
            "desc": p["desc"],
            "suggestions": p["suggestions"],
            "profile_rows": p.get("profile_rows", []),
            "pain_points": p.get("pain_points", []),
        }
        for pid, p in PERSONAS.items()
    ])


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    persona_id = data.get("persona_id", "julia")
    if persona_id not in PERSONAS:
        return jsonify({"error": f"Persona '{persona_id}' tidak dikenal"}), 400
    session_id = data.get("session_id") or str(uuid.uuid4())
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "Pesan kosong"}), 400

    session = get_or_create_session(persona_id, session_id)

    def generate():
        with session["lock"]:
            agent = session["agent"]
            agent.listen_and_act(message)
            actions = agent.pop_latest_actions()

        if not actions:
            yield sse_event({"type": "error", "content": "Tidak ada respons dari agent."})
            return

        has_talk = False
        for action in actions:
            atype = action.get("type", "")
            content = (action.get("content") or "").strip()

            if atype == "THINK" and content:
                yield sse_event({"type": "THINK", "content": content})
                time.sleep(0.15)
            elif atype == "TALK" and content:
                has_talk = True
                yield sse_event({"type": "TALK", "content": content})
                time.sleep(0.1)
            elif atype == "DONE":
                yield sse_event({"type": "DONE", "content": content or ""})

        if not has_talk:
            yield sse_event({
                "type": "TALK",
                "content": "(Tidak ada respons verbal. Coba ubah pertanyaan.)"
            })
        yield sse_event({"type": "END", "session_id": session_id})

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.route("/api/reset", methods=["POST"])
def reset():
    data = request.get_json(force=True)
    persona_id = data.get("persona_id", "julia")
    session_id = data.get("session_id")
    if not session_id:
        return jsonify({"error": "session_id diperlukan"}), 400
    if persona_id not in PERSONAS:
        return jsonify({"error": f"Persona '{persona_id}' tidak dikenal"}), 400

    key = f"{persona_id}:{session_id}"
    with sessions_lock:
        sessions.pop(key, None)
    return jsonify({"status": "ok", "session_id": session_id})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8018))
    import socket
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except Exception:
        local_ip = "cek ifconfig"

    print(f"\n🟢 Server jalan di:")
    print(f"   Lokal  → http://localhost:{port}")
    print(f"   Tim    → http://{local_ip}:{port}  (satu WiFi)\n")
    app.run(host="0.0.0.0", port=port, threaded=True)
