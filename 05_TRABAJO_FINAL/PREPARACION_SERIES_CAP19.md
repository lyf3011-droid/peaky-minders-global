# 🧮 PREPARACIÓN DE SERIES Y CÁLCULO — CAPÍTULO 19

## 14 de agosto de 2026 · clasificación macro ejecutada según R1-R8 congelado

> **Esto no es el capítulo 19.** Es la ejecución del criterio congelado sobre datos reales.
> **Los resultados macro de este documento están calculados, no estimados**; las
> rentabilidades de los activos **todavía no se han descargado ni analizado** *(R8 exigía
> congelar las reglas primero — ya está hecho)*.

---

# 1. Series descargadas — trazabilidad completa

| Serie | Proveedor original | Identificador | Cobertura descargada | Descarga |
|---|---|---|---|---|
| PIB real EEUU, trimestral, encadenado | **BEA**, vía FRED | `GDPC1` | 1947Q1 → **2026Q2** | 14-ago-2026 |
| IPC EEUU, todos los consumidores urbanos, mensual | **BLS**, vía FRED | `CPIAUCSL` | 1947-01 → 2026 | 14-ago-2026 |

**Transformaciones aplicadas** *(R2, R3, cierre 2.4 de la auditoría)*: PIB → variación
interanual; IPC → media de los tres meses del trimestre → variación interanual.
**Ninguna otra manipulación.**

**Anexo de datos:** [`ANEXO_CLASIFICACION_CAJAS.csv`](ANEXO_CLASIFICACION_CAJAS.csv) — 273
filas con trimestre, ambas variables, ambos umbrales, caja principal, caja alternativa y
marca de proximidad. **Reproducible línea a línea.**

---

# 2. Resultado de la clasificación *(criterio principal: mediana móvil de 40 trimestres)*

**Periodo clasificado: 1958Q1 → 2026Q2 · 273 trimestres.**
*(La v2 del dossier anticipaba el arranque en 1957; el dato real es **1958Q1**, porque la
variación interanual consume 4 trimestres antes de que empiece a contar la ventana de 40.
Corrección registrada.)*

| Caja | Trimestres | % |
|---|---:|---:|
| **1 · Expansión desinflacionaria** | 63 | 23,1% |
| **2 · Recalentamiento** | 63 | 23,1% |
| **3 · Recesión desinflacionaria** | 61 | 22,3% |
| **4 · Estanflación** | **86** | **31,5%** |

**Episodios (R5, ≥2 trimestres consecutivos): 50 en total** — 13 de caja 1, 12 de caja 2,
13 de caja 3, **12 de caja 4**. Además, **33 trimestres aislados**, que conservan su caja
en los cálculos pero no cuentan como episodio *(cierre 2.1 de la auditoría)*.

---

# 3. ✅ Prueba externa de sentido económico: **1973-75 la supera**

| Trimestre | PIB real i.a. | Umbral | IPC i.a. | Umbral | Caja |
|---|---:|---:|---:|---:|:---:|
| 1973Q1 | +7,56 | +4,49 | +4,11 | +3,25 | 2 |
| 1973Q2 | +6,32 | +4,66 | +5,61 | +3,30 | 2 |
| **1973Q3** | +4,77 | +4,89 | +6,84 | +3,42 | **4** *(cerca del umbral)* |
| 1973Q4 | +4,02 | +4,86 | +8,42 | +3,52 | **4** |
| 1974Q1 | +0,64 | +4,64 | +9,91 | +3,55 | **4** |
| 1974Q2 | −0,21 | +4,49 | +10,55 | +3,66 | **4** |
| 1974Q3 | −0,63 | +4,42 | +11,46 | +3,93 | **4** |
| 1974Q4 | −1,95 | +4,19 | +12,05 | +4,12 | **4** |
| 1975Q1 | −2,30 | +3,93 | +11,13 | +4,20 | **4** |
| 1975Q2 | −1,83 | +3,66 | +9,54 | +4,29 | **4** |
| 1975Q3 | +0,80 | +3,29 | +8,68 | +4,40 | **4** |
| 1975Q4 | +2,55 | +3,09 | +7,38 | +4,55 | **4** *(cerca)* |

> **El clasificador sitúa 1973Q3–1975Q4 en la caja 4 de forma continuada (10 trimestres),
> coincidiendo con la descripción histórica habitual del episodio.** El criterio no se
> tocó para conseguirlo: se aplicó tal como quedó congelado.

**Otros episodios candidatos, según el clasificador** *(secuencias completas en el CSV)*:
1979Q2–1981Q2 caja 4 → 1982 entero caja 3 *(la transición Volcker aparece tal como la
describe la historia)* · **2000Q3–2001Q2 caja 4 → 2001Q3-2002 caja 3** · 2007Q4–2008Q3
caja 4 → 2008Q4–2009 caja 3 · 1997–1999 caja 1 sostenida · **2022Q3–2023Q1 caja 4** ·
2020Q2–Q4 caja 3.

---

# 4. Robustez: las dos clasificaciones y su desacuerdo

| | Caja 1 | Caja 2 | Caja 3 | Caja 4 |
|---|---:|---:|---:|---:|
| **Principal** *(mediana 40T)* | 63 | 63 | 61 | **86** |
| **Alternativa** *(media 10 años)* | **83** | 63 | 60 | **67** |

> ### **Desacuerdo: 44 trimestres de 273 = 16,1%**

**El desacuerdo se concentra casi por completo entre las cajas 1 y 4** — es decir, en si un
trimestre tenía «inflación alta» o no. La media se deja arrastrar por los picos
inflacionistas de los setenta y eleva el umbral; la mediana no. **Un 16,1% de desacuerdo
no es despreciable y se publica tal cual**: significa que la frontera entre climas es más
difusa de lo que sugiere una tabla de cuatro casillas.

**Marca informativa de proximidad *(R6)*: 91 trimestres, el 33,3%**, quedan a menos de
0,20 desviaciones típicas de su umbral. **Un tercio de las asignaciones pende de un hilo** —
dato incómodo y publicable, que no altera ninguna clasificación.

---

# 5. 🔴 DISCREPANCIA CON EL PROPIO DOSSIER — para auditoría, no corregida por iniciativa propia

**El dossier (P7 y §7) afirmaba que «la caja 4 tiene esencialmente uno o dos episodios» y
que por eso solo cabía ilustrar, no inferir.**

**El clasificador encuentra 12 episodios de caja 4 y 86 trimestres (31,5%).**

**La afirmación P7 queda contradicha por nuestro propio criterio.** Explicación técnica
—no corrección— del porqué:

> La caja 4 está definida como **crecimiento por debajo de su mediana reciente e inflación
> por encima de la suya**. Eso es **mucho más ancho que el término histórico
> «estanflación»**, que evoca recesión profunda con inflación de dos dígitos. Bajo nuestra
> definición operativa, un trimestre con crecimiento del +2,5% e inflación del +3% puede
> caer en la caja 4 si ambos están al lado equivocado de sus medianas.

**Consecuencias que exigen decisión del equipo, no mía:**

| # | Cuestión abierta | Opciones |
|---|---|---|
| **A** | **¿Se mantiene P7?** | Retirarla *(los datos la desmienten)* · o reformularla como «episodios de estanflación **severa** son escasos», distinguiendo la caja operativa del fenómeno histórico |
| **B** | **¿Debe renombrarse la caja 4?** | «Estanflación» sugiere más de lo que la definición mide. Alternativa neutra: **«crecimiento débil con inflación alta»**, reservando «estanflación» para los episodios severos |
| **C** | **¿Se añade una capa de severidad?** | P. ej. marcar los episodios de caja 4 con PIB interanual negativo *(1974-75, 1980, 1990-91, 2008)* como subgrupo «severo» — **requiere fórmula fija antes de mirar rentabilidades, por R8** |

**No he tocado el dossier ni el capítulo 4.** La discrepancia se publica; la decisión es
del equipo. *(La regla del proyecto es enumerar contradicciones, no corregirlas en
silencio.)*

---

# 6. Verificaciones de integridad — las cuatro exigidas por la auditoría

| # | Prueba | Resultado |
|---|---|---|
| 1 | Suma de trimestres por caja = total clasificado | ✅ `True` *(63+63+61+86 = 273)* |
| 2 | Ningún umbral usa datos posteriores al trimestre | ✅ Por construcción: la ventana es `trims[n−40:n]`, estrictamente anterior |
| 3 | La alternativa usa el mismo código, cambiando un parámetro | ✅ `median` → `mean`, nada más |
| 4 | Resultados guardados con la fecha de descarga | ✅ 14-ago-2026, en el CSV y en este documento |

---

# 7. Lo que queda para poder redactar el capítulo 19

| # | Tarea | Estado |
|---|---|---|
| **1** | **Decisión del equipo sobre A, B y C del §5** | 🔴 **Bloqueante** — afecta a cómo se nombran y agrupan las cajas |
| **2** | Descargar retornos por clase de activo *(Damodaran / Shiller: acciones, bonos, letras)* | ⏳ Siguiente paso técnico |
| **3** | Descargar factores tamaño y valor *(Fama-French)* y precio del oro | ⏳ |
| **4** | Calcular M1-M4 por módulo y caja *(nominal, real, relativo al Motor, consistencia)* | ⏳ Depende de 2 y 3 |
| **5** | Evaluar H1-H7 con la regla de consistencia §9.1 | ⏳ Depende de 4 |
| **6** | Buscar serie sectorial larga para Defensivos *(P2)* | 🟠 Puede resultar imposible — se declararía |
| **7** | Redactar el capítulo 19 | ⛔ **No antes de 1-5** |

> **El capítulo 4 no se ha modificado y no se modificará para hacerlo coincidir con estos
> resultados.** Cualquier corrección al mapa del capítulo 4 saldrá de la evaluación
> completa de H1-H7, se registrará como decisión, y se propagará **después**.

---

## Código

El clasificador es un script de ~90 líneas sin dependencias externas, que va al anexo del
libro junto al CSV *(exigencia R7)*. Reproduce este documento entero con las dos series
públicas y un solo comando.
