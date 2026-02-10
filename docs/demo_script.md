# Guion de Video (90 segundos) — Ciberseguridad Relacional

Este guion está pensado para hablar en lenguaje común, con claridad para personas técnicas y no técnicas.

## Versión principal (Español, lenguaje común)

**0–10s — Bienvenida y idea central**  
“Hola, este proyecto muestra una idea simple: la seguridad no depende de esconder datos detrás de muros.  
La seguridad depende de qué pasa cuando alguien accede.”

**10–25s — Flujo en 5 pasos**  
“Trabajamos con este flujo:  
Acceso → Reconocimiento → Licencia de cuidado → Acción → Reparación.  
No registramos para vigilar, registramos para cuidar y responder.”

**25–40s — Mostrar ejemplos JSON**  
“Aquí tenemos dos ejemplos de acceso:  
uno con licencia de cuidado y otro sin licencia.  
Cuando falta la licencia, el sistema lo reconoce como incidente.”

**40–60s — Ejecutar validación**  
“Ahora corro el validador para revisar estructura y coherencia ética.”

```bash
python src/validate.py
```

“Si el incidente tiene su RepairCase asociado, el sistema cierra en OK.  
La idea no es castigar: es garantizar reparación.”

**60–78s — (Opcional) CLI en vivo**  
“También podemos registrar eventos en vivo con la CLI.”

```bash
python src/ledger_cli.py record --actor-role caretaker --resource community_dataset --purpose "Care review of access log" --action read --data-subject community_member_anonymized
python src/ledger_cli.py status
```

“Aquí vemos el registro y el indicador de tensión relacional.”

**78–90s — Cierre**  
“Este MVP propone seguridad como acuerdo de cuidado:  
si hay acceso, hay responsabilidad; si hay daño, hay reparación.”

---

## Versión corta (30 segundos)

“Este MVP muestra que la seguridad no nace del muro, sino de la responsabilidad cuando hay acceso.  
Usamos tres componentes: registro de acceso, licencia ética de cuidado y caso de reparación.  
Si falta licencia, se reconoce incidente y se exige reparación.  
Por eso, la seguridad aquí es cuidado trazable, no vigilancia.”

---

## Optional English summary (for Q&A)

“Relational Cybersecurity treats access as inevitable and makes responsibility explicit.  
Flow: Access → Recognition → Care License → Action → Repair.  
Missing care is treated as an incident, and repair is required for a coherent OK.”
