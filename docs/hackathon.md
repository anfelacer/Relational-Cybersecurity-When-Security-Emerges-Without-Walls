# Hackathon Context — Techinance Cyberhack 2

🌐 **Bilingual note / Nota bilingüe**  
This document is intentionally written in both **English and Spanish**.  
Language here is not cosmetic: it is part of the security model.  
Este documento está escrito intencionalmente en **inglés y español**.  
El lenguaje no es decorativo: hace parte del modelo de seguridad relacional.

## English

### Challenge summary (Techinance Cyberhack 2)

Techinance Cyberhack 2 invites students to build beginner‑friendly cybersecurity solutions that protect vulnerable populations. The event encourages prototypes that are functional, accessible, and grounded in real-world impact.

**Submission expectations:**
- Functional prototype (code repo, live link, etc.)
- Visual explanation (short video)
- Optional: slides, user testimonials, or roadmap

### How this MVP responds

Relational Cybersecurity offers a conceptual‑technical MVP that reframes security as responsibility when access occurs. It provides:
- A minimal **relational access ledger** (AccessEvent)
- An **Ethical Care License** required for access (CareLicense)
- **Accountability / Repair** flows when care is missing (RepairCase)
- A validator script that demonstrates the full access → care → repair pattern

This is a functional prototype focused on **ethics‑by‑design** and **accountable access** rather than wall‑based security.

### Demo plan (1–2 minutes)

1. Show the README (problem + 5‑step flow).
2. Open JSON examples (care event + incident).
3. Run `python src/validate.py`.
4. Explain how a missing Care License triggers RepairCase.
5. Close with why this model protects vulnerable populations.

Optional: show the CLI tool (`python src/ledger_cli.py`) to generate a live AccessEvent and tension indicator.

See `docs/demo_script.md` for a 90‑second narration aligned with this flow.

## Español

### Resumen del reto (Techinance Cyberhack 2)

Techinance Cyberhack 2 invita a estudiantes a construir soluciones de ciberseguridad para principiantes que protejan poblaciones vulnerables. El evento prioriza prototipos funcionales, accesibles y con impacto real.

**Qué se debe entregar:**
- Prototipo funcional (repo de código, enlace en vivo, etc.)
- Explicación visual (video corto)
- Opcional: presentación, testimonios de usuarios o hoja de ruta

### Cómo responde este MVP

Ciberseguridad Relacional ofrece un MVP conceptual‑técnico que redefine la seguridad como responsabilidad cuando ocurre el acceso. Proporciona:
- Un **registro relacional de acceso** (AccessEvent)
- Una **Licencia Ética del Cuidado** para acceder (CareLicense)
- Flujos de **rendición de cuentas / reparación** cuando falta cuidado (RepairCase)
- Un validador que demuestra el patrón acceso → cuidado → reparación

Es un prototipo funcional centrado en **ética por diseño** y **acceso responsable**, no en muros.

### Plan de demo (1–2 minutos)

1. Mostrar el README (problema + flujo de 5 pasos).
2. Abrir ejemplos JSON (evento con cuidado + incidente).
3. Ejecutar `python src/validate.py`.
4. Explicar cómo la ausencia de licencia activa RepairCase.
5. Cerrar con por qué este modelo protege poblaciones vulnerables.

Opcional: mostrar la CLI (`python src/ledger_cli.py`) para generar un AccessEvent en vivo y el indicador de tensión.

Ver `docs/demo_script.md` para un guion de 90 segundos alineado a este flujo.
