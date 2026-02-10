# 90‑Second Demo Script — Relational Cybersecurity

🌐 **Bilingual note / Nota bilingüe**  
This document is intentionally written in both **English and Spanish**.  
Language here is not cosmetic: it is part of the security model.  
Este documento está escrito intencionalmente en **inglés y español**.  
El lenguaje no es decorativo: hace parte del modelo de seguridad relacional.

## Español (guion sugerido)

**0–10s — Apertura (problema + tesis)**  
“La seguridad no nace del muro; el muro crea puntos ciegos.  
En Ciberseguridad Relacional, la seguridad emerge de lo que ocurre cuando hay acceso.”

**10–25s — Flujo en 5 pasos**  
“El flujo es: Acceso → Reconocimiento → Licencia de Cuidado → Acción → Reparación.  
No registramos para vigilar, registramos para cuidar.”

**25–45s — Mostrar ejemplos**  
“Aquí hay dos AccessEvent: uno con licencia y otro sin licencia.  
El evento sin licencia no se oculta: se reconoce como incidente y exige reparación.”

**45–65s — Ejecutar el validador**  
Ejecuta:  
```bash
python src/validate.py
```  
“El validador confirma el evento cuidado y detecta el incidente.  
Si existe RepairCase correspondiente, el sistema sigue siendo ‘OK’.”

**65–80s — (Opcional) CLI en vivo**  
Ejecuta:  
```bash
python src/ledger_cli.py record --actor-role caretaker --resource community_dataset --purpose "Care review of access log" --action read --data-subject community_member_anonymized
python src/ledger_cli.py status
```  
“Aquí vemos un evento en vivo y el indicador de tensión relacional.”

**80–90s — Cierre**  
“Cuando el muro desaparece, la responsabilidad aparece.  
Eso es seguridad relacional: cuidado, trazabilidad y reparación.”

## English (optional)

**0–10s — Opening**  
“Security does not come from walls; walls create blind spots.  
Relational Cybersecurity focuses on what happens when access occurs.”

**10–25s — 5‑step flow**  
“Flow: Access → Recognition → Care License → Action → Repair.  
We log to enable care, not surveillance.”

**25–45s — Examples**  
“Two AccessEvents: one with a Care License, one without.  
Missing care is treated as an incident that requires repair.”

**45–65s — Validator**  
Run:  
```bash
python src/validate.py
```  
“The validator confirms care, detects the incident, and verifies repair.”

**65–80s — (Optional) Live CLI**  
Run:  
```bash
python src/ledger_cli.py record --actor-role caretaker --resource community_dataset --purpose "Care review of access log" --action read --data-subject community_member_anonymized
python src/ledger_cli.py status
```  
“We see a live event and the relational tension indicator.”

**80–90s — Close**  
“When the wall disappears, responsibility appears.  
That is relational security: care, traceability, repair.”
