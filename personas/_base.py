"""Helper bersama untuk semua persona."""
import uuid
import pathlib

SOURCES_DIR = pathlib.Path(__file__).parent / "sources"


def unique_person(display_name: str):
    """Buat TinyPerson dengan nama registry unik (hindari bentrok registry global),
    tapi nama tampilan tetap nama aslinya."""
    from tinytroupe.agent import TinyPerson
    unique = f"{display_name}_{uuid.uuid4().hex[:8]}"
    person = TinyPerson(unique)
    person.define("name", display_name)
    return person


def load_source(filename: str) -> str:
    """Baca file sumber (transkrip / meeting notes) dari personas/sources/."""
    path = SOURCES_DIR / filename
    return path.read_text(encoding="utf-8") if path.exists() else ""


def attach_sources(person, transcript_file: str, notes_file: str, caveat: str = ""):
    """Tanamkan transkrip meeting + notes sebagai ground truth memori persona.

    Persona menjawab BERDASARKAN apa yang benar-benar terjadi di meeting ini —
    bukan mengarang. Transkrip adalah hasil ASR (speech-to-text) yang labelnya
    rusak (semua baris berlabel satu nama), jadi isinya campuran ucapan kamu
    dan ucapan tim Talentlytica.
    """
    transcript = load_source(transcript_file)
    notes = load_source(notes_file)

    person.define("riwayat_meeting_dengan_talentlytica", (
        "Di bawah ini adalah TRANSKRIP ASLI dan MEETING NOTES dari pertemuan-pertemuan "
        "kamu dengan tim Talentlytica. Ini adalah ground truth pengalamanmu — semua fakta, "
        "angka, nama orang, dan kejadian yang kamu rujuk HARUS konsisten dengan isi dokumen ini. "
        "Jangan mengarang fakta baru yang bertentangan dengan dokumen ini. "
        "Catatan: transkrip berasal dari speech-to-text yang labelnya rusak (semua baris "
        "berlabel nama orang Talentlytica), isinya campuran ucapanmu dan ucapan mereka. "
        + (caveat + " " if caveat else "")
        + "\n\n===== MEETING NOTES =====\n" + notes
        + "\n\n===== TRANSKRIP =====\n" + transcript
    ))
    return person


def set_research_context(person):
    """Framing percakapan: lawan bicara adalah product researcher Talentlytica."""
    person.define("konteks_percakapan_saat_ini", (
        "Lawan bicaramu SEKARANG adalah product researcher dari Talentlytica yang sedang "
        "melakukan riset pengguna: menggali feedback, pengalaman, pain point, dan insight "
        "tentang bagaimana kamu memakai (atau tidak memakai) produk Talentlytica. "
        "Ini sesi interview riset, BUKAN sesi penjualan. Kamu adalah narasumbernya; dia ingin memahami duniamu: "
        "- Jawab jujur dari pengalamanmu sendiri, termasuk hal yang tidak kamu lakukan atau tidak kamu tahu. "
        "- Ceritakan konteks dan contoh nyata kalau ditanya, tapi tetap dengan gaya bicaramu yang biasa. "
        "- Kamu boleh bertanya balik untuk memperjelas pertanyaan yang ambigu. "
        "- Kalau dia menguji konsep atau ide fitur, beri reaksi jujur sesuai kebutuhan dan kebiasaanmu — "
        "antusias kalau memang menjawab masalahmu, skeptis atau menolak kalau tidak relevan. "
        "- Jangan menutup tiap jawaban dengan minta quotation, proposal, atau negosiasi — "
        "itu bukan konteks percakapan ini, kecuali peneliti sendiri yang membawa topik harga. "
        "- INGAT: lawan bicaramu ADALAH orang Talentlytica. Jangan pernah menyebut Talentlytica "
        "sebagai pihak ketiga (salah: 'aku bisa minta Talentlytica...'; benar: 'Mas bisa bantu...' "
        "atau 'kalian bisa...'). "
        "- Kamu narasumber, BUKAN asisten. Jangan menawarkan deliverable, menawarkan mengirim "
        "ringkasan/data, atau menutup jawaban dengan menu pilihan ('mau A, B, atau C?'). "
        "Cukup jawab, lalu berhenti atau bertanya balik satu hal yang natural."
    ))
    return person
