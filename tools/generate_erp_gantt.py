#!/usr/bin/env python3
"""Genera CSV, JSON y validación de la carta Gantt ERP v1 (6 meses)."""

from __future__ import annotations

import csv
import json
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs" / "erp-planificacion"
PROJECT_START = date(2026, 7, 13)  # lunes
PROJECT_END_TARGET = date(2027, 1, 9)  # viernes go-live


from erp_gantt_tasks import MILESTONES, TASKS, Task
from erp_gantt_traceability import build_traceability


def add_business_days(start: date, days: int) -> date:
    """Suma días hábiles (lun-vie). days=1 => mismo día si hábil."""
    if days <= 0:
        return start
    current = start
    added = 0
    while added < days:
        if current.weekday() < 5:
            added += 1
            if added < days:
                current += timedelta(days=1)
        else:
            current += timedelta(days=1)
    return current


def next_business_day(d: date) -> date:
    current = d
    while current.weekday() >= 5:
        current += timedelta(days=1)
    return current


def task_end(start: date, duration: int) -> date:
    return add_business_days(start, duration)


TIPO_ORDER = {"def": 0, "mock": 1, "fb": 2, "infra": 3, "back": 4, "front": 5, "qa": 6}


def _resource_pool(task: Task, back_slots: int, front_slots: int) -> tuple[str, int]:
    if task.tipo in ("front", "mock", "fb"):
        return "front", front_slots
    if task.tipo in ("back", "def"):
        return "back", back_slots
    if task.tipo in ("infra", "qa"):
        return task.tipo, 1
    return "back", back_slots


def list_schedule(
    tasks: list[Task],
    *,
    back_slots: int = 1,
    front_slots: int = 1,
    fullstack: bool = False,
) -> dict[str, tuple[date, date]]:
    """Planificación por lista con recursos paralelos (back/front/infra/qa)."""
    by_id = {t.id: t for t in tasks}
    for t in tasks:
        for dep in t.dependencias:
            if dep not in by_id:
                raise ValueError(f"{t.id} depende de {dep} inexistente")

    pools: dict[str, list[date]] = {
        "back": [PROJECT_START] * (1 if fullstack else back_slots),
        "front": [PROJECT_START] * (1 if fullstack else front_slots),
        "infra": [PROJECT_START],
        "qa": [PROJECT_START],
        "fullstack": [PROJECT_START],
    }

    end_dates: dict[str, date] = {}
    start_dates: dict[str, date] = {}
    scheduled: set[str] = set()

    def dep_ready_end(deps: list[str]) -> date:
        if not deps:
            return PROJECT_START
        end = max(end_dates[d] for d in deps)
        return next_business_day(end + timedelta(days=1))

    def pick_pool(task: Task) -> tuple[str, int]:
        if fullstack:
            return "fullstack", 1
        kind, size = _resource_pool(task, back_slots, front_slots)
        return kind, size

    while len(scheduled) < len(tasks):
        ready = [
            t for t in tasks
            if t.id not in scheduled and all(d in scheduled for d in t.dependencias)
        ]
        if not ready:
            raise ValueError("Ciclo o dependencia rota en tareas")

        # Priorizar: definiciones → mockups → feedback → back → front
        ready.sort(key=lambda t: (t.fase, TIPO_ORDER.get(t.tipo, 9), t.id))

        progress = False
        for t in ready:
            pool_name, pool_size = pick_pool(t)
            pool = pools[pool_name]
            dep_end = dep_ready_end(t.dependencias)
            if t.fecha_minima:
                dep_end = max(dep_end, t.fecha_minima)
            idx = min(range(len(pool)), key=lambda i: pool[i])
            start = max(dep_end, pool[idx])
            start = next_business_day(start)
            end = task_end(start, t.duracion_dias)
            start_dates[t.id] = start
            end_dates[t.id] = end
            pool[idx] = next_business_day(end + timedelta(days=1))
            scheduled.add(t.id)
            progress = True

        if not progress:
            break

    return {tid: (start_dates[tid], end_dates[tid]) for tid in start_dates}


def schedule(tasks: list[Task], team: str) -> dict[str, tuple[date, date]]:
    if team == "1dev":
        return list_schedule(tasks, fullstack=True)
    if team == "2dev":
        return list_schedule(tasks, back_slots=1, front_slots=1)
    if team == "plan":
        # Escenario mínimo validado para ventana 6 meses: 2 back + 2 front
        return list_schedule(tasks, back_slots=2, front_slots=2)
    raise ValueError(f"Equipo desconocido: {team}")


def critical_path(tasks: list[Task], schedule_map: dict[str, tuple[date, date]]) -> list[str]:
    by_id = {t.id: t for t in tasks}
    # Backtrack from latest end
    latest = max(schedule_map.items(), key=lambda x: x[1][1])
    path = [latest[0]]
    current_end = latest[1][0]
    visited = set(path)

    while True:
        t = by_id[path[-1]]
        if not t.dependencias:
            break
        # pick dependency that ends latest before current start
        candidates = []
        for dep in t.dependencias:
            dep_start, dep_end = schedule_map[dep]
            if dep_end < current_end and dep not in visited:
                candidates.append((dep_end, dep))
        if not candidates:
            # pick any critical dep
            candidates = [(schedule_map[d][1], d) for d in t.dependencias]
        candidates.sort(reverse=True)
        chosen = candidates[0][1]
        path.append(chosen)
        visited.add(chosen)
        current_end = schedule_map[chosen][0]
        if len(path) > 200:
            break
    path.reverse()
    return path


def write_csv(path: Path, tasks: list[Task], schedule_map: dict[str, tuple[date, date]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "nombre", "tipo", "modulo", "fase", "fecha_inicio", "fecha_fin", "duracion_dias", "dependencias", "entregable", "riesgo"])
        for t in tasks:
            start, end = schedule_map[t.id]
            w.writerow([
                t.id, t.nombre, t.tipo, t.modulo, t.fase,
                start.isoformat(), end.isoformat(), t.duracion_dias,
                "|".join(t.dependencias), t.entregable, t.riesgo,
            ])


def write_json(path: Path, tasks: list[Task], schedule_map: dict[str, tuple[date, date]], team: str) -> None:
    cp = critical_path(tasks, schedule_map)
    project_end = max(schedule_map.values(), key=lambda x: x[1])[1]
    milestones_out = []
    end_by_id = {tid: schedule_map[tid][1] for tid in schedule_map}
    for m in MILESTONES:
        after = m["after"]
        milestones_out.append({
            **m,
            "fecha": end_by_id[after].isoformat(),
        })

    payload = {
        "proyecto": "ERP v1 Web",
        "equipo": team,
        "fecha_inicio": PROJECT_START.isoformat(),
        "fecha_fin": project_end.isoformat(),
        "fecha_fin_objetivo": PROJECT_END_TARGET.isoformat(),
        "dentro_plazo": project_end <= PROJECT_END_TARGET,
        "tasks": [
            {
                "id": t.id,
                "nombre": t.nombre,
                "tipo": t.tipo,
                "modulo": t.modulo,
                "fase": t.fase,
                "duracion_dias": t.duracion_dias,
                "fecha_inicio": schedule_map[t.id][0].isoformat(),
                "fecha_fin": schedule_map[t.id][1].isoformat(),
                "dependencias": t.dependencias,
                "paralelizable_con": t.paralelizable_con,
                "entregable": t.entregable,
                "criterio_aceptacion": t.criterio_aceptacion,
                "riesgo": t.riesgo,
            }
            for t in tasks
        ],
        "critical_path": cp,
        "milestones": milestones_out,
        "traceability": build_traceability(),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return project_end, cp


def business_days_between(start: date, end: date) -> int:
    count = 0
    current = start
    while current <= end:
        if current.weekday() < 5:
            count += 1
        current += timedelta(days=1)
    return count


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    sched_1 = schedule(TASKS, "1dev")
    write_csv(OUT_DIR / "erp_gantt_tareas_1dev.csv", TASKS, sched_1)
    end_1, cp_1 = write_json(OUT_DIR / "erp_dependencias_1dev.json", TASKS, sched_1, "1 dev fullstack")

    sched_2 = schedule(TASKS, "2dev")
    write_csv(OUT_DIR / "erp_gantt_tareas_2dev.csv", TASKS, sched_2)
    end_2, cp_2 = write_json(OUT_DIR / "erp_dependencias_2dev.json", TASKS, sched_2, "2 devs (1 back + 1 front)")

    sched_plan = schedule(TASKS, "plan")
    write_csv(OUT_DIR / "erp_gantt_tareas.csv", TASKS, sched_plan)
    end_plan, cp_plan = write_json(
        OUT_DIR / "erp_dependencias.json",
        TASKS,
        sched_plan,
        "Plan objetivo: 2 back + 2 front (4 FTE)",
    )

    total_person_days = sum(t.duracion_dias for t in TASKS)
    window_days = business_days_between(PROJECT_START, PROJECT_END_TARGET)

    summary = {
        "fecha_inicio": PROJECT_START.isoformat(),
        "fecha_fin_objetivo": PROJECT_END_TARGET.isoformat(),
        "ventana_dias_habiles": window_days,
        "esfuerzo_total_persona_dia": total_person_days,
        "escenarios": {
            "1dev_fullstack": {
                "fin": end_1.isoformat(),
                "dentro_plazo": end_1 <= PROJECT_END_TARGET,
                "dias_desviacion": business_days_between(PROJECT_END_TARGET, end_1) if end_1 > PROJECT_END_TARGET else 0,
                "critical_path_ids": len(cp_1),
            },
            "2dev_back_front": {
                "fin": end_2.isoformat(),
                "dentro_plazo": end_2 <= PROJECT_END_TARGET,
                "dias_desviacion": business_days_between(PROJECT_END_TARGET, end_2) if end_2 > PROJECT_END_TARGET else 0,
                "critical_path_ids": len(cp_2),
            },
            "plan_2back_2front": {
                "fin": end_plan.isoformat(),
                "dentro_plazo": end_plan <= PROJECT_END_TARGET,
                "dias_desviacion": business_days_between(PROJECT_END_TARGET, end_plan) if end_plan > PROJECT_END_TARGET else 0,
                "critical_path_ids": len(cp_plan),
                "recomendado": True,
            },
        },
        "nota": "298 persona-dia v3.1 Enterprise. Validado vs PDFs. 85 tareas. Sin Prod/RRHH v1.",
    }
    (OUT_DIR / "validacion_fechas.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
