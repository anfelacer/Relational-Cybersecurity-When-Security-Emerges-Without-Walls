import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker, RefResolver
from jsonschema.exceptions import ValidationError

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS_DIR = ROOT / "schemas"
EXAMPLES_DIR = ROOT / "examples"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_schema_store():
    store = {}
    for schema_path in SCHEMAS_DIR.glob("*.schema.json"):
        schema = load_json(schema_path)
        store[schema_path.as_uri()] = schema
        schema_id = schema.get("$id")
        if schema_id:
            store[schema_id] = schema
    return store


def build_validator(schema_name: str, store) -> Draft202012Validator:
    schema_path = SCHEMAS_DIR / schema_name
    schema = load_json(schema_path)
    resolver = RefResolver.from_schema(schema, store=store)
    return Draft202012Validator(schema, resolver=resolver, format_checker=FormatChecker())


def validate_access_events(store):
    access_events = load_json(EXAMPLES_DIR / "access_event.example.json")
    validator = build_validator("access_event.schema.json", store)

    if not isinstance(access_events, list):
        raise ValidationError("access_event.example.json must be a list of AccessEvent objects.")

    errors = []
    incidents = []
    for index, event in enumerate(access_events, start=1):
        event_errors = sorted(validator.iter_errors(event), key=lambda e: e.path)
        if event_errors:
            errors.append((index, event, event_errors))
        if "care_license" not in event:
            incidents.append(event)

    if errors:
        print("AccessEvent validation errors:")
        for index, event, event_errors in errors:
            event_id = event.get("event_id", f"index {index}")
            print(f"- Event {event_id}:")
            for err in event_errors:
                path = ".".join([str(p) for p in err.path]) or "(root)"
                print(f"  * {path}: {err.message}")
        return False, incidents

    for event in access_events:
        event_id = event.get("event_id", "unknown")
        if "care_license" in event:
            print(f"CARE OK: AccessEvent {event_id}")
        else:
            print(f"INCIDENT: AccessEvent {event_id} missing care_license")

    return True, incidents


def load_repair_cases(store):
    repair_case_data = load_json(EXAMPLES_DIR / "repair_case.example.json")
    validator = build_validator("repair_case.schema.json", store)

    repair_cases = repair_case_data if isinstance(repair_case_data, list) else [repair_case_data]
    errors = []
    for index, repair_case in enumerate(repair_cases, start=1):
        case_errors = sorted(validator.iter_errors(repair_case), key=lambda e: e.path)
        if case_errors:
            errors.append((index, repair_case, case_errors))

    if errors:
        print("RepairCase validation errors:")
        for index, repair_case, case_errors in errors:
            case_id = repair_case.get("case_id", f"index {index}")
            print(f"- RepairCase {case_id}:")
            for err in case_errors:
                path = ".".join([str(p) for p in err.path]) or "(root)"
                print(f"  * {path}: {err.message}")
        return False, []

    print("RepairCase example(s): OK")
    return True, repair_cases


def validate_incident_repairs(incidents, repair_cases):
    if not incidents:
        return True

    repair_lookup = {
        repair_case.get("related_access_event_id"): repair_case for repair_case in repair_cases
    }
    missing_repairs = []
    for event in incidents:
        event_id = event.get("event_id")
        repair_case = repair_lookup.get(event_id)
        if repair_case:
            case_id = repair_case.get("case_id", "unknown")
            print(f"INCIDENT OK: missing Care License -> RepairCase found ({case_id})")
        else:
            missing_repairs.append(event_id)
            print(f"INCIDENT ERROR: missing Care License -> no RepairCase for {event_id}")

    return not missing_repairs


def main():
    store = load_schema_store()
    access_ok, incidents = validate_access_events(store)
    repairs_ok, repair_cases = load_repair_cases(store)
    incident_ok = validate_incident_repairs(incidents, repair_cases)

    if access_ok and repairs_ok and incident_ok:
        print("OK")
    else:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
