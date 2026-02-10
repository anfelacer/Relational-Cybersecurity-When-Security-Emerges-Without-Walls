# Relational Cybersecurity — When Security Emerges Without Walls

🌐 **Bilingual note / Nota bilingüe**  
This repository is intentionally written in both **English and Spanish**.  
Language here is not cosmetic: it is part of the security model.  
Este repositorio está escrito intencionalmente en **inglés y español**.  
El lenguaje no es decorativo: hace parte del modelo de seguridad relacional.

## English

Relational Cybersecurity treats access as an unavoidable reality and turns it into an ethical agreement.  
Security does not come from walls; walls create blind spots.  
Security comes from clear recognition of access and responsibility for what happens next.  
Every access is acknowledged as a relational event, not a surveillance log.  
Every access carries a Care License: purpose + obligations.  
When something goes wrong, a Repair Case is created and tracked.  
This MVP is a minimal, technical demo of that idea using JSON Schemas and examples.  
“The wall is not security; the wall creates blind spots. Security is the agreement about what happens when access occurs.”  
Access is not ownership: it is a commitment to care and accountability.  
The record is not surveillance; it is recognition that enables care and repair.  
Security emerges when the wall disappears and the agreement appears.

**Flow (5 steps)**: Access → Recognition → Care License → Action → Accountability/Repair

## Español

La Ciberseguridad Relacional entiende el acceso como una realidad inevitable y lo convierte en un acuerdo ético.  
La seguridad no nace del muro; el muro crea puntos ciegos.  
La seguridad nace del reconocimiento del acceso y de la responsabilidad sobre lo que ocurre después.  
Cada acceso se reconoce como evento relacional, no como vigilancia.  
Cada acceso incluye una Licencia Ética del Cuidado: propósito + obligaciones.  
Si algo falla, se crea y se sigue un Caso de Reparación.  
Este MVP es una demostración técnica mínima usando JSON Schemas y ejemplos.  
“La pared no es seguridad; la pared crea puntos ciegos. La seguridad es el acuerdo sobre qué pasa cuando hay acceso.”  
Acceder no es poseer: es comprometerse a cuidar y responder.  
El registro no vigila; reconoce para habilitar cuidado y reparación.  
La seguridad emerge cuando desaparece el muro y aparece el acuerdo.

**Flujo (5 pasos)**: Acceso → Reconocimiento → Licencia de Cuidado → Acción → Rendición de cuentas/Reparación

## Ethical Care License details

For the full ethical framing of the Care License, see `docs/ethics.md`.  
Para el marco ético completo de la Licencia de Cuidado, ver `docs/ethics.md`.

## Thresholds of Care

This MVP is intentionally minimal: it demonstrates a relational security pattern, not a production system.  
See `docs/thresholds_of_care.md` for the care thresholds that ground the model.

## Foundational texts

* Technical Manifesto: `docs/manifesto.md`
* Manifiesto Intersistémico (versión ampliada): `docs/manifesto_intersistemico.md`
* PROC v1.0 (Programación Relacional Orientada al Cuidado): `docs/proc.md`

## System diagram

See `docs/system_diagram.md` for a single diagram of the access → recognition → care → action → repair flow.

## Hackathon context (Techinance Cyberhack 2)

See `docs/hackathon.md` for the challenge summary, how this MVP responds, and a short demo plan.

## Project status

See `docs/status_and_next_steps.md` for a concise explanation of what is complete and what remains as optional phase 2 work.

## Demo script (90 seconds)

See `docs/demo_script.md` for a 90‑second narration + command sequence for the video demo.

## CLI tool (optional demo)

Spanish-first CLI to generate AccessEvents, RepairCases, and a tension indicator:

```bash
python src/ledger_cli.py record --actor-role caretaker --resource community_dataset --purpose "Care review of access log" --action read --data-subject community_member_anonymized
python src/ledger_cli.py status
python src/ledger_cli.py export
```

## Run the validator

```bash
pip install jsonschema
python src/validate.py
```

> Note: one AccessEvent example intentionally omits the Care License to demonstrate an incident.
> The validator will report the incident, confirm a matching RepairCase, and still print OK.

## Video plan (1–2 min)
1. Show this README and the JSON examples.
2. Run `python src/validate.py`.
3. Point out how an access without a Care License triggers a Repair Case example.
