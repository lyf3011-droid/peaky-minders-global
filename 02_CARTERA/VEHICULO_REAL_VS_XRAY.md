# 🔍 VEHÍCULO REAL ↔ VEHÍCULO DEL X-RAY

## Tabla de conciliación · 13 de agosto de 2026

> **Para qué sirve:** el informe Morningstar **no siempre usa exactamente el instrumento
> definitivo de la arquitectura.** Esta tabla dice, posición por posición, **si lo que se
> analizó es el vehículo real o un sustituto**, y **qué diferencia introduce**.
>
> 🔴 **Sin esta tabla, cualquier cifra del X-Ray es atacable.** Con ella, es defendible.

---

# 1. LA TABLA

| Bloque | **Vehículo REAL** *(arquitectura)* | **Vehículo del X-Ray** | Estado |
|---|---|---|---|
| 🚀 **Motor · tilt USA** | iShares Core S&P 500 · `IE00B5BMR087` | iShares Core S&P 500 UCITS ETF USD (Acc) | ✅ **IDÉNTICO** |
| 🚀 **Motor · ancla global** | Vanguard FTSE All-World · `IE00BK5BQT80` | Vanguard FTSE All-World UCITS ETF USD Acc | ✅ **IDÉNTICO** |
| 💧 **Reserva Operativa** | Efectivo remunerado | ❌ **No representado** | 🔴 **FUERA DEL INFORME** |
| 🌿 **Defensivos · consumo** | Xtrackers World Consumer Staples · `IE00BM67HN09` | El mismo | ✅ **IDÉNTICO** |
| 🌿 **Defensivos · salud** | iShares S&P 500 Health Care · `IE00B43HR379` | El mismo | ✅ **IDÉNTICO** |
| ⚡ **Aceleración · tamaño** | 🔴 **CONTRADICCIÓN ABIERTA** *(ver §2.1)* | SPDR MSCI World Small Cap · `IE00BCBJG560` | 🔴 **A RESOLVER** |
| ⚡ **Aceleración · valor** | Robeco BP Global Premium **D Acc EUR** · `LU0203975437` | Robeco BP Global Premium Equities D EUR | ✅ **IDÉNTICO** |
| ⚡ **Aceleración · multifactor** | iShares STOXX Europe Multifactor · `IE00BZ0PKV06` | El mismo | ✅ **IDÉNTICO** |
| 🌍 **Emergentes** | iShares Emerging Markets Index **clase S** · `IE000QAZP7L2` | iShares EM Index **clase D** · `IE00BYWYCC39` | 🟡 **PROXY** *(§2.2)* |
| ⚓ **Freno · monetario** | AXA Trésor Court Terme C · `FR0000447823` | El mismo | ✅ **IDÉNTICO** |
| ⚓ **Freno · renta fija** | PIMCO GIS Income E EUR (H) Acc · `IE00B84J9L26` | El mismo | ✅ **IDÉNTICO** |
| 🥇 **Activos reales · oro** | WisdomTree **Core** Physical Gold · `JE00BN2CJ301` | WisdomTree Physical Gold · **`JE00B1VS3770`** | 🟡 **PROXY** *(§2.3)* |
| 🥇 **Activos reales · cobre** | WisdomTree Copper · `GB00B15KXQ89` **sin cubrir** | WisdomTree Copper · **EUR Daily Hedged** | 🔴 **DISTINTO** *(§2.4)* |
| 💥 **Asimetría** | 21Shares Bitcoin Core ETP · `CH1199067674` | El mismo | ✅ **IDÉNTICO** |

## Recuento

| | Posiciones |
|---|---|
| ✅ **Idénticas** | **8** |
| 🟡 Proxy de bajo impacto | **2** |
| 🔴 **Requieren advertencia expresa** | **2** |
| ❌ Fuera del informe | **1** |

---

# 2. LOS CUATRO CASOS QUE HAY QUE EXPLICAR

## 2.1 🔴 Aceleración · tamaño — **contradicción abierta, no resuelta**

| Documento | Vehículo | TER |
|---|---|---|
| `CARTERA_HOY.md` y `CIFRAS_MAESTRAS.md` | **Vanguard Global Small-Cap Index** `IE00B42W4L06` | **0,30%** |
| **X-Ray oficial** y la ficha de vehículos | **SPDR MSCI World Small Cap** `IE00BCBJG560` | **0,45%** |

**Los dos replican el MSCI World Small Cap**, así que el look-through de geografía y sectores
es equivalente. **Pero no son el mismo producto y no cuestan lo mismo.**

| | Vanguard `IE00B42W4L06` | **SPDR `IE00BCBJG560`** |
|---|---|---|
| Tipo | Fondo indexado | **ETF** |
| TER | **0,30%** | **0,45%** |
| Patrimonio | 7.047 M€ | 1.783 M€ |
| Posiciones | — | **3.623** |
| EEUU | — | 62,73% |
| ⚠️ Fiscalidad | **Traspasable sin tributar** | **No traspasable** |

> ### 🔴 **NO se resuelve aquí porque cambiaría un vehículo, y la instrucción es no tocar
> ### ninguno.** **Requiere decisión del equipo.**
>
> ⚠️ **Y no es menor: la diferencia no es solo de 15 puntos básicos de coste. Es que uno
> es traspasable y el otro no**, lo cual afecta al rebalanceo a diez años.

## 2.2 🟡 Emergentes — clase S vs clase D

**Mismo fondo, mismo índice, misma cartera. Solo cambia la clase.** La clase S contratada
**no está en la base de Morningstar**; la D sí.

✅ **Impacto en el look-through: ninguno.** ⚠️ **Impacto en el coste mostrado: sí** — hay que
usar el TER de la clase S *(0,16%)*, no el de la D.

## 2.3 🟡 Oro — Core vs clase estándar

| | Real | X-Ray |
|---|---|---|
| Producto | WisdomTree **Core** Physical Gold | WisdomTree Physical Gold |
| ISIN | `JE00BN2CJ301` | `JE00B1VS3770` |
| Coste | **0,12%** | **0,39%** |

**Es el mismo oro físico**, con custodio y barras LBMA en ambos casos.

✅ **Impacto en composición: ninguno** — el oro entra como materia prima sin look-through.
🔴 **Impacto en coste: 27 puntos básicos sobre el 7%**. **El cálculo de costes usa el Core.**

## 2.4 🔴 Cobre — **cubierto vs sin cubrir: SÍ cambia el comportamiento**

| | Real | X-Ray |
|---|---|---|
| Producto | WisdomTree Copper | WisdomTree Copper **EUR Daily Hedged** |
| ISIN | `GB00B15KXQ89` | *clase cubierta* |
| Divisa | **Sin cubrir** | **Cubierto a euro diariamente** |

> ### 🔴 **Éste es el único caso donde el sustituto NO es equivalente.**
>
> **La cobertura de divisa sobre una materia prima cambia el resultado de forma material:**
> el precio del cobre cotiza en dólares, y cubrir el dólar **elimina el componente de divisa
> de la rentabilidad y añade el coste de la cobertura** *(aproximadamente el diferencial de
> tipos a corto plazo)*.
>
> ⚠️ **Además, es el dato más antiguo del informe: cartera a 31-oct-2025**, nueve meses.

**Consecuencia:** las cifras de rentabilidad y volatilidad del cobre en el X-Ray
**corresponden a un producto con distinto perfil de divisa que el que llevamos.**
**Debe decirse en el capítulo de Activos Reales.**

## 2.5 ❌ Reserva Operativa — fuera por diseño

**El 3% es efectivo y no es un vehículo analizable.** El informe se ejecuta sobre el
**97%** reescalado, con **factor de conversión × 0,97**.

✅ **No es una omisión: es una decisión metodológica declarada.**

---

# 3. QUÉ HAY QUE ESCRIBIR EN EL INVESTMENT BOOK

> *«El informe X-Ray se ejecuta sobre el 97% invertido. De las trece posiciones, **ocho se
> analizan con el instrumento exactamente definitivo**. Dos utilizan una clase distinta del
> mismo fondo, sin efecto sobre la composición y con efecto solo sobre el coste mostrado,
> que se corrige usando el TER de la clase contratada. **Una —el cobre— se analiza con una
> clase cubierta a euro mientras la posición real no lo está, lo que sí altera su perfil de
> rentabilidad y volatilidad y queda advertido expresamente.** El vehículo del bloque de
> pequeña capitalización presenta una discrepancia documental abierta entre dos productos
> del mismo índice, pendiente de resolución por el equipo.»*

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Creación.** Conciliación de las trece posiciones: 8 idénticas, 2 proxy de bajo impacto, **2 con advertencia expresa** *(cobre por cobertura de divisa, small cap por contradicción documental)* y 1 fuera por diseño *(Reserva)*. **Ningún vehículo modificado.** |
