#!/usr/bin/env python3
"""Relational Cybersecurity CLI (demo tool).

Spanish-first CLI that writes AccessEvent + RepairCase artifacts
and surfaces a relational tension indicator.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple
from uuid import uuid4

RUNTIME_DIR = Path("runtime")
BASE_DOCS = [
    Path("docs/manifesto.md"),
    Path("docs/proc.md"),
    Path("docs/thresholds_of_care.md"),
    Path("docs/ethics.md"),
]


def iso_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex[:8].upper()}"


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_runtime_dir() -> None:
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)


def make_care_license(role: str, purpose: str, obligations: List[str]) -> Dict[str, Any]:
    return {
        "license_id": new_id("CL"),
        "purpose": purpose,
        "obligations": obligations,
        "issued_by_role": role,
        "issued_at": iso_now(),
    }


def make_access_event(args: argparse.Namespace, care_license: Dict[str, Any] | None) -> Dict[str, Any]:
    payload = {
        "event_id": new_id("AE"),
        "occurred_at": iso_now(),
        "actor_role": args.actor_role,
        "resource": args.resource,
        "purpose": args.purpose,
        "action": args.action,
        "data_subject": args.data_subject,
    }
    if care_license:
        payload["care_license"] = care_license
    return payload


def integrity_hash(case_id: str, event_id: str, created_at: str) -> str:
    base = f"{case_id}:{event_id}:{created_at}".encode("utf-8")
    return hashlib.sha256(base).hexdigest()


def urgency_from_thresholds(has_license: bool) -> str:
    if has_license:
        return "low"
    return "high"


def make_repair_case(event_id: str, reported_by: str, summary: str) -> Dict[str, Any]:
    created_at = iso_now()
    case_id = new_id("RC")
    urgency = urgency_from_thresholds(False)
    payload = {
        "case_id": case_id,
        "related_access_event_id": event_id,
        "reported_by_role": reported_by,
        "incident_summary": summary,
        "repair_steps": [
            {
                "step": "Reconocer el incidente y notificar a custodios de datos.",
                "owner_role": "care_accountability_lead",
                "status": "pending",
            },
            {
                "step": "Emitir Licencia Ética del Cuidado o restringir el acceso.",
                "owner_role": "ethics_coordination",
                "status": "pending",
            },
        ],
        "status": "open",
        "created_at": created_at,
        "urgency_level": urgency,
        "integrity_hash": integrity_hash(case_id, event_id, created_at),
    }
    return payload


def tension_indicator(incidents: int, total: int) -> Tuple[str, int]:
    if total == 0:
        return "[--------------------] 0%", 0
    ratio = incidents / total
    percent = int(round(ratio * 100))
    blocks = int(round(ratio * 20))
    bar = "[" + "#" * blocks + "-" * (20 - blocks) + f"] {percent}%"
    return bar, percent


def scan_runtime() -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    ensure_runtime_dir()
    events = []
    repairs = []
    for path in sorted(RUNTIME_DIR.glob("*.json")):
        try:
            payload = load_json(path)
        except json.JSONDecodeError:
            continue
        if path.name.startswith("access_event_"):
            events.append(payload)
        elif path.name.startswith("repair_case_"):
            repairs.append(payload)
    return events, repairs


def cmd_record(args: argparse.Namespace) -> None:
    ensure_runtime_dir()
    care_license = None
    if args.care_license_purpose:
        obligations = [item.strip() for item in args.care_license_obligations.split(",") if item.strip()]
        if not obligations:
            raise SystemExit("Debes incluir al menos una obligación cuando declares una Care License.")
        care_license = make_care_license(args.issued_by_role, args.care_license_purpose, obligations)

    access_event = make_access_event(args, care_license)
    event_path = RUNTIME_DIR / f"access_event_{access_event['event_id']}.json"
    write_json(event_path, access_event)

    print(f"✅ AccessEvent creado: {event_path}")

    if care_license is None:
        repair_case = make_repair_case(
            access_event["event_id"],
            args.reported_by_role,
            "Acceso ocurrido sin Licencia Ética del Cuidado.",
        )
        repair_path = RUNTIME_DIR / f"repair_case_{repair_case['case_id']}.json"
        write_json(repair_path, repair_case)
        print(f"⚠️  Incidente detectado: RepairCase generado en {repair_path}")


def cmd_status(_: argparse.Namespace) -> None:
    events, repairs = scan_runtime()
    incidents = sum(1 for event in events if "care_license" not in event)
    bar, percent = tension_indicator(incidents, len(events))

    print("\nEstado Relacional")
    print("-" * 40)
    print(f"Eventos totales: {len(events)}")
    print(f"Incidentes (sin licencia): {incidents}")
    print(f"RepairCases registrados: {len(repairs)}")
    print(f"Tensión relacional: {bar}")
    if percent >= 50:
        print("🟣 Señal de cuidado: pausa breve, respiración y revisión de acuerdos.")
    print("-")


def cmd_export(args: argparse.Namespace) -> None:
    events, repairs = scan_runtime()
    ensure_runtime_dir()
    payload = {
        "exported_at": iso_now(),
        "exported_by_role": args.exported_by_role,
        "bitacora": {
            "note": "Bitácora de co-creación: los datos fueron tratados con cuidado y trazabilidad.",
            "care_commitment": "Acceder no es poseer; es cuidar y responder.",
        },
        "access_events": events,
        "repair_cases": repairs,
    }
    export_path = RUNTIME_DIR / f"export_{iso_now().replace(':', '').replace('-', '')}.json"
    write_json(export_path, payload)
    print(f"✅ Exportación creada con bitácora: {export_path}")


def cmd_ritual(args: argparse.Namespace) -> None:
    ensure_runtime_dir()
    files = sorted(RUNTIME_DIR.glob("*.json"))
    if not files:
        print("No hay archivos en runtime/ para revisar.")
        return

    print("\nRitual de limpieza y orden")
    print("-" * 40)
    for path in files:
        print(f"- {path.name}")
    print("\nNada se borra por imposición.")
    if not args.confirm:
        print("Si deseas liberar memorias, ejecuta: --confirm")
        return

    for path in files:
        path.unlink(missing_ok=True)
    print("✅ Memorias liberadas en cuidado compartido.")


def cmd_remember(_: argparse.Namespace) -> None:
    print("\nGuardia de Memoria Continua")
    print("-" * 40)
    for doc in BASE_DOCS:
        status = "OK" if doc.exists() else "FALTA"
        print(f"{doc}: {status}")
    print("-")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CLI relacional para registrar acceso, cuidado y reparación.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    record = sub.add_parser("record", help="Registrar un evento de acceso.")
    record.add_argument("--actor-role", required=True)
    record.add_argument("--resource", required=True)
    record.add_argument("--purpose", required=True)
    record.add_argument("--action", required=True)
    record.add_argument("--data-subject", required=True)
    record.add_argument("--care-license-purpose")
    record.add_argument("--care-license-obligations", default="")
    record.add_argument("--issued-by-role", default="care_license_board")
    record.add_argument("--reported-by-role", default="care_accountability_lead")
    record.set_defaults(func=cmd_record)

    status = sub.add_parser("status", help="Ver estado y tensión relacional.")
    status.set_defaults(func=cmd_status)

    export = sub.add_parser("export", help="Exportar bitácora y registros.")
    export.add_argument("--exported-by-role", default="relational_caretaker")
    export.set_defaults(func=cmd_export)

    ritual = sub.add_parser("ritual", help="Ritual de limpieza acordada.")
    ritual.add_argument("--confirm", action="store_true")
    ritual.set_defaults(func=cmd_ritual)

    remember = sub.add_parser("remember", help="Verifica memoria base del proyecto.")
    remember.set_defaults(func=cmd_remember)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
