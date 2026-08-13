# 🔬 X-RAY v4 FINAL — REFERENCIA VIGENTE

## PEAKY MINDERS GLOBAL 10Y · Informe Morningstar de 13 de agosto de 2026

> # ✅ **ESTE ES EL X-RAY DE REFERENCIA DE LA ARQUITECTURA INICIAL.**
>
> **Sustituye a `XRAY_V1.md` y `XRAY_V36.md`, que quedan como históricos.**
> **Fuente:** informe Morningstar X-Ray™ · benchmark **RV Global Cap. Grande Blend** ·
> datos a **31 de julio de 2026** · 12 posiciones · **cobertura 100% del 97% invertido**.
>
> ⏳ **Pendiente únicamente de:** D47a *(estrés)* · D47b *(sobreponderaciones)* · Convicción.

---

# 1. CÓMO SE LEE ESTE INFORME

## 1.1 🔴 La regla que evita el error más común

> ## **Morningstar expresa países y sectores sobre la PARTE ACCIONARIAL, no sobre el
> ## patrimonio total.**

**La renta variable es el 76,93%. Por tanto:**

```
EEUU 60,78% de las acciones   →   60,78 × 0,7693  =  46,76% del patrimonio
Tecnología 21,42% de acciones →   21,42 × 0,7693  =  16,48% del patrimonio
```

**Ambas cifras son correctas. Dicen cosas distintas.** En todo documento hay que indicar
cuál de las dos se está usando.

## 1.2 El reescalado del 97%

**La Reserva Operativa (3%) es efectivo y no es un vehículo analizable.** Los pesos se
introdujeron reescalados sobre 97 → 100.

| Vehículo | En Morningstar | **Peso real** |
|---|---|---|
| Developed World | 45,36 | **44%** |
| Emerging Markets | 7,22 | **7%** |
| Oro | 7,22 | **7%** |
| Consumer Staples | 6,19 | **6%** |
| Health Care | 6,19 | **6%** |
| AXA Trésor | 6,19 | **6%** |
| Bitcoin | 4,12 | **4%** |
| World Small Cap | 4,12 | **4%** |
| **Robeco BP Global Premium** | 4,12 | **4%** |
| Europe Multifactor | 4,12 | **4%** |
| **PIMCO GIS Income** | 3,09 | **3%** |
| Cobre | 2,06 | **2%** |
| | **100,00** | **97%** |
| 💧 **Reserva Operativa** | *fuera* | **3%** |
| 🎯 **Convicción** | *fuera* | **0%** |
| | | **100%** |

> **Factor de conversión: × 0,97** sobre cualquier peso del informe.
> **Comprobación:** el oro sale al 7,22% → 7,22 × 0,97 = **7,00%**. ✅

---

# 2. ARQUITECTURA CANÓNICA — **CONGELADA**

| Bloque | Componente | Peso |
|---|---|---|
| 🚀 **Motor** | Developed World | **44%** |
| 💧 **Reserva Operativa** | efectivo remunerado | **3%** |
| 🎯 **Convicción** | 0-14%, sin desplegar | **0%** |
| 🌿 **Defensivos** | Staples 6 + Health 6 | **12%** |
| ⚡ **Aceleración** | Small Cap 4 + **Robeco Global Premium 4** + Europe Multifactor 4 | **12%** |
| 🌍 **Emergentes** | | **7%** |
| ⚓ **Freno** | AXA 6 + **PIMCO GIS Income 3** | **9%** |
| 🥇 **Activos reales** | Oro 7 + Cobre 2 | **9%** |
| 💥 **Asimetría** | Bitcoin | **4%** |
| | | **100%** |

> ### 🔒 **No se añaden módulos, fondos ni factores. No se vuelve a probar China,
> ### tecnología, Quality ni otras variantes** salvo contradicción material posterior.

---

# 3. RENTABILIDAD Y RIESGO — **cifras de registro**

## 3.1 Rentabilidad

| Periodo | Cartera | **vs benchmark** |
|---|---|---|
| **3 años anualizado** | **14,14%** | **+1,18** |
| **5 años anualizado** | **10,31%** | **+1,75** |
| 1 año | 14,47% | −2,07 |
| 6 meses | 6,68% | −2,54 |
| Año en curso | 8,68% | −1,81 |

## 3.2 Riesgo

| | **3 años** | **5 años** |
|---|---|---|
| **Volatilidad** | **9,13** | **10,14** |
| Rentabilidad media | 13,70 | 10,36 |
| **Ratio de Sharpe** | **1,19** | **0,83** |
| **Alfa** | **3,04** | **2,90** |
| **Beta** | **0,79** | **0,81** |
| **R²** | **93,22** | **95,10** |
| **Ratio de información** | **0,41** | **0,62** |
| **Tracking error** | **3,30** | **3,21** |

## 3.3 Peores periodos históricos de esta composición

| Ventana | Peor |
|---|---|
| 3 meses | **−15,87%** *(dic-19 → mar-20)* |
| 6 meses | **−11,76%** *(sep-19 → mar-20)* |
| 1 año | **−8,67%** *(dic-21 → dic-22)* |
| 3 años anualizado | −0,65% *(sep-12 → sep-15)* |
| 5 años anualizado | **+1,55%** *(mar-15 → mar-20)* |

> ### 🔴 **Estas cifras NO son el escenario de estrés.** Son el peor tramo del histórico
> ### disponible. **La pérdida bajo estrés severo sigue PENDIENTE en D47a.**

---

# 4. COMPOSICIÓN

## 4.1 Distribución de activos

| Clase | % largo | % corto | **Neto** |
|---|---|---|---|
| **Acciones** | 76,93 | 0,00 | **76,93** |
| Obligaciones | 12,38 | 2,60 | **9,79** |
| **Efectivo** | 24,53 | **26,39** | 🔴 **−1,86** |
| Otro | 15,25 | 0,11 | **15,14** |
| No clasificado | — | — | **0,00** |

### 🔴 El efectivo neto es NEGATIVO

**Es la primera vez que ocurre y hay que saber por qué:** el **PIMCO GIS Income** usa
derivados y repos de forma intensiva. Sus fondos hermanos declaran posiciones de efectivo
de **−9%** a **−103%** sobre su propio patrimonio.

> **No es un error del informe ni un apalancamiento nuestro.** Es que un fondo de renta fija
> activa mantiene exposición sintética. **Pero debe declararse**, porque la cartera aparenta
> tener menos liquidez de la que tiene.

## 4.2 Geografía — **% sobre acciones**

| Región | % acciones | **% patrimonio** |
|---|---|---|
| 🌎 **América** | **64,01** | **49,24** |
| 🇺🇸 *Estados Unidos* | **60,78** | **46,76** |
| 🇨🇦 *Canadá* | 2,49 | 1,92 |
| 🌍 **Europa** | **21,54** | **16,57** |
| *Occidental euro* | 10,82 | 8,32 |
| *Occidental no euro* | 4,99 | 3,84 |
| 🇬🇧 *Reino Unido* | 4,67 | 3,59 |
| 🌏 **Asia** | **14,45** | **11,12** |
| 🇯🇵 *Japón* | 4,57 | 3,52 |
| *Cuatro tigres* | 5,42 | 4,17 |

**Diez mayores países:** EEUU 60,78 · R. Unido 4,67 · Japón 4,57 · Francia 3,18 ·
Suiza 3,15 · Canadá 2,49 · Taiwán 2,44 · Corea 2,23 · Alemania 2,13 · China 1,87.

## 4.3 Sectores — **% sobre acciones**

| Sector | % acciones | **% patrimonio** |
|---|---|---|
| 💻 **Tecnología** | **21,42** | **16,48** |
| ⚕️ **Salud** | **15,97** | **12,29** |
| 🏦 **Financieros** | **14,90** | **11,46** |
| 🛒 **Consumo defensivo** | **12,34** | **9,49** |
| 🏗️ Industria | 10,00 | 7,69 |
| 🛍️ Consumo cíclico | 7,60 | 5,85 |
| 📡 Comunicación | 6,27 | 4,82 |
| ⛽ Energía | 4,04 | 3,11 |
| ⛏️ Materiales | 3,45 | 2,65 |
| 💡 Servicios públicos | 2,30 | 1,77 |
| 🏢 Inmobiliario | 1,69 | 1,30 |

**Supersectores:** Sensible al ciclo **41,74** · Defensivo **30,62** · Cíclico **27,65**.

## 4.4 Estilo

| Acciones | | Renta fija | |
|---|---|---|---|
| Precio/Valor contable | **3,11** | **Duración efectiva** | **4,46** |
| Precio/Beneficio | **17,58** | Vencimiento efectivo | 6,63 |
| Precio/Cashflow | **12,12** | **Calidad crediticia media** | **BBB** |

### 🟡 La renta fija cambia de naturaleza

| | X-Ray v4 anterior | **v4 FINAL** |
|---|---|---|
| Duración efectiva | **0,01** | **4,46** |
| Calidad crediticia | BB | **BBB** |

**Antes el Freno era efectivo puro. Ahora tiene duración real**, porque el PIMCO GIS Income
no es un fondo de vencimiento corto. **La calidad crediticia mejora a BBB**, lo que cierra
el pendiente que arrastrábamos sobre la «BB».

⚠️ **Consecuencia para la tesis del Freno:** un activo con duración 4,46 **sí pierde valor si
suben los tipos**. El Freno ya no es solo munición estable.

## 4.5 Las diez mayores exposiciones subyacentes

| % | Nombre | Tipo |
|---|---|---|
| **7,22** | **Oro** | Materia prima |
| **2,40** | **NVIDIA** | Acción |
| **2,11** | **Apple** | Acción |
| **2,06** | **Cobre** *(TRS Bloomberg Copper Sub EUR Hedged)* | Derivado |
| **1,48** | **Microsoft** | Acción |
| **1,40** | **Eli Lilly** | Acción |
| **1,13** | **Amazon** | Acción |
| **1,05** | **TSMC** | Acción |
| 0,97 | Johnson & Johnson | Acción |
| 0,97 | Walmart | Acción |

> ### ✅ **Ninguna empresa individual supera el 2,40%.** Sin Convicción desplegada,
> ### **Microsoft se queda en 1,48%**, muy por debajo del límite del 2% de compra directa
> ### *(que se sumaría a esta cifra, no la sustituiría — D52)*.

---

# 5. 🔗 CORRELACIONES — 3 años

**Orden del informe:** 1 Motor · 2 Emergentes · 3 Oro · 4 Staples · 5 Health · 6 AXA ·
7 Bitcoin · 8 Small Cap · 9 Robeco · 10 Multifactor.
*(PIMCO y cobre no entran en la matriz: son las posiciones 11 y 12.)*

## 5.1 Las que importan

| Par | | Lectura |
|---|---|---|
| 🔴 **Robeco ↔ Multifactor** | **0,91** | **La más alta de la matriz — y las dos están en Aceleración** |
| 🔴 Motor ↔ Small Cap | **0,85** | |
| 🔴 Robeco ↔ Small Cap | **0,79** | |
| 🔴 **Motor ↔ Robeco** | **0,74** | |
| Motor ↔ Multifactor | 0,70 | |
| Small Cap ↔ Multifactor | 0,70 | |
| Motor ↔ Emergentes | 0,64 | |
| Motor ↔ Bitcoin | **0,39** | Diversifica, **pero no es independiente** |
| Motor ↔ AXA | **0,05** | ✅ El Freno hace su trabajo |
| ✅ **Motor ↔ Oro** | **0,01** | **El mejor diversificador de la cartera, medido** |

## 5.2 🔴 Hallazgo: Aceleración es más homogénea de lo que aparenta

> ## **Sus tres componentes correlacionan entre 0,70 y 0,91, y entre 0,74 y 0,85 con el Motor.**

**El bloque tiene tres vehículos para no depender de uno solo. Medido a tres años, se mueven
casi juntos.**

⚠️ **No invalida el bloque** —su función es capturar primas factoriales, no diversificar—
**pero obliga a decirlo así: Aceleración diversifica el ORIGEN de la prima, no el riesgo.**

---

# 6. 💰 COSTE — 🔴 **CAMBIA DE FORMA MATERIAL**

## 6.1 El cálculo

| Bloque | Peso | TER | Aporta |
|---|---|---|---|
| Motor | 44% | 0,06% | 2,64 |
| Reserva Operativa | 3% | 0,06% | 0,18 |
| Staples | 6% | 0,25% | 1,50 |
| Health Care | 6% | 0,15% | 0,90 |
| Emergentes | 7% | 0,16% | 1,12 |
| AXA monetario | 6% | 0,06% | 0,36 |
| **PIMCO GIS Income** | **3%** | 🔴 **≈1,45%** | **≈4,35** |
| Oro | 7% | 0,12% | 0,84 |
| Cobre | 2% | 0,49% | 0,98 |
| Small Cap | 4% | 0,30% | 1,20 |
| **Robeco BP Global Premium** | **4%** | 🔴 **1,46%** | **5,84** |
| Europe Multifactor | 4% | 0,25% | 1,00 |
| Bitcoin | 4% | 0,10% | 0,40 |
| | **100%** | | **≈21,31** |

> ## 🔴 **Coste ponderado ≈ 0,21% anual.** *(era 0,12%)*

## 6.2 Qué lo provoca

| | |
|---|---|
| **Robeco sustituye al Xtrackers Value** | 4% pasa de **0,25%** a **1,46%** → **+4,84 pb** |
| **PIMCO sustituye a los bonos iShares** | 3% pasa de **0,08%** a **≈1,45%** → **+4,11 pb** |
| **Los dos cambios juntos** | **+8,95 pb, casi duplican el coste de la cartera** |

## 6.3 En euros, sobre 100.000 €

| | Al año |
|---|---|
| Coste anterior *(0,12%)* | **124 €** |
| **Coste actual (≈0,21%)** | **≈213 €** |
| **Diferencia** | **≈89 €/año** |

## 6.4 🔴 PENDIENTE DE VERIFICACIÓN

**El TER del Robeco (1,46%) está verificado en el catálogo** *(clase D, `LU0951559797`)*.

⚠️ **El del PIMCO GIS Income E EUR Hedged Acc NO.** La clase concreta no aparece en el
catálogo consultado. **Las clases E hermanas de PIMCO están entre 1,39% y 1,69%**, y se ha
usado **1,45%** como estimación central. **La cifra final del coste queda pendiente de
verificar ese TER.**

## 6.5 🟠 Qué documentos hay que corregir

**Todo el relato de coste del proyecto está construido sobre «0,10%».** Con la arquitectura
final **eso ya no es cierto** y hay que decirlo antes de la entrega:

| Frase actual | Debe pasar a |
|---|---|
| *«la cartera entera cuesta un 0,10% al año»* | **«≈0,21%»** |
| *«más de la mitad de la cartera cuesta 0,10%»* | **Sigue siendo cierto del núcleo indexado, pero hay que separar núcleo y gestión delegada** |
| **La comparación con la cartera de Astralis** *(1,68% ponderado)* | **Sigue siendo favorable —0,21% frente a 1,68%— pero la cifra cambia y el argumento debe rehacerse con el número correcto** |

---

# 7. 🔄 CAMBIO METODOLÓGICO — gestión activa delegada

## 7.1 La frase que queda derogada

> ❌ ~~*«Convicción es la única gestión activa de la cartera.»*~~

## 7.2 La formulación vigente

> ## ✅ **«Convicción es la única capa de selección directa y discrecional de acciones.
> ## Determinados módulos pueden utilizar gestión activa delegada cuando su función esté
> ## previamente delimitada y justificada.»**

## 7.3 Dónde hay gestión activa delegada, y con qué mandato

| Módulo | Vehículo | Función delimitada |
|---|---|---|
| ⚡ **Aceleración** | **Robeco BP Global Premium Equities** | Prima de **valor** global, con selección delegada. Categoría Morningstar: *RV Global Cap. Grande Value*. 3★ · vol. 5a **12,02%** · 8.833 M€ |
| ⚓ **Freno** | **PIMCO GIS Income** | Renta fija **multisectorial** con gestión activa de duración y crédito. 3★ |

**Distinción que hay que mantener siempre:**

| | Quién decide | Dónde |
|---|---|---|
| **Selección directa discrecional** | **Nosotros**, empresa a empresa, con IDC | 🎯 **Solo Convicción** |
| **Gestión activa delegada** | **Un gestor externo**, dentro de un mandato acotado | ⚡ Aceleración · ⚓ Freno |
| **Réplica sistemática** | **Nadie: un índice** | El resto |

---

# 8. 📉 QUÉ HA CAMBIADO FRENTE AL X-RAY ANTERIOR

| | v4 *(12-ago, 9 posiciones)* | **v4 FINAL** | |
|---|---|---|---|
| Posiciones | 9 | **12** | ✅ |
| Cobertura | 100% de una estructura vieja | **100% del 97%** | ✅ |
| **Rentabilidad 3a** | 13,29 | **14,14** | ✅ **+0,85** |
| **Rentabilidad 5a** | 9,88 | **10,31** | ✅ +0,43 |
| **Alfa 3a** | 2,69 | **3,04** | ✅ +0,35 |
| **Sharpe 3a** | 1,14 | **1,19** | ✅ |
| **Ratio de información 3a** | 0,13 | **0,41** | ✅ **×3** |
| **Tracking error 3a** | 3,95 | **3,30** | ✅ baja |
| **Volatilidad 3a** | 8,79 | **9,13** | 🔴 sube |
| **Beta 3a** | 0,75 | **0,79** | 🔴 sube |
| **R² 5a** | 92,39 | **95,10** | 🔴 más dependiente del índice |
| Acciones | 72,17% | **76,93%** | 🔄 |
| Efectivo neto | +2,15% | **−1,86%** | 🔴 |
| Duración renta fija | 0,01 | **4,46** | 🔄 |
| **Coste** | ~0,12% | **≈0,21%** | 🔴 |

## 8.1 Lectura honesta

> **La cartera renta más y con mejor alfa, información y Sharpe. Pero es más volátil, tiene
> más beta, se parece más al índice y cuesta casi el doble.**
>
> **Ninguna de las dos mitades de esa frase puede omitirse en la entrega.**

---

# 9. 🗄️ TRAZABILIDAD — alternativas descartadas

**Se conservan como evidencia de sensibilidad del proceso, no como opciones abiertas.**

| Alternativa | Cuándo | Por qué se descartó | Dónde vive |
|---|---|---|---|
| **iShares World Quality** | 12 ago | **Correlación 0,96 con el Motor.** Al retirarlo mejoraron cinco métricas de seis | `XRAY_V1.md §6` |
| **Bloque de tecnología** | 10 ago | El look-through reveló **18,7% ya dentro** sin comprarlo | `CARTERA_DEFINITIVA` |
| **China** | — | Variante probada y descartada | `XRAY_V1.md` |
| **Japón** *(4%)* | 11 ago | Ya cubierto por Emergentes; el 4% pasó a Aceleración | `ESTADO` D-serie |
| **Xtrackers MSCI World Value** `IE00BL25JM42` | 13 ago | **Componente canónico anterior de Aceleración.** Sustituido por el Robeco | **Este documento** |
| **iShares Global Aggregate 1-5a** `IE0004ZP1ND3` | 13 ago | **Componente canónico anterior del Freno.** Sustituido por el PIMCO | **Este documento** |
| **RobecoSAM Smart Energy** | 11 ago | 52,76% tecnología, 0,00% materiales | `CIFRAS_MAESTRAS` |
| **Janus Henderson salud** | 11 ago | Clase comprable al **2,38%**, por debajo del ETF indexado | `CIFRAS_MAESTRAS` |
| **VanEck Gold Miners** `IE00BQQP9F84` | 11 ago | **Disponible**, descartado **por diseño**: vol. 31,65% frente al 16,79% del oro físico | `CIFRAS_MAESTRAS` |
| **USA Small Value** `IE00BSPLC413` | 13 ago | Nunca perteneció a la v3.6 | **Este documento** |

> ### 🔒 **No se vuelven a probar** salvo que aparezca una contradicción material posterior.

---

# 10. ⚠️ SALVEDADES DEL INFORME

| # | | |
|---|---|---|
| 1 | **El oro analizado es `JE00B1VS3770`** *(0,39%)*, no nuestro **Core `JE00BN2CJ301`** *(0,12%)* | **Mismo oro físico**, distinta clase. No afecta al look-through; **sí al coste**, ya corregido en §6 |
| 2 | **El cobre analizado es la clase EUR Daily Hedged** | La canónica es `GB00B15KXQ89`. **La cobertura de divisa cambia el comportamiento** |
| 3 | **Datos del cobre a 31-oct-2025** | **Nueve meses de antigüedad.** Es el dato más viejo del informe |
| 4 | **El Small Cap analizado es el SPDR**, no el Vanguard `IE00B42W4L06` | **Mismo índice MSCI World Small Cap.** Look-through equivalente |
| 5 | **El Robeco analizado es la clase D EUR**; el catálogo verifica la **D USD** `LU0951559797` | Mismo fondo, misma cartera |
| 6 | **Motor y Emergentes en clase D**, no en la clase S contratada | **Mismos fondos, mismos índices.** La clase S no está en la base de Morningstar |

**Ninguna de las seis altera la composición económica analizada. Las seis deben aparecer
declaradas en la entrega.**

---

# 11. ⏳ LO QUE ESTE X-RAY NO RESUELVE

| # | | Estado |
|---|---|---|
| 1 | **D47a** — pérdida bajo estrés severo | 🔴 **PENDIENTE.** Los shocks heredados siguen sin auditar |
| 2 | **D47b** — bandas de sobreponderación | ⏳ **ABIERTO** |
| 3 | **D53** — escenarios de despliegue de Convicción | ⏳ **ABIERTO** |
| 4 | **TER del PIMCO GIS Income** | 🔴 **SIN VERIFICAR** — el coste de 0,21% depende de él |
| 5 | Fichas de las empresas de Convicción | ⏳ |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Creación. X-Ray v4 FINAL establecido como referencia vigente.** 12 posiciones, cobertura del 100% del 97% invertido. Entran **Robeco BP Global Premium** *(Aceleración)* y **PIMCO GIS Income** *(Freno)* como **gestión activa delegada**. Registradas las 21 cifras de rentabilidad y riesgo. **Hallazgos materiales: coste ≈0,21% (era 0,12%), efectivo neto −1,86%, duración de renta fija 0,01 → 4,46, y correlación Robeco ↔ Multifactor de 0,91 dentro de Aceleración.** `XRAY_V1.md` y `XRAY_V36.md` pasan a históricos |
