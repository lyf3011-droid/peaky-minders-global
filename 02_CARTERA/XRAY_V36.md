# 🔬 X-RAY v3.6 — RADIOGRAFÍA DE LA CARTERA VIGENTE

## 13 de agosto de 2026 · **Fuente: catálogo MyInvestor + fichas Morningstar de cada vehículo**

> **Objeto:** fotografía exacta de la cartera que se entrega, no de la fase madura ni de la
> composición histórica. **Convicción entra al 0%, que es su peso real hoy.**
>
> ## ⚠️ ESTE X-RAY **NO ESTÁ COMPLETO**. Lea el §1 antes que cualquier cifra.

---

# 1. 🔴 LO QUE ESTE X-RAY **NO** PUEDE DECIR

**Se declaran primero los huecos, porque condicionan todo lo demás.**

## 1.1 Seis métricas pedidas que NO están disponibles

| Métrica | Estado |
|---|---|
| **Beta** | ❌ **No disponible** |
| **Alfa** | ❌ **No disponible** |
| **R²** | ❌ **No disponible** |
| **Tracking error** | ❌ **No disponible** |
| **Information ratio** | ❌ **No disponible** |
| **Ratio de Sharpe** | ❌ **No disponible** |

> **Por qué:** estas seis son métricas *relativas a un índice de referencia*. La fuente de este
> X-Ray devuelve composición, rentabilidad, volatilidad y correlaciones, **pero no calcula
> regresión contra un benchmark**. Las cifras anteriores *(beta 0,74 · alfa 2,42 · R² 88,64)*
> venían del **informe X-Ray de Morningstar**, que se genera manualmente.
>
> ## 🔴 **No se inventa ninguna. Quedan pendientes del informe de Morningstar sobre la v3.6.**

## 1.2 El periodo simulable son **12 meses**, no 3 ni 5 años

```
Periodo efectivo:  21-ago-2025  →  07-ago-2026
Vehículo que lo limita:  iShares Developed World Index clase S  (IE000ZYRH0Q7)
```

**La clase S del Motor es de creación reciente y no tiene serie más larga.** Como el
backtesting se acota al histórico común, **toda la cartera queda limitada a un año**.

> ### 🔴 **Consecuencia grave: la volatilidad, la caída máxima y las correlaciones de este
> ### documento son de UN AÑO. No son comparables con las cifras a 3 y 5 años del X-Ray
> ### anterior.**

## 1.3 La geografía cubre el 68%, y solo el 20% está medido

| | Peso | Origen |
|---|---|---|
| ✅ **Medido** *(dato propio del vehículo)* | **20%** | Staples · Salud · Value · Multifactor |
| 🟡 **Proxy declarado** | **48%** | Motor *(vía iShares Core MSCI World `IE00B4L5Y983`)* · Small Cap *(vía `IE00BF4RFH31`)* |
| ❌ **Sin dato** | **32%** | Emergentes 7 · Oro 7 · Freno 9 · Bitcoin 4 · Reserva 3 · Cobre 2 |

⚠️ **Los dos fondos índice de BlackRock (Motor y Emergentes) no publican desglose regional en
esta fuente.** Para el Motor se usa un ETF que replica el mismo índice como proxy, **y queda
marcado como proxy en todas las tablas**. Para Emergentes no hay sustituto fiable.

## 1.4 El cobre sigue sin vehículo

**El 2% de cobre no tiene ISIN verificado.** Queda fuera de la simulación y los pesos se
renormalizan sobre el 98% restante.

---

# 2. COMPOSICIÓN ANALIZADA

| Bloque | Peso | Vehículo | ISIN |
|---|---|---|---|
| 🚀 **Motor** | **44%** | iShares Developed World Index clase S | `IE000ZYRH0Q7` |
| 💧 Reserva Operativa | 3% | *efectivo remunerado* | — |
| 🎯 **Convicción** | **0%** | *sin desplegar* | — |
| 🌿 Defensivos · consumo | 6% | Xtrackers MSCI World Consumer Staples | `IE00BM67HN09` |
| 🌿 Defensivos · salud | 6% | iShares S&P 500 Health Care | `IE00B43HR379` |
| 🌍 Emergentes | 7% | iShares Emerging Markets Index clase S | `IE000QAZP7L2` |
| ⚓ Freno · monetario | 6% | AXA Trésor Court Terme C | `FR0000447823` |
| ⚓ Freno · bonos | 3% | iShares Global Aggregate 1-5y EUR H | `IE0004ZP1ND3` |
| 🥇 Activos reales · oro | 7% | WisdomTree Core Physical Gold | `JE00BN2CJ301` |
| 🥇 Activos reales · cobre | 2% | 🔴 **sin vehículo** | — |
| ⚡ Aceleración · tamaño | 4% | Vanguard Global Small-Cap Index | `IE00B42W4L06` |
| ⚡ Aceleración · valor | 4% | Xtrackers MSCI World Value | `IE00BL25JM42` |
| ⚡ Aceleración · multifactor | 4% | iShares STOXX Europe Multifactor | `IE00BZ0PKV06` |
| 💥 Asimetría | 4% | 21Shares Bitcoin Core ETP | `CH1199067674` |

⚠️ **En la simulación, la Reserva (3%) y el monetario del Freno (6%) se agregan en el mismo
vehículo (12% con los bonos)** por el límite de diez posiciones de la herramienta. **Es
agregación dentro de la misma función, no una sustitución de activo.**

---

# 3. ASIGNACIÓN DE ACTIVOS — **medido**

| Clase | Peso | Comentario |
|---|---|---|
| 📈 **Renta variable** | **76,2%** | ✅ **Dentro de la banda D5 (75-85%)** |
| 📉 Renta fija | **7,0%** | |
| 💵 Liquidez | **1,9%** | |
| 🟡 **Otros** | **14,8%** | Oro 7,1 + bitcoin 4,1 + «otros» del monetario ≈3,5 |

## 3.1 ✅ El diseño y la medición coinciden

**El diseño dice 75% de renta variable. La medición dice 76,2%.** La diferencia viene de que
los fondos llevan algo de liquidez dentro y de que el cobre está excluido.

> ### **Es la primera vez en el proyecto que el peso de diseño y el peso medido coinciden.**
> En la v3.3 el X-Ray medía **70,68%** frente a un diseño del 72%.

## 3.2 🟡 Un hallazgo menor pero real: el monetario no es efectivo

**El AXA Trésor Court Terme declara: bonos 57,5% · efectivo 13,6% · otros 29,0%.**

**Funcionalmente se comporta como efectivo** —volatilidad a un año del **0,05%**, indicador de
riesgo **1**, liquidación en **el mismo día**—, pero **no es una cuenta corriente**, y ese 29%
de «otros» es lo que infla la fila «Otros» de la cartera.

---

# 4. 🌍 GEOGRAFÍA

| País | Peso en la cartera | Origen |
|---|---|---|
| 🇺🇸 **Estados Unidos** | **45,82%** | 🟡 proxy + ✅ medido |
| 🇯🇵 Japón | 4,07% | |
| 🇬🇧 Reino Unido | 3,29% | |
| 🇨🇭 Suiza | 2,21% | |
| 🇫🇷 Francia | 1,99% | |
| 🇨🇦 Canadá | 1,86% | |
| 🇩🇪 Alemania | 1,63% | |
| 🇦🇺 Australia | 0,85% | |
| 🇳🇱 Países Bajos | 0,49% | |
| 🇮🇹 Italia · 🇪🇸 España · 🇸🇪 Suecia · 🇧🇪 Bélgica | 0,34 · 0,32 · 0,31 · 0,11% | |
| ❌ **Emergentes** | **7%** | **sin desglose** — el fondo declara Taiwán, Corea, China, India y Brasil, sin pesos |

## 4.1 🔴 EL HALLAZGO PRINCIPAL DE ESTE X-RAY

> ## **Estados Unidos pesa el 45,8% de la cartera total — y el 61,1% de toda la renta variable.**

**Y no viene de una decisión de asignar a Estados Unidos.** Viene de sumar cuatro cosas que
nadie eligió por su geografía:

| Vía | Aporta |
|---|---|
| 🚀 El **Motor** *(MSCI World, 71,9% EEUU)* | **31,6 pp** |
| 🌿 La **salud** *(S&P 500 Health Care, 99,7% EEUU)* | **6,0 pp** |
| 🌿 El **consumo defensivo** *(64,8% EEUU)* | **3,9 pp** |
| ⚡ **Small Cap** *(61,5% EEUU)* y **Value** *(46,5% EEUU)* | **4,3 pp** |

> ### **El bloque de salud es el más concentrado geográficamente de toda la cartera: es un
> ### ETF del S&P 500, no un fondo global.** Un 6% de la cartera está en un solo sector de un
> ### solo país.

## 4.2 ✅ El único contrapeso real es el multifactorial europeo

**El iShares STOXX Europe Multifactor no tiene ni un euro en Estados Unidos.** Es el bloque
que se eligió en el experimento controlado del 12 de agosto **precisamente por eso**, y aquí
se ve el efecto: aporta 4 puntos de Europa pura.

---

# 5. 🏭 SECTORES — look-through

| Sector | Peso | Cobertura |
|---|---|---|
| 💻 **Tecnología** | **16,95%** | ✅ completo |
| ⚕️ **Salud** | **11,47%** | ✅ completo |
| 🏦 Servicios financieros | **10,71%** | ✅ completo |
| 🏗️ Industria | 7,39% | ✅ completo |
| 🛒 Consumo defensivo | ≥6,36% | 🟡 parcial |
| 🛍️ Consumo cíclico | 5,81% | ✅ completo |
| 📡 Comunicación | ≥4,58% | 🟡 parcial |
| Materiales · Energía · Inmobiliario · Utilities | ≥1,29% | 🟡 parcial |

⚠️ **«Parcial» significa que algún fondo no publica ese sector en su lista de los ocho
principales.** Los cinco marcados «completo» aparecen en todos los vehículos relevantes y su
cifra es firme.

## 5.1 ✅ La tecnología BAJA de 18,7% a 17,0%

| | v3.3 | **v3.6** | |
|---|---|---|---|
| Tecnología look-through | 18,7% | **16,95%** | ✅ **−1,75 puntos** |

**Y la razón es exactamente la que predecía la arquitectura:** en la v3.3, Convicción llevaba
Alphabet y Meta como posiciones directas, que aportaban **5,0 puntos de tecnología**. **Con
Convicción al 0%, ese solapamiento desaparece.**

> ### 🔴 **Pero ojo: es un efecto temporal.** Si Convicción se llena con las candidatas
> ### previstas, la tecnología vuelve a subir. **El 17,0% es la foto de hoy, no el techo.**

## 5.2 🟡 La salud es el segundo sector, con 11,5%

**Y eso sí es una decisión deliberada** —el bloque Defensivos dedica la mitad a salud—, pero
conviene saber que, sumando lo que ya viene dentro del Motor, **la salud pesa casi tanto como
los financieros de toda la cartera**.

---

# 6. 📊 RIESGO Y RENTABILIDAD — **12 meses**

| | Valor | ⚠️ |
|---|---|---|
| Rentabilidad acumulada del periodo | **+19,18%** | 12 meses |
| **Volatilidad** | **9,37%** | 🔴 **a 1 año** |
| **Caída máxima del periodo** | **−4,83%** | 🔴 **a 1 año — NO es la caída de estrés** |
| Ratio de Sharpe | ❌ no calculado | |

## 6.1 🔴 Advertencia que debe acompañar siempre a estas cifras

> ## **El −4,83% NO es la caída de diseño de la cartera.**
>
> Es la mayor caída observada en **doce meses tranquilos**. La pérdida estimada bajo escenario
> de estrés severo sigue siendo **−43,45%, provisional y pendiente de la auditoría de shocks
> de D47a**. **Son dos cosas distintas y no deben aparecer juntas sin esta nota.**

## 6.2 Volatilidad de cada pieza — donde sí hay serie larga

| Vehículo | Vol. 1a | Vol. 3a | Vol. 5a |
|---|---|---|---|
| 💥 **Bitcoin** | **36,95%** | *sin serie* | *sin serie* |
| 🥇 **Oro** | **27,82%** | 18,85% | 16,79% |
| ⚡ Value | 19,50% | 14,69% | 13,91% |
| ⚕️ Salud | 16,20% | 14,54% | 13,91% |
| ⚡ Small Cap | 12,11% | 14,71% | 15,71% |
| 🌿 Consumo defensivo | 13,64% | 10,46% | 11,11% |
| ⚡ Multifactor Europa | **9,59%** | 10,24% | 12,80% |
| ⚓ **Monetario** | **0,05%** | 0,25% | 0,48% |

> ### 🔴 **El oro es hoy el segundo activo más volátil de la cartera: 27,8% a un año.**
> Tras subir un **64,8% en 2025** y un **26,1% en 2024**, su volatilidad reciente casi duplica
> la de su media de cinco años. **No se está comprando un activo tranquilo.**

---

# 7. 🔗 CORRELACIONES

## 7.1 🔴 Primero, la advertencia estadística

```
Observaciones disponibles:  12
```

> ### **Con doce observaciones, el intervalo de confianza del 95% en torno a una correlación
> ### de cero es aproximadamente ±0,58.**
>
> **Solo los valores por encima de ~0,58 en valor absoluto son distinguibles del ruido.**
> Todo lo que esté por debajo **no se puede interpretar**, y en este documento no se interpreta.

## 7.2 Lo que SÍ es significativo

| Par | Correlación | Lectura |
|---|---|---|
| 🌍 Emergentes ↔ ⚡ Small Cap | **0,86** | 🔴 **Casi el mismo activo** |
| 🌍 Emergentes ↔ ⚡ Value | **0,81** | 🔴 |
| ⚡ Small Cap ↔ ⚡ Multifactor | **0,81** | 🔴 |
| ⚡ Small Cap ↔ ⚡ Value | **0,80** | 🔴 |
| 🚀 Motor ↔ ⚡ Small Cap | **0,78** | |
| 🚀 Motor ↔ ⚡ Value | **0,77** | |
| 🚀 Motor ↔ ⚡ Multifactor | **0,75** | |
| 🌿 Consumo defensivo ↔ 💥 Bitcoin | **−0,68** | ⚠️ **casi con seguridad ruido** |
| 🌿 Consumo defensivo ↔ ⚡ Multifactor | **0,72** | |

## 7.3 🔴 EL SEGUNDO HALLAZGO: Aceleración diversifica menos de lo que parece

> ## **Los tres componentes de Aceleración correlacionan 0,75-0,78 con el Motor, y entre
> ## 0,80 y 0,81 entre ellos.**

**Aceleración pesa un 12% y está construido con tres vehículos distintos para no depender de
uno solo. Medido, los tres se mueven prácticamente juntos y prácticamente con el Motor.**

⚠️ **Esto no invalida el bloque** —su tesis es capturar primas factoriales, no diversificar—
**pero sí obliga a corregir cómo se cuenta**: no se puede decir que Aceleración diversifica la
cartera. **Diversifica el origen de la prima, no el riesgo.**

## 7.4 🔴 EL TERCER HALLAZGO: el oro ya no correlaciona 0,01

| | v3.3 publicado | **v3.6 medido** |
|---|---|---|
| Oro ↔ Motor | **0,01** | **0,35** |
| Oro ↔ Emergentes | *no publicado* | **0,52** |

**Ninguno de los dos supera el umbral de significación con 12 observaciones**, así que **no se
puede afirmar que el oro haya dejado de diversificar**. Pero **tampoco se puede seguir
publicando el 0,01 como si fuera un hecho estable**.

> ### ✅ **Acción: retirar de todos los documentos la afirmación «el oro correlaciona 0,01 con
> ### el Motor» y sustituirla por «históricamente baja, medida recientemente al alza,
> ### pendiente de serie larga».**

## 7.5 ✅ Lo que sí funciona: el Freno

**El monetario correlaciona entre −0,21 y +0,17 con todo lo demás.** Es el único activo de la
cartera que se mueve por su cuenta, y con volatilidad del 0,05% **hace exactamente el trabajo
para el que está.**

---

# 8. 💰 COSTE

| Escenario | Coste ponderado |
|---|---|
| Sin el cobre *(98% de la cartera)* | **0,116%** |
| **Con un cobre al 0,49%** | **0,124%** |
| Con un cobre al 0,55% | 0,125% |

## 8.1 ⚠️ La cifra publicada es optimista

| Dónde | Dice |
|---|---|
| `COMO_ENSENAR_LA_WEB.md` y la web | **0,10%** |
| `CARTERA_HOY.md` | **≈0,11%** |
| **Medido aquí** | **0,12%** |

> ### **Son dos décimas de diferencia sobre una cifra que se enseña en la portada.**
> **Recomendación: publicar «≈0,12%» y decir que incluye una estimación del cobre**, o
> publicar «0,116% sin el cobre, pendiente de cerrarlo». **Cualquiera de las dos es defendible;
> el 0,10% ya no.**

---

# 9. 🔄 COMPARATIVA CONTRA EL X-RAY ANTERIOR

| Métrica | X-Ray v3 *(12-ago)* | **X-Ray v3.6** | Veredicto |
|---|---|---|---|
| **Renta variable** | 70,68% | **76,2%** | 🔄 **Cambio material** |
| **Otros** *(oro+btc)* | 18,75% | **14,8%** | ✅ baja |
| **Tecnología** | 18,7% | **16,95%** | ✅ **mejora −1,75 pp** |
| **EEUU** | *no aislado* | **45,8%** | 🆕 **nuevo dato** |
| **Coste** | ~0,11% | **0,12%** | 🔴 empeora al medirlo |
| Oro ↔ Motor | 0,01 | **0,35** | 🔴 **contradice lo publicado** |
| Bitcoin ↔ Motor | 0,39 | 0,21 | ⚠️ ambos por debajo del umbral |
| **Volatilidad** | 8,87% *(3 años)* | 9,37% *(1 año)* | ⛔ **NO COMPARABLE** |
| **Beta** | 0,74 | ❌ | ⛔ no disponible |
| **Alfa** | 2,42 | ❌ | ⛔ no disponible |
| **Sharpe** | 1,11 | ❌ | ⛔ no disponible |
| **R²** | 88,64 | ❌ | ⛔ no disponible |
| **Tracking error** | 4,07 | ❌ | ⛔ no disponible |
| **Cobertura del informe** | 77,80% | **98%** | ✅ **+20 puntos** |

## 9.1 ✅ Qué ha MEJORADO

| | |
|---|---|
| **La cobertura** | Del **77,80%** al **98%**. **Solo queda fuera el cobre**, que no tiene vehículo |
| **La tecnología** | −1,75 puntos, por la retirada de Alphabet y Meta directas |
| **La coherencia diseño ↔ medición** | El 75% de diseño mide **76,2%**. Antes había 1,3 puntos de desfase |
| **La concentración por empresa** | Sin Convicción desplegada, **no hay ninguna posición directa**. Microsoft ya no llega al 2,99% |

## 9.2 🔴 Qué ha EMPEORADO

| | |
|---|---|
| **La medición del riesgo** | Se pasa de **tres años** de historia a **uno**. **Es un retroceso grande** y lo causa el cambio a la clase S del Motor |
| **El coste real** | 0,12% frente al 0,10-0,11% publicado |
| **Las seis métricas relativas** | Beta, alfa, R², TE, IR y Sharpe **ya no están** |

## 9.3 🆕 Qué es NUEVO

| | |
|---|---|
| 🔴 **EEUU al 45,8%** *(61,1% de la RV)* | **Nunca se había aislado.** Es el riesgo de concentración dominante |
| 🔴 **Aceleración correlaciona 0,75-0,81** | Consigo mismo y con el Motor |
| 🟡 **El oro al 27,8% de volatilidad** | Segundo activo más volátil de la cartera |
| 🟡 **El monetario es 57% bonos** | Funciona como efectivo, pero no lo es |

---

# 10. ⚖️ VEREDICTO

## 10.1 ✅ La arquitectura puede seguir adelante SIN CAMBIOS

**No se ha encontrado ninguna contradicción material de concentración o riesgo que obligue a
reabrir el flujo operativo cerrado.** Concretamente:

| Control | Resultado |
|---|---|
| Renta variable dentro de la banda D5 (75-85%) | ✅ **76,2%** |
| Ningún bloque fuera de su objetivo | ✅ |
| Ninguna posición individual sobre su límite | ✅ *(no hay posiciones directas)* |
| Solapamiento oculto no declarado | ✅ ninguno nuevo |

## 10.2 🔴 Pero tres cosas exigen decisión — **ninguna toca la arquitectura**

| # | | Qué hay que decidir |
|---|---|---|
| **1** | **EEUU al 45,8%** | **No es un error: es el resultado de indexar al mundo.** Hay que decidir si se declara como riesgo asumido o se corrige. **Declararlo es más barato y más honesto que corregirlo** |
| **2** | **El coste publicado** | Cambiar el 0,10% de la portada por **0,12%** |
| **3** | **La correlación del oro** | Retirar el «0,01» de todos los documentos |

## 10.3 ⏳ Y dos cosas siguen sin poder cerrarse

| | |
|---|---|
| **El cobre** | Sigue sin ISIN. **Es el único hueco de la cartera** |
| **Las seis métricas relativas** | Requieren el **informe X-Ray de Morningstar sobre la v3.6**, que hay que generar manualmente con los once vehículos y sus pesos reales |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Creación del X-Ray v3.6.** Cobertura del 98%. Declarados de entrada los seis indicadores no disponibles y la limitación del periodo a 12 meses. Hallazgos principales: **EEUU 45,8%** *(61,1% de la RV)*, **tecnología 16,95%** *(−1,75 pp)*, **Aceleración correlaciona 0,75-0,81 consigo misma y con el Motor**, **oro a 0,35 con el Motor frente al 0,01 publicado** y **coste real 0,12%** |
