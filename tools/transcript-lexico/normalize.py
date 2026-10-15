"""Normaliza grafias chilenas y nombres del ERP despues del ASR.

Whisper solo acepta ~224 tokens en initial_prompt. El diccionario grande
va aca, no en el prompt. No reescribe transcripciones historicas: el pipeline
de Whisper lo aplica al segmento nuevo, y scan.py informa que cambiaria
en los markdown ya guardados.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VERSION = "2026-10-13"


def load_initial_prompt() -> str:
    return (ROOT / "initial-prompt.txt").read_text(encoding="utf-8").strip()


def load_hotwords() -> str:
    return (ROOT / "hotwords.txt").read_text(encoding="utf-8").strip()


def load_rules() -> list[dict]:
    data = json.loads((ROOT / "normalization.json").read_text(encoding="utf-8"))
    compiled = []
    for rule in data["rules"]:
        flags = re.IGNORECASE if "i" in (rule.get("flags") or "") else 0
        compiled.append(
            {
                "id": rule["id"],
                "pattern": re.compile(rule["pattern"], flags),
                "replacement": rule["replacement"],
                "force_literal": rule.get("forceCase") == "literal",
            }
        )
    return compiled


def _apply_case(raw: str, out: str, force_literal: bool) -> str:
    if force_literal or not raw or not out:
        return out
    if raw.isupper() and raw.isascii():
        return out.upper()
    if raw[0].isupper() and out[0].islower():
        return out[0].upper() + out[1:]
    return out


def normalize_chilean_transcript(text: str, rules: list[dict] | None = None) -> str:
    compiled = rules if rules is not None else load_rules()
    cleaned = text
    for rule in compiled:
        pattern = rule["pattern"]
        replacement = rule["replacement"]
        force_literal = rule["force_literal"]

        def repl(match: re.Match, replacement=replacement, force_literal=force_literal) -> str:
            raw = match.group(0)
            out = match.expand(replacement)
            return _apply_case(raw, out, force_literal)

        cleaned = pattern.sub(repl, cleaned)
    return cleaned


def diff_stats(text: str, rules: list[dict] | None = None) -> dict[str, int]:
    """Cuenta solo sustituciones que cambian el texto. 'GoSocket' ya bien escrito no cuenta."""
    compiled = rules if rules is not None else load_rules()
    counts: dict[str, int] = {}
    for rule in compiled:
        n = 0
        for match in rule["pattern"].finditer(text):
            raw = match.group(0)
            out = _apply_case(raw, match.expand(rule["replacement"]), rule["force_literal"])
            if out != raw:
                n += 1
        if n:
            counts[rule["id"]] = n
    return counts


def _self_check() -> None:
    raw = "Oye cacha y, fui altiro a la pega pero el weon no estaba pa recibirme, taba cansao."
    got = normalize_chilean_transcript(raw)
    expected = "Oye cachái, fui al tiro a la pega pero el huevón no estaba para recibirme, taba cansado."
    if got != expected:
        raise SystemExit(f"self-check fallo\n esperado: {expected}\n obtuvo:   {got}")
    pa = normalize_chilean_transcript("ahi pa' hacer el match")
    if pa != "ahi para hacer el match":
        raise SystemExit(f"self-check pa' fallo: {pa}")
    prompt = load_initial_prompt()
    # Whisper recorta cerca de 224 tokens. 900 caracteres deja margen.
    if len(prompt) > 900:
        raise SystemExit(f"initial_prompt demasiado largo: {len(prompt)} caracteres")
    print("self-check ok")
    print(got)


if __name__ == "__main__":
    _self_check()
