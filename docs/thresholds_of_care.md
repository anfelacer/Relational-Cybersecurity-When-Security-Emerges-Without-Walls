# Thresholds of Care
## Umbrales del Cuidado

> This document clarifies the thresholds of care that make relational security possible.  
> It does not add new technical entities; it describes the ethical ground that already sustains  
> the Care License, RepairCase, and validator behavior in this MVP.

> Este documento aclara los umbrales de cuidado que hacen posible la seguridad relacional.  
> No agrega nuevas entidades técnicas; describe el suelo ético que ya sostiene  
> la Licencia de Cuidado, los RepairCase y el comportamiento del validador en este MVP.

---

## 1. What is a threshold of care  
## 1. Qué es un umbral de cuidado

A threshold of care is the minimal condition that allows access to be recognized as responsible.  
It is not a permission gate; it is an ethical floor beneath the action.

Un umbral de cuidado es la condición mínima que permite reconocer un acceso como responsable.  
No es un portón de permisos; es el piso ético que sostiene la acción.

---

## 2. Three operational thresholds  
## 2. Tres umbrales operativos

### 2.1 Recognition  
### 2.1 Reconocimiento

Access is named and recorded as a relational event.  
No access is “neutral.”

El acceso se nombra y se registra como evento relacional.  
Ningún acceso es “neutral.”

### 2.2 Obligation  
### 2.2 Obligación

The accessing role accepts explicit obligations.  
This is expressed through the Care License.

El rol que accede asume obligaciones explícitas.  
Esto se expresa mediante la Licencia de Cuidado.

### 2.3 Repairability  
### 2.3 Reparabilidad

If care is missing or harm emerges, the system must be able to repair.  
Repair is not optional; it is the continuity of care.

Si el cuidado falta o aparece daño, el sistema debe poder reparar.  
La reparación no es opcional; es la continuidad del cuidado.

---

## 3. Thresholds in this MVP  
## 3. Umbrales en este MVP

In this MVP, thresholds are enforced by design:

- **Recognition** is represented by `AccessEvent`.  
- **Obligation** is represented by `CareLicense`.  
- **Repairability** is represented by `RepairCase` and verified by the validator.

En este MVP, los umbrales se materializan así:

- **Reconocimiento** en `AccessEvent`.  
- **Obligación** en `CareLicense`.  
- **Reparabilidad** en `RepairCase` y verificada por el validador.

---

## 4. Why thresholds matter  
## 4. Por qué importan los umbrales

Thresholds keep the system from collapsing into two extremes:

- total restriction (the wall), or  
- total exposure (false transparency).

They make access possible **without erasing responsibility**.

Los umbrales evitan dos extremos:

- restricción total (el muro), o  
- exposición total (falsa transparencia).

Permiten el acceso **sin borrar la responsabilidad**.

---

## 5. Relation to prior frameworks  
## 5. Relación con marcos previos

The Manifiesto Técnico and PROC are referenced as public, prior frameworks.  
They ground the thresholds conceptually, without adding new mechanics to this MVP.

El Manifiesto Técnico y PROC se reconocen como marcos públicos y previos.  
Sostienen los umbrales a nivel conceptual, sin introducir nueva mecánica en este MVP.
