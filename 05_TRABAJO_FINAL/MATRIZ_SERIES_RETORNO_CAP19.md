# 🗂️ MATRIZ DE SERIES DE RETORNO — CAPÍTULO 19

## Registrada ANTES de calcular · 14 de agosto de 2026 · descarga del 14-ago-2026

> **Decisiones A/B/C aplicadas *(D89)*. R1-R8 congeladas definitivamente.** Este documento
> fija qué serie representa a cada módulo, con qué límites, **antes de ver ningún
> resultado**.

---

# 1. Nomenclatura descriptiva de las cuatro cajas *(decisión B)*

**Los nombres pasan a describir las variables, no a narrar una época.**

| Caja | Nombre operativo *(vigente)* | Nombre narrativo *(retirado del uso automático)* |
|---|---|---|
| **1** | **Crecimiento fuerte + inflación baja** | ~~Expansión desinflacionaria~~ |
| **2** | **Crecimiento fuerte + inflación alta** | ~~Recalentamiento~~ |
| **3** | **Crecimiento débil + inflación baja** | ~~Recesión desinflacionaria~~ |
| **4** | **Crecimiento débil + inflación alta** | ~~Estanflación~~ |

**«Fuerte» y «débil» significan por encima o por debajo de la mediana móvil de 40
trimestres** — son términos **relativos a la propia historia reciente**, no juicios
absolutos. **«Estanflación», «recesión» o «recalentamiento» solo se usarán para describir
episodios históricos concretos cuando corresponda**, nunca como sinónimo de una caja.

---

# 2. Convenciones de medición — **fijadas aquí, antes de calcular**

R1-R8 gobiernan la **clasificación macro**. El lado de los activos necesita sus propias
convenciones, y se congelan ahora por el mismo principio:

| # | Convención | Decisión |
|---|---|---|
| **C1** | **Sincronía** | El retorno del trimestre *t* se empareja con la caja del trimestre *t*. **Sin desfases.** No se prueban retardos alternativos: introducirlos después de ver resultados sería exactamente lo que R8 prohíbe |
| **C2** | **Agregación** | Los retornos mensuales se componen a trimestre; los trimestres de una misma caja se componen geométricamente y se **anualizan** |
| **C3** | **Real** | Rentabilidad real = deflactada por la **inflación efectiva de los mismos trimestres** *(no una constante)*. `(1+nominal)/(1+inflación)−1` |
| **C4** | **Moneda** | **Todo en dólares.** Un inversor en euros habría obtenido otra cosa; declarado como límite *(P6)*, y la conversión es trabajo del cap. 18 |
| **C5** | **M3** | Comparación frente al Motor **en rentabilidad real**, misma caja, mismos trimestres |
| **C6** | **Trimestres aislados** | Entran en los agregados por caja; **no** cuentan como episodio para M4 *(cierre 2.1)* |
| **C7** | **Sin selección posterior** | Se publican **todas** las series de la matriz, ganen o pierdan. Ninguna se retira después de ver el resultado |

---

# 3. La matriz

| Módulo | Activo / proxy histórico | Serie · identificador | Fuente | Periodo disponible | Moneda | Nominal/real | Limitaciones declaradas |
|---|---|---|---|---|---|---|---|
| 🚀 **Motor** | Mercado de acciones EEUU, ponderado por capitalización, retorno total | `Mkt-RF` + `RF` | **Biblioteca de datos Kenneth French** *(Dartmouth)*, base CRSP 202606 | **1926-07 → 2026-06** | USD | Nominal → se calcula real | No es el All-World: **sobre-representa EEUU**. Sin costes ni fiscalidad. **No es nuestro vehículo**, es el tipo de exposición |
| 🌿 **Defensivos · consumo básico** | Cartera sectorial *Consumer NonDurables* | `NoDur` *(12 Industry Portfolios, value-weighted)* | Kenneth French | **1926-07 → 2026-06** | USD | Nominal → real | Definición sectorial académica ≠ índice MSCI del vehículo real. **Resuelve parcialmente P2** |
| 🌿 **Defensivos · salud** | Cartera sectorial *Healthcare* | `Hlth` *(12 Industry Portfolios)* | Kenneth French | **1926-07 → 2026-06** | USD | Nominal → real | Ídem. La composición del sector salud de 1950 no se parece a la de hoy |
| ⚡ **Aceleración · tamaño** | Media de las tres carteras pequeñas | `SMALL LoBM`,`ME1 BM2`,`SMALL HiBM` *(6 Portfolios 2×3)* | Kenneth French | **1926-07 → 2026-06** | USD | Nominal → real | **Cartera académica, no un fondo**: sin costes, sin límites de liquidez |
| ⚡ **Aceleración · valor** | Media de las dos carteras de alto valor contable | `SMALL HiBM`,`BIG HiBM` | Kenneth French | **1926-07 → 2026-06** | USD | Nominal → real | Ídem. El Robeco es gestión activa, no una cartera de factor |
| ⚓ **Freno · monetario** | Letra del Tesoro a 1 mes | `RF` | Kenneth French *(Ibbotson hasta 2024-05; ICE BofA 1-Month T-Bill después)* | **1926-07 → 2026-06** | USD | Nominal → real | **Buen proxy de los 6 puntos de fondo monetario**; en euros el tipo habría sido otro |
| ⚓ **Freno · renta fija** | — | ⛔ **SIN SERIE** | — | — | — | — | 🔴 **No hay retorno total de bonos largos en las fuentes descargadas.** El módulo se analiza **solo por su pata monetaria**, y se declara. **No se aproxima con rendimientos** — sería inventar retornos |
| 🥇 **Activos Reales · oro** | Precio del oro, fixing PM de Londres | Serie diaria USD | **LBMA** *(fuente primaria oficial)* | **1968-04 → 2026-08** | USD | Nominal → real | ⚠️ **Precio administrado hasta agosto de 1971**: los trimestres anteriores se **excluyen** del análisis del oro |
| 🥇 **Activos Reales · cobre** | — | ⛔ **SIN SERIE** | — | — | — | — | 🔴 Pendiente de fuente pública gratuita con historia larga |
| 🌍 **Emergentes** | — | ⛔ **SIN SERIE** | — | — | — | — | 🔴 **P1 confirmado.** No se sustituye por acciones EEUU: sería falsear el módulo |
| 💥 **Asimetría** | — | ⛔ **NO ANALIZABLE** | — | *(bitcoin existe desde 2009)* | — | — | 🔴 **No se inventa historia anterior a su existencia.** No cubre ningún episodio de los años setenta, ochenta, noventa ni 2008 |
| 💧 **Reserva** | — | ⚪ No aplica | — | — | — | — | Es capacidad operativa, no retorno *(H8)* |

## 3.1 Cobertura efectiva — lo que este análisis puede y no puede decir

| Módulo | ¿Analizable? | Desde |
|---|---|---|
| 🚀 Motor | ✅ Completo | 1958Q1 *(inicio de la clasificación)* |
| 🌿 Defensivos | ✅ Completo *(mejor de lo previsto: P2 se resuelve en gran parte)* | 1958Q1 |
| ⚡ Aceleración | ✅ Completo | 1958Q1 |
| ⚓ Freno | ⚠️ **Parcial — solo la pata monetaria** | 1958Q1 |
| 🥇 Activos Reales | ⚠️ **Parcial — solo oro, y desde 1971Q4** | 1971Q4 |
| 🌍 Emergentes | ❌ **No analizable** | — |
| 💥 Asimetría | ❌ **No analizable** | — |

> **Dos de los siete módulos quedan fuera del análisis histórico y un tercero entra a
> medias.** Eso limita lo que el capítulo 19 puede concluir sobre H7 *(cobertura de las
> cuatro cajas)*, y se dirá con esas palabras: **la cobertura se evalúa sobre los módulos
> con datos, no sobre la cartera entera.**

## 3.2 Las cinco prohibiciones, recordadas

1. **No inventar historia para bitcoin** — no la hay, y no se sustituye.
2. **No presentar la cartera actual como si hubiera existido en 1973** — no existía, ni sus
   productos. Los proxies miden **tipos de exposición**.
3. **Distinguir siempre proxy histórico de vehículo actual** — la conciliación vive en
   `CARTERA_V1_0_FUENTE_DE_VERDAD.md`.
4. **No mezclar nominal y real** — se publican ambos, siempre etiquetados *(C3)*.
5. **No cambiar reglas después de ver qué activo gana cada caja** — R1-R8 y C1-C7 quedan
   congeladas en este documento, con fecha.

---

**Siguiente:** ejecución de M1-M4 → [`RESULTADOS_M1_M4_CAP19.md`](RESULTADOS_M1_M4_CAP19.md).
**El capítulo 19 no se redacta.**
