# Architecture — Relational Cybersecurity MVP

🌐 **Bilingual note / Nota bilingüe**  
This document is intentionally written in both **English and Spanish**.  
Language here is not cosmetic: it is part of the security model.  
Este documento está escrito intencionalmente en **inglés y español**.  
El lenguaje no es decorativo: hace parte del modelo de seguridad relacional.

## English

```
+-------------------------+     +---------------------+
| Access Recognition      |     | Ethical Care License|
| Ledger (AccessEvent)    |<--->| (CareLicense)       |
+-----------+-------------+     +---------+-----------+
            |                               |
            v                               v
        [Action] ------------------> [Accountability]
                                        (RepairCase)
```

### Core data definitions

**AccessEvent**
- A recognition record of an access event (role, resource, purpose, action).
- Includes an anonymized data subject reference.
- May include a Care License; if missing, it is treated as an incident.

**CareLicense**
- A compact ethical license that accompanies access.
- Declares purpose and obligations.

**RepairCase**
- A repair record created when access occurs without a Care License or when harm is detected.
- Tracks responsible role, steps, and status (open → in_progress → closed).

## Español

```
+-------------------------+     +---------------------+
| Registro de Reconocimiento|   | Licencia Ética     |
| de Acceso (AccessEvent) |<--->| del Cuidado        |
+-----------+-------------+     +---------+----------+
            |                               |
            v                               v
        [Acción] -------------------> [Rendición de cuentas]
                                         (RepairCase)
```

### Definiciones de datos

**AccessEvent**
- Registro de reconocimiento de un evento de acceso (rol, recurso, propósito, acción).
- Incluye una referencia anonimizada de la persona o comunidad representada.
- Puede incluir Licencia de Cuidado; si falta, se trata como incidente.

**CareLicense**
- Licencia ética compacta que acompaña el acceso.
- Declara propósito y obligaciones.

**RepairCase**
- Registro de reparación creado cuando hay acceso sin Licencia de Cuidado o cuando se detecta daño.
- Da seguimiento a rol responsable, pasos y estado (open → in_progress → closed).
