# 🏛️ PEAKY MINDERS MODULAR ARCHITECTURE v1.0

## Decisión metodológica · 13 de agosto de 2026 · **D75**

> # **Los módulos definen FUNCIONES, no productos.**
>
> **Los pesos actuales son una parametrización específica del mandato
> `Peaky Minders Global 10Y`. No son pesos universales.**

---

# 1. EL PRINCIPIO

**Hasta ahora el proyecto describía nueve bloques como si todos fueran lo mismo.
No lo son.** Siete cumplen una función estructural permanente. Los otros dos son de
naturaleza distinta y mezclarlos oscurece el diseño.

> ## **Siete módulos estructurales · un overlay condicional · una capa de ejecución.**

---

# 2. LOS SIETE MÓDULOS ESTRUCTURALES

**Están siempre. Cambian de peso y de vehículo; no de función.**

| # | Módulo | **Función estructural** |
|---|---|---|
| 1 | 🚀 **MOTOR** | **Capturar el crecimiento empresarial agregado.** Es la fuente principal de rentabilidad y define la beta de la cartera |
| 2 | 🌿 **DEFENSIVOS** | **Reducir la sensibilidad al ciclo** mediante beneficios estables y demanda inelástica |
| 3 | ⚡ **ACELERACIÓN** | **Capturar primas factoriales sistemáticas** distintas de la beta de mercado |
| 4 | 🌍 **EMERGENTES** | **Incorporar crecimiento económico no recogido** por los índices desarrollados |
| 5 | ⚓ **FRENO** | **Estabilizar la cartera y financiar las compras** en las caídas |
| 6 | 🥇 **ACTIVOS REALES** | **Cubrir escenarios de inflación y pérdida de confianza monetaria** |
| 7 | 💥 **ASIMETRÍA** | **Aportar opcionalidad convexa** con pérdida máxima acotada |

## 2.1 Qué significa «función, no producto»

**Cada módulo se define por la pregunta a la que responde, no por el fondo que lo ocupa.**

| ❌ Formulación de producto | ✅ Formulación de función |
|---|---|
| *«El Motor es el iShares Core S&P 500 más el FTSE All-World»* | **«El Motor captura el crecimiento empresarial agregado. En este mandato se implementa con S&P 500 al 22% y FTSE All-World al 22%»** |
| *«Activos Reales es oro y cobre»* | **«Activos Reales cubre inflación y pérdida de confianza monetaria. En este mandato se implementa con oro al 7% y cobre al 2%»** |

> **Consecuencia práctica: cambiar un vehículo NO cambia la arquitectura.**
> **Cambiar una función, SÍ.**

---

# 3. CONVICCIÓN — **ACTIVE OVERLAY CONDICIONAL**

> ## **No es un módulo estructural. Es una capa superpuesta que puede no existir.**

| | |
|---|---|
| **Naturaleza** | Selección directa y discrecional de acciones |
| **Activación** | **Condicional**: solo cuando `precio ≤ IDC` y la tesis está intacta |
| **Peso hoy** | **0%** |
| **Techo** | **14%** — es un **presupuesto de riesgo**, no un objetivo |
| **Puede permanecer en 0% indefinidamente** | ✅ **Sí, y eso no es un fallo** |

## 3.1 Por qué NO es un módulo estructural

| Los siete módulos | Convicción |
|---|---|
| Existen siempre | **Puede no existir nunca** |
| Tienen peso objetivo | **Tiene techo, no objetivo** |
| Se rebalancean hacia su peso | **Nunca entra en el ranking de infraponderación** |
| No exigen habilidad | **Exige habilidad real de valoración** |

**Mientras no está desplegada, su capital permanece en el Motor.** Por eso Motor, Reserva y
Convicción forman el **macrobloque del 47%**.

---

# 4. RESERVA OPERATIVA — **EXECUTION LAYER**

> ## **No es una asignación de activos. Es infraestructura de ejecución.**

| | |
|---|---|
| **Función** | Permitir ejecutar el overlay **sin depender de reembolsos ni de vender el Motor** |
| **Peso** | **hasta 3%** |
| ❌ **No es** | Freno · liquidez estratégica · market timing · predicción de caída |

**Su tamaño no responde a una visión de mercado, sino a una restricción operativa:**
el reembolso de un fondo tarda días y las oportunidades no esperan.

---

# 5. LA ARQUITECTURA, EN UN ESQUEMA

```
┌─────────────────────────────────────────────────────────────┐
│  ACTIVE OVERLAY  ·  condicional  ·  0-14%                   │
│  🎯 CONVICCIÓN — selección directa y discrecional           │
└─────────────────────────────────────────────────────────────┘
                              ▲
                    se financia desde
                              │
┌─────────────────────────────────────────────────────────────┐
│  EXECUTION LAYER  ·  hasta 3%                               │
│  💧 RESERVA OPERATIVA — capacidad de ejecutar sin vender    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  SIETE MÓDULOS ESTRUCTURALES                                │
│                                                             │
│  🚀 MOTOR            crecimiento empresarial agregado       │
│  🌿 DEFENSIVOS       menor sensibilidad al ciclo            │
│  ⚡ ACELERACIÓN      primas factoriales sistemáticas        │
│  🌍 EMERGENTES       crecimiento no recogido por el índice  │
│  ⚓ FRENO            estabilidad y financiación de compras  │
│  🥇 ACTIVOS REALES   inflación y confianza monetaria        │
│  💥 ASIMETRÍA        opcionalidad convexa acotada           │
└─────────────────────────────────────────────────────────────┘
```

---

# 6. PARAMETRIZACIÓN ACTUAL — `PEAKY MINDERS GLOBAL 10Y`

⚠️ **Estos pesos pertenecen a ESTE mandato.** *(100.000 € · 1.000 €/mes · 10 años · perfil
agresivo.)* **No son la arquitectura: son una instancia de la arquitectura.**

| Capa | Componente | **Peso en este mandato** |
|---|---|---|
| **Estructural** | 🚀 Motor | **44%** |
| | 🌿 Defensivos | **12%** |
| | ⚡ Aceleración | **12%** |
| | 🌍 Emergentes | **7%** |
| | ⚓ Freno | **9%** |
| | 🥇 Activos reales | **9%** |
| | 💥 Asimetría | **4%** |
| | **Subtotal estructural** | **97%** |
| **Execution layer** | 💧 Reserva Operativa | **3%** |
| **Active overlay** | 🎯 Convicción | **0%** *(techo 14%)* |
| | **TOTAL** | **100%** |

---

# 7. ESCALABILIDAD A OTROS MANDATOS

> ## **El modelo puede aplicarse a otros mandatos modificando pesos, límites y vehículos
> ## sin alterar necesariamente las siete funciones.**

## 7.1 Qué se modificaría en otro mandato

| Elemento | ¿Cambia? |
|---|---|
| **Las siete funciones** | ❌ **No necesariamente** |
| Los **pesos** de cada módulo | ✅ Sí |
| Los **límites** *(techo del overlay, tamaño de la execution layer, bandas)* | ✅ Sí |
| Los **vehículos** concretos | ✅ Sí |
| La **existencia del overlay** | ✅ Puede eliminarse por completo |

## 7.2 🔴 Lo que este documento NO hace

**No se diseñan otras carteras. No se inventan pesos para otros perfiles.
No se define ninguna parametrización distinta de la actual.**

> **Establecer que el modelo es escalable no es lo mismo que escalarlo.**
> **Lo primero es una propiedad del diseño; lo segundo sería trabajo nuevo y no está hecho.**

---

# 8. QUÉ APORTA ESTA FORMALIZACIÓN AL TRABAJO

| | |
|---|---|
| **1** | **Separa el diseño de la implementación.** Los vehículos pueden cambiar sin que cambie la tesis |
| **2** | **Explica por qué Convicción puede valer 0%** sin que sea un hueco: es un overlay condicional, no un módulo con objetivo |
| **3** | **Explica por qué la Reserva no compite con el Freno**: no es asignación, es infraestructura |
| **4** | **Convierte la cartera en un modelo**, no en una lista de fondos. Es la diferencia entre describir y diseñar |
| **5** | **Hace auditable la arquitectura**: cada módulo responde a una pregunta y se puede comprobar si la responde |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Creación · D75.** Formalización de la arquitectura en **siete módulos estructurales + un active overlay condicional (Convicción) + una execution layer (Reserva Operativa)**. Establecido que **los módulos definen funciones y no productos**, y que **los pesos actuales son la parametrización de `Peaky Minders Global 10Y`, no pesos universales**. Declarada la escalabilidad a otros mandatos **sin diseñar ninguno**. ❌ **Ningún peso ni vehículo modificado** |
