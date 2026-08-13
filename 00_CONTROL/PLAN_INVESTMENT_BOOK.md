# 📘 PLAN DEL INVESTMENT BOOK — FASE DE DEMOSTRACIÓN Y ENTREGA

## 13 de agosto de 2026 · **PLAN APROBADO, PENDIENTE DE EJECUTAR**

> **La construcción de cartera está CERRADA.** La arquitectura queda congelada por **D65**.
> **Este documento es el plan de trabajo de los dos días siguientes**, con el índice del
> libro, el reparto y las dependencias.
>
> ⚠️ **Nada de esto está ejecutado todavía. La carpeta del trabajo final NO está creada.**

---

# 0. ESTADO AL CERRAR LA SESIÓN

| | |
|---|---|
| **Arquitectura** | 🔒 **CONGELADA** — D65 |
| **X-Ray de referencia** | ✅ [`XRAY_FINAL_2026-08-13.md`](../02_CARTERA/XRAY_FINAL_2026-08-13.md) |
| **Decisiones registradas** | **D1 → D68** |
| **Carpeta del trabajo final** | ❌ **sin crear** — pendiente de decidir `04_` o `05_` |
| **Coste de la cartera** | 🔴 **≈0,21% ESTIMADO**, pendiente de KIID del PIMCO |

## Composición vigente

```
Motor 44 · Reserva Operativa 3 · Convicción 0-14
Defensivos 12 (Staples 6 + Health 6)
Aceleración 12 (Small Cap 4 + Robeco 4 + Europe Multifactor 4)
Emergentes 7 · Freno 9 (AXA 6 + PIMCO 3)
Activos reales 9 (Oro 7 + Cobre 2) · Asimetría 4        =  100
```

---

# A. ÍNDICE MAESTRO — 27 capítulos + 6 anexos

## PARTE I — MANDATO Y MARCO

| # | Capítulo |
|---|---|
| 1 | **Resumen ejecutivo** *(se escribe el último)* |
| 2 | Mandato, parámetros y denominación |
| 3 | Filosofía de inversión |
| 4 | Objetivos y criterios de éxito — **incluye qué contaría como fracaso** |
| 5 | Restricciones y límites autoimpuestos |

## PARTE II — CONSTRUCCIÓN

| # | Capítulo |
|---|---|
| 6 | Proceso de construcción y método de decisión |
| 7 | Arquitectura modular: el principio rector |
| 8 | **Justificación módulo a módulo** *(9 secciones)* |
| 9 | Selección de vehículos: criterios y evidencia |
| 10 | 🔴 **Costes** — bloqueado |

## PARTE III — LA CAPA ACTIVA

| # | Capítulo |
|---|---|
| 11 | Gestión activa propia vs delegada |
| 12 | El protocolo IDC |
| 13 | Convicción como presupuesto de riesgo |
| 14 | Aportaciones y rebalanceo |
| 15 | La Reserva Operativa |

## PARTE IV — ANÁLISIS

| # | Capítulo |
|---|---|
| 16 | X-Ray: exposición real vs aparente |
| 17 | Métricas de rentabilidad y riesgo |
| 18 | Correlaciones y diversificación efectiva |
| 19 | Mapa de riesgos |
| 20 | 🔴 **Stress test** — bloqueado por D47a |
| 21 | 🔴 **Sobreponderaciones y política de venta** — bloqueado por D47b |
| 22 | 🔴 **Escenarios de implantación** — bloqueado por D53 |

## PARTE V — GOBIERNO Y CIERRE

| # | Capítulo |
|---|---|
| 23 | Benchmark y medición del alfa |
| 24 | Seguimiento, Fecha Cero y cohorte real |
| 25 | Gobernanza |
| 26 | **Límites del modelo y crítica propia** |
| 27 | Conclusiones |

## ANEXOS

**A.** Registro D1-D68 · **B.** Fichas de los 12 vehículos · **C.** X-Ray íntegro ·
**D.** Alternativas descartadas · **E.** Bibliografía · **F.** Glosario

---

# B. MATRIZ CAPÍTULO → EVIDENCIA → FUENTE → RESPONSABLE

| Cap. | Evidencia | Fuente | Responsable |
|---|---|---|---|
| 2 | Mandato, denominación, vocabulario prohibido | `PROTOCOLO §0` · D54 | **Fran** |
| 3-5 | Filosofía, objetivos, restricciones | `ARQUITECTURA_V1 §0-1` | **Fran** |
| 6 | Cronología de decisiones | `ESTADO §3` | **Fran** |
| 7 | Jerarquía por habilidad exigida | `ARQUITECTURA_V1 §1` | **Fran** |
| 8 · Motor | Índice, SPIVA, Bessembinder | `CIFRAS` | **Fran · Cristina R.** |
| 8 · Defensivos | Staples + Salud · **por qué la salud es S&P 500** | X-Ray §4.2 | **Celia Bravo** |
| 8 · Emergentes | Países · por qué salió Japón | X-Ray §4.2 | **Jordi** |
| 8 · Aceleración | Small Cap · Robeco · Multifactor · **D67 ① ②** | X-Ray §5, §7 | **Fran** |
| 8 · Freno | AXA + PIMCO · **D67 ③ ④** | X-Ray §4.4 · D68 | **Grupo** |
| 8 · Activos reales | Oro físico vs ETC de futuros | `CIFRAS` | **Mary M. · Cristina R.** |
| 8 · Asimetría | Bitcoin: tamaño, custodia, desplomes | `CIFRAS` | **Andrea Miguel** |
| 9 | 12 fichas con ISIN, TER, patrimonio, rating | `VEHICULOS_MYINVESTOR` | **Cada responsable** |
| 10 | 🔴 **KIID del PIMCO** + los 11 restantes | X-Ray §6 · D68 | **Grupo** |
| 11-15 | Protocolo completo | `PROTOCOLO_OPERATIVO` | **Fran** |
| 16-18 | Informe Morningstar íntegro | `XRAY_FINAL_2026-08-13` | **Fran** |
| 19 | Mapa de riesgos | X-Ray §4-5 | **Fran** |
| 20 | 🔴 Shocks auditados | `D47a` | **Fran** |
| 21 | 🔴 Bandas de venta | D47b — **no existe** | **Fran** |
| 22 | 🔴 Escenarios | D53 — **no existe** | **Fran** |
| 23-24 | Benchmark, alfa, Fecha Cero | `PROTOCOLO §15-19` | **Fran** |
| 25 | Mayorías, calendario, roles | `REVISIONES_EQUIPO` | **Grupo** |
| 26 | Seis salvedades + tres hallazgos | X-Ray §10-11 · D66 | **Fran** |
| Anexo D | 10 alternativas descartadas | X-Ray §9 | **Fran** |
| Anexo E-F | Bibliografía y glosario | — | **Delegable** |

---

# C. TAREAS DELEGABLES

> ## 🔒 **REGLA DE BLINDAJE**
> **El grupo produce EVIDENCIA y PROSA. Nunca pesos, vehículos ni cifras del X-Ray.**
>
> **Solo lectura para todos:** `ESTADO.md` · `PROTOCOLO_OPERATIVO.md` ·
> `XRAY_FINAL_2026-08-13.md`

| # | Tarea | Quién | h |
|---|---|---|---|
| **T1** | Descargar los **12 KIID/PRIIPs**: TER oficial, divisa, clase | Cada responsable | 2 |
| **T2** | 🔴 **KIID del PIMCO `IE00B84J9L26`** — desbloquea el cap. 10 | **Grupo** | 0,5 |
| **T3** | **Ficha de una carilla** por vehículo *(12)*, plantilla fija | Cada responsable | 6 |
| **T4** | Redactar la **justificación de su módulo** *(cap. 8)* | 6 personas | 8 |
| **T5** | **Bibliografía**: SPIVA, Bessembinder, Asness, Booth & Fama, Vanguard, CNMV | Delegable | 3 |
| **T6** | **Glosario** de 40 términos en lenguaje llano | Delegable | 3 |
| **T7** | **Gráficos** con datos congelados: donut, sectores, correlaciones | Delegable | 4 |
| **T8** | Revisión de estilo y erratas | Delegable | 4 |
| **T9** | Verificar las **seis salvedades** del X-Ray §10 | **Grupo** | 2 |
| **T10** | Formato, portada, índice, numeración | Delegable | 3 |

## 🚫 No delegable nunca

**Cambiar pesos o vehículos · recalcular el X-Ray · cerrar D47a, D47b o D53 ·
escribir los capítulos 1, 26 y 27 · tocar el registro de decisiones.**

---

# D. DEPENDENCIAS

```
LIBRE DESDE YA ─────────────────────────────────────
  T5 · T6 · T7 · T10        sin dependencias
  T1 · T3                   solo necesitan el catálogo
  T4                        necesita T1 y T3 del mismo módulo

CADENA CRÍTICA ─────────────────────────────────────
  T2 (KIID PIMCO) ──→ cap.10 Costes ──→ cap.23 Alfa neto
                                    └─→ comparación Astralis

  D47a ──→ cap.20 Stress ──→ cap.19 Riesgos
                          └─→ cap.27 Conclusiones
  D47b ──→ cap.21
  D53  ──→ cap.22

  caps. 8,16,20,21,22 ──→ cap.26 ──→ cap.27 ──→ cap.1
```

## Los cuatro cuellos de botella

| | Bloquea | Coste |
|---|---|---|
| 🔴 **T2 · KIID del PIMCO** | Caps. 10 y 23 | **30 min — el más barato** |
| 🔴 **D47a** | Caps. 19, 20 y 27 | **El más caro:** 3 shocks sobre el 63% |
| 🟠 **D47b** | Cap. 21 | Media sesión |
| 🟠 **D53** | Cap. 22 | Media sesión |

---

# E. LO QUE PUEDE HACER FRAN EN PARALELO

## 🟢 Trece capítulos desbloqueados — **≈60% del libro**

```
PARTE I completa     2 · 3 · 4 · 5
PARTE II             6 · 7 · 9
PARTE III completa  11 · 12 · 13 · 14 · 15
PARTE IV            16 · 17 · 18
PARTE V             23 · 24 · 25
```

**Todo sale de material cerrado:** `PROTOCOLO_OPERATIVO`, `XRAY_FINAL_2026-08-13`, `ESTADO`.

## 🔴 Cuatro bloqueados · ⚫ Tres al final

**Bloqueados:** 10 · 20 · 21 · 22 — **Al final por definición:** 26 · 27 · 1

---

# 🎯 SECUENCIA RECOMENDADA

| Cuándo | Qué |
|---|---|
| **Primero, 30 min** | **T2 — KIID del PIMCO.** Dos capítulos por medio euro de esfuerzo |
| **Día 1** | Repartir T1, T3, T4, T5, T6. **Fran empieza por la Parte III** |
| **Día 1 tarde** | **D47a** — el cuello de botella caro |
| **Día 2** | D47b y D53, medio día cada uno |
| **Día 2 tarde** | Caps. 26, 27 y 1 |

---

## ⚠️ DECISIÓN PENDIENTE ANTES DE CREAR LA CARPETA

**Ya existe `04_PRESENTACION/`.** Crear `04_TRABAJO_FINAL/` dejaría **dos carpetas con el
mismo número**.

> **Propuesta: `05_TRABAJO_FINAL/`.** Pendiente de confirmación.

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Creación.** Plan completo de la fase de demostración y entrega: índice de 27 capítulos, matriz de evidencia con responsables, 10 tareas delegables con regla de blindaje, grafo de dependencias y reparto de trabajo paralelo. **Nada ejecutado: la carpeta del trabajo final no está creada** |
