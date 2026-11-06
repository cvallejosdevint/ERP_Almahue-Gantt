"""Transcribe reunion 2026-11-03 (AM + PM screen recordings) y genera minuta + HTML interactivo."""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from pathlib import Path

_TOOL = Path(__file__).resolve().parent
_REPO = _TOOL.parents[1]
_LEXICO = _REPO / "tools" / "transcript-lexico"
if str(_LEXICO) not in sys.path:
    sys.path.insert(0, str(_LEXICO))

from normalize import load_hotwords, load_initial_prompt, normalize_chilean_transcript  # noqa: E402
from transcribe_one import _prepend_nvidia_cuda_bins  # noqa: E402
from faster_whisper import WhisperModel  # noqa: E402

AM_WAV = _REPO / "docs/reuniones/medios/whisper-local/2026-11-03-reunion-am/audio.wav"
PM_WAV = _REPO / "docs/reuniones/medios/whisper-local/2026-11-03-reunion-pm/audio.wav"
AM_SRC = r"C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-11-03 115116.mp4 (00:42:16)"
PM_SRC = r"C:\Users\c\Videos\Screen Recordings\Screen Recording 2026-11-03 173934.mp4 (02:38:24)"

OUT_AM = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion-am.md"
OUT_PM = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion-pm.md"
OUT_FULL = _REPO / "docs/reuniones/transcripciones/transcripcion-2026-11-03-reunion.md"
MINUTA = _REPO / "docs/reuniones/minutas/reunion-2026-11-03-cliente.md"
HTML = _REPO / "docs/reuniones/minutas/reunion-2026-11-03-cliente-interactiva.html"
README = _REPO / "docs/reuniones/medios/whisper-local/2026-11-03-reunion-am/README.md"


def transcribe_session(
    model: WhisperModel,
    wav: Path,
    title: str,
    source: str,
    session_label: str,
) -> tuple[str, list[dict]]:
    prompt = load_initial_prompt()
    hotwords = load_hotwords()
    segments, info = model.transcribe(
        str(wav),
        language="es",
        vad_filter=True,
        beam_size=5,
        initial_prompt=prompt,
        hotwords=hotwords,
        condition_on_previous_text=False,
    )
    lines = [
        f"# {title}",
        "",
        f"Idioma: {info.language} (p={info.language_probability:.2f})",
        "Modelo: faster-whisper `large-v3` cuda float16 + VAD",
        f"Fuente: {source}",
        "Normalizacion: tools/transcript-lexico (grafias chilenas y nombres del ERP).",
        "",
    ]
    items: list[dict] = []
    for seg in segments:
        t0 = int(seg.start)
        hh, rem = divmod(t0, 3600)
        mm, ss = divmod(rem, 60)
        stamp = f"{hh:02d}:{mm:02d}:{ss:02d}" if hh else f"{mm:02d}:{ss:02d}"
        text = normalize_chilean_transcript((seg.text or "").strip())
        if not text:
            continue
        anchor = f"{session_label}-{stamp.replace(':', '-')}"
        lines.append(f"- [{stamp}] {text}")
        items.append({"session": session_label, "stamp": stamp, "text": text, "anchor": anchor})
        print(f"[{session_label} {stamp}] {text[:80]}", flush=True)
    body = "\n".join(lines) + "\n"
    return body, items


def merge_transcripts(am_body: str, pm_body: str) -> str:
    return (
        "# Reunion Almahue 2026-11-03 (Whisper large-v3 + lexico)\n\n"
        "Sesiones: AM (~42 min) + PM (~2 h 38 min). Screen recordings Windows.\n\n"
        "## Parte AM\n\n"
        + "\n".join(am_body.splitlines()[8:])
        + "\n## Parte PM\n\n"
        + "\n".join(pm_body.splitlines()[8:])
    )


def ollama_minuta(full_transcript: str) -> str:
    prompt_file = _REPO / "tools/transcript-ollama/prompts/system-es-cl.md"
    system_prompt = prompt_file.read_text(encoding="utf-8")
    user_prompt = f"""{system_prompt}

Transcripcion reunion 03/11/2026 (ERP Almahue, screen recording):

---
{full_transcript[:120000]}
---

Genera SOLO markdown de minuta tecnica para desarrollo:
- Encabezado con fecha, fuentes de audio, participantes (solo si aparecen nombrados: MJ, Fran, Lupe, Mario, Agustin, Carlos, Sergio, etc.).
- Secciones por modulo (Compras, Contratistas, Insumos, Contabilidad, Tesoreria, DTE, Admin, otros).
- Bajo cada punto: **Acuerdo** o **Pendiente** con citas [MM:SS] o [HH:MM:SS] de la sesion AM o PM (prefijo AM/PM si ayuda).
- Lista final **Compromisos y proximos pasos** numerados.
- No uses raya larga ni flecha unicode. Carlos/Sergio en demo = marcar como hipotesis Devint si no confirma cliente.
- Prohibido mermas.
"""
    payload = {
        "model": "qwen2.5-coder:14b",
        "prompt": user_prompt,
        "stream": False,
        "options": {"num_ctx": 32768, "temperature": 0.2},
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=1200) as resp:
        res = json.loads(resp.read().decode("utf-8"))
    return res.get("response", "")


def parse_minuta_sections(minuta_md: str) -> list[dict]:
    sections: list[dict] = []
    current: dict | None = None
    mod_map = {
        "compras": "compras",
        "contratista": "param",
        "insumo": "compras",
        "bodega": "compras",
        "contab": "conta",
        "tesorer": "teso",
        "dte": "ventas",
        "gosocket": "ventas",
        "ventas": "ventas",
        "admin": "param",
        "param": "param",
    }
    for line in minuta_md.splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            mod = "param"
            low = title.lower()
            for key, cls in mod_map.items():
                if key in low:
                    mod = cls
                    break
            current = {"title": title, "mod": mod, "lines": []}
            sections.append(current)
        elif current is not None and line.strip():
            current["lines"].append(line)
    return sections


def build_interactive_html(minuta_md: str, items: list[dict]) -> str:
    sections = parse_minuta_sections(minuta_md)
    if not sections:
        sections = [{"title": "Resumen", "mod": "param", "lines": minuta_md.splitlines()[:40]}]

    def find_quote(stamp_hint: str) -> str:
        m = re.search(r"\[?(AM|PM)?\s*(\d{1,2}:\d{2}(?::\d{2})?)\]?", stamp_hint)
        if not m:
            return ""
        stamp = m.group(2)
        for it in items:
            if it["stamp"] == stamp or it["stamp"].endswith(stamp):
                return it["text"][:280]
        return ""

    steps_js = []
    for i, sec in enumerate(sections):
        body = " ".join(sec["lines"])
        body_html = "<br>".join(sec["lines"]).replace('"', "&quot;")
        quote = ""
        for ln in sec["lines"]:
            q = find_quote(ln)
            if q:
                quote = q
                break
        steps_js.append(
            {
                "mod": sec["mod"].upper() if len(sec["mod"]) <= 6 else sec["title"].split()[0],
                "cls": sec["mod"],
                "title": f"{i + 1}. {sec['title']}",
                "body": body_html,
                "quote": quote.replace('"', "&quot;"),
            }
        )

    steps_json = json.dumps(steps_js, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <title>Minuta interactiva - Reunion 03/11/2026</title>
  <style>
    :root {{ --bg: #f4f1ea; --ink: #1c1917; --muted: #57534e; --line: #e7e5e4; --card: #fff;
      --compras: #9a3412; --ventas: #166534; --conta: #1d4ed8; --teso: #b45309; --param: #0f766e; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font: 15px/1.4 "Segoe UI", sans-serif; background: var(--bg); color: var(--ink); }}
    header {{ padding: 10px 18px; border-bottom: 1px solid var(--line); max-width: 1200px; margin: 0 auto; }}
    h1 {{ margin: 0; font-size: 1.1rem; }}
    .sub {{ color: var(--muted); font-size: 13px; margin-top: 4px; }}
    .layout {{ display: grid; grid-template-columns: 280px 1fr; gap: 12px; max-width: 1200px; margin: 0 auto; padding: 10px 18px 24px; }}
    nav {{ position: sticky; top: 12px; background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 6px; max-height: calc(100vh - 80px); overflow-y: auto; }}
    nav button {{ display: grid; grid-template-columns: 28px 1fr; gap: 8px; width: 100%; text-align: left; border: 0; background: transparent; border-radius: 8px; padding: 6px 8px; cursor: pointer; font: inherit; }}
    nav button.on {{ background: #f5f5f4; }}
    .n {{ width: 28px; height: 28px; border-radius: 50%; display: grid; place-items: center; color: #fff; font-size: 12px; font-weight: 700; }}
    .compras {{ background: var(--compras); }} .ventas {{ background: var(--ventas); }} .conta {{ background: var(--conta); }}
    .teso {{ background: var(--teso); }} .param {{ background: var(--param); }}
    .card {{ background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 14px 16px; }}
    .card h2 {{ margin: 0 0 8px; font-size: 1.05rem; }}
    .quote {{ margin-top: 12px; padding: 10px 12px; background: #fafaf9; border-left: 4px solid #78716c; font-size: 14px; color: var(--muted); }}
    .links {{ margin-top: 12px; font-size: 13px; }}
    .links a {{ color: #1d4ed8; }}
    @media (max-width: 900px) {{ .layout {{ grid-template-columns: 1fr; }} nav {{ position: static; max-height: none; }} }}
  </style>
</head>
<body>
  <header>
    <h1>Minuta interactiva - Reunion 03/11/2026</h1>
    <p class="sub">Indice de acuerdos. Fuente primaria: transcripcion Whisper. Minuta generada para desarrollo.</p>
  </header>
  <div class="layout">
    <nav id="rail"></nav>
    <main class="card" id="panel"></main>
  </div>
  <script>
    const steps = {steps_json};
    let idx = 0;
    const rail = document.getElementById("rail");
    const panel = document.getElementById("panel");
    steps.forEach((s, i) => {{
      const b = document.createElement("button");
      b.innerHTML = `<span class="n ${{s.cls}}">${{i+1}}</span><span>${{s.title.replace(/^\\d+\\.\\s/, "")}}</span>`;
      b.onclick = () => show(i);
      rail.appendChild(b);
    }});
    function show(i) {{
      idx = i;
      [...rail.children].forEach((el, j) => el.classList.toggle("on", j === i));
      const s = steps[i];
      let q = s.quote ? `<div class="quote"><strong>Cita transcripcion:</strong> ${{s.quote}}</div>` : "";
      panel.innerHTML = `<h2>${{s.title}}</h2><div>${{s.body}}</div>${{q}}
        <div class="links">Ver texto completo:
          <a href="../transcripciones/transcripcion-2026-11-03-reunion.md">transcripcion consolidada</a>
          | <a href="reunion-2026-11-03-cliente.md">minuta markdown</a>
        </div>`;
    }}
    show(0);
  </script>
</body>
</html>
"""


def main() -> int:
    _prepend_nvidia_cuda_bins()
    t0 = time.time()
    print("Cargando Whisper large-v3...")
    model = WhisperModel("large-v3", device="cuda", compute_type="float16")

    print("\n=== AM ===")
    am_body, am_items = transcribe_session(
        model,
        AM_WAV,
        "Reunion Almahue 2026-11-03 AM (Whisper large-v3 + lexico)",
        AM_SRC,
        "AM",
    )
    OUT_AM.write_text(am_body, encoding="utf-8")

    print("\n=== PM ===")
    pm_body, pm_items = transcribe_session(
        model,
        PM_WAV,
        "Reunion Almahue 2026-11-03 PM (Whisper large-v3 + lexico)",
        PM_SRC,
        "PM",
    )
    OUT_PM.write_text(pm_body, encoding="utf-8")

    full = merge_transcripts(am_body, pm_body)
    OUT_FULL.write_text(full, encoding="utf-8")
    all_items = am_items + pm_items

    README.parent.mkdir(parents=True, exist_ok=True)
    README.write_text(
        "# Reunion 2026-11-03\n\n"
        f"- AM: `{AM_SRC}`\n"
        f"- PM: `{PM_SRC}`\n"
        f"- Transcripcion: `{OUT_FULL.relative_to(_REPO).as_posix()}`\n",
        encoding="utf-8",
    )

    del model
    time.sleep(2)

    print("\nGenerando minuta Ollama...")
    try:
        minuta = ollama_minuta(full)
    except Exception as e:
        print(f"Ollama fallo: {e}")
        minuta = (
            "# Reunion 2026-11-03 (borrador)\n\n"
            "Minuta automatica pendiente: Ollama no disponible. Ver transcripcion consolidada.\n"
        )
    MINUTA.write_text(minuta, encoding="utf-8")

    html = build_interactive_html(minuta, all_items)
    HTML.write_text(html, encoding="utf-8")

    print(f"\nListo en {time.time()-t0:.0f}s")
    print(OUT_FULL)
    print(MINUTA)
    print(HTML)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
