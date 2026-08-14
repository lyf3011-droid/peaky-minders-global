# 🗝️ CARTERA v1.0 — FUENTE ÚNICA DE VERDAD

## Peaky Minders Global 10Y · 14 de agosto de 2026

> **Este documento reconcilia la versión de implementación con la versión analizada en el
> X-Ray, posición a posición.** Donde la evidencia del registro no permite resolver una
> divergencia, se marca **DECISIÓN PENDIENTE** con lo que falta exactamente — nada se
> decide en silencio. **Ante discrepancia entre cualquier otro documento y éste, manda
> éste** *(y ante discrepancia entre éste y el registro Dxx, manda el registro)*.

---

## 1. LA TABLA

*(Fuente = de dónde sale el dato del vehículo real · todos los datos de producto proceden
de fuente secundaria — catálogo del distribuidor / plataforma de análisis — consultada en
la fecha indicada; la documentación primaria oficial está pendiente para las 13 posiciones.)*

| Módulo | Peso | Vehículo real | ISIN real | Clase | Cobertura divisa | Vehículo usado en X-Ray | Diferencia | Motivo | Fuente | Fecha | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 🚀 Motor · tilt EEUU | 22% | iShares Core S&P 500 UCITS ETF | `IE00B5BMR087` | Acc USD *(cotiza EUR)* | Sin cubrir | El mismo | Ninguna | — | Catálogo · D73 | 13-ago | 🟢 **CERRADO** |
| 🚀 Motor · ancla global | 22% | Vanguard FTSE All-World UCITS ETF | `IE00BK5BQT80` | Acc USD *(cotiza EUR)* | Sin cubrir | El mismo | Ninguna | — | Catálogo · D73 | 13-ago | 🟢 **CERRADO** |
| 🌿 Defensivos · consumo | 6% | Xtrackers MSCI World Consumer Staples | `IE00BM67HN09` | 1C Acc | Sin cubrir | El mismo | Ninguna | — | Catálogo | 13-ago | 🟢 CERRADO |
| 🌿 Defensivos · salud | 6% | iShares S&P 500 Health Care | `IE00B43HR379` | Acc USD | Sin cubrir | El mismo | Ninguna | — | Catálogo | 13-ago | 🟢 CERRADO |
| ⚡ Acel. · tamaño | 4% | **Vanguard Global Small-Cap Index Fund** | `IE00B42W4L06` | **EUR Acc** | Sin cubrir | **SPDR MSCI World Small Cap `IE00BCBJG560`** | **Producto distinto, mismo índice** *(fondo 0,30% vs ETF 0,45%)* | La herramienta de análisis no resolvió la clase del Vanguard | **D77** · catálogo | 13-ago | 🟢 **CERRADO — proxy con regla de atribución** *(del proxy: geografía, sectores, estilo; nunca coste, fiscalidad ni condiciones)* |
| ⚡ Acel. · valor | 4% | Robeco BP Global Premium Equities | `LU0203975437` | **D Acc EUR** | Sin cubrir | Robeco BP Global Premium D EUR | **Mismo fondo** *(identidad verificada: el ISIN `LU0951559797` es la clase D USD del mismo fondo)* | — | D76 · catálogo | 13-ago | 🟢 CERRADO |
| ⚡ Acel. · multifactor | 4% | iShares STOXX Europe Equity Multifactor | `IE00BZ0PKV06` | EUR Acc | Sin cubrir | El mismo | Ninguna | — | Catálogo | 13-ago | 🟢 CERRADO |
| 🌍 **Emergentes** | 7% | *candidato:* iShares Emerging Markets Index **clase S** | `IE000QAZP7L2` | **S Acc EUR** | Sin cubrir | **Clase D del mismo fondo `IE00BYWYCC39`** | **Clase distinta del mismo fondo** *(misma cartera interna; TER distinto: S 0,16%)* | La clase S no está en la base de la herramienta | Catálogo | 13-ago | 🔴 **DECISIÓN PENDIENTE** — ver §2.1 |
| ⚓ Freno · monetario | 6% | AXA Trésor Court Terme C | `FR0000447823` | C | EUR nativo | El mismo | Ninguna | — | Catálogo | 13-ago | 🟢 CERRADO |
| ⚓ Freno · renta fija | 3% | PIMCO GIS Income | `IE00B84J9L26` | **E EUR (Hedged) Acc** | **Cubierta a EUR** | El mismo | Ninguna en el análisis | — | D68 · plataforma de análisis | 13-ago | 🟠 **VIGENTE SUJETO A REVISIÓN por coste** *(decisión pendiente D-a; la función Freno no depende del vehículo)* |
| 🥇 Reales · oro | 7% | WisdomTree **Core** Physical Gold | `JE00BN2CJ301` | ETC física asignada | Sin cubrir | **WisdomTree Physical Gold `JE00B1VS3770`** *(clase estándar)* | **Clase distinta del mismo oro físico** *(coste 0,12% vs 0,39%)* | El Core no estaba en la base de la herramienta | Registro 11-ago *(oro cerrado)* · catálogo | 13-ago | 🟢 **CERRADO — el coste que cuenta es el del Core** |
| 🥇 Reales · cobre | 2% | WisdomTree Copper | `GB00B15KXQ89` | ETC sobre futuros | **SIN cubrir** | **WisdomTree Copper EUR Daily Hedged** | 🔴 **Cobertura de divisa distinta — la única diferencia que CAMBIA EL COMPORTAMIENTO** *(rentabilidad y volatilidad del análisis no trasladables)* | Clase disponible en la herramienta | D76-D77 · catálogo | 13-ago | 🟢 **CERRADO — con limitación declarada en toda cifra del cobre** |
| 💥 Asimetría | 4% | 21Shares Bitcoin Core ETP | `CH1199067674` | ETP físico | Sin cubrir | El mismo | Ninguna | — | Catálogo | 13-ago | 🟢 CERRADO |
| 💧 Reserva | 3% | Efectivo remunerado | — | — | EUR | **No representada** | Fuera del análisis | Por diseño: se analiza el 97% y se reescala *(×0,97)* | D50 · D78 | — | 🟢 CERRADO |

**Suma: 97% módulos + 3% Reserva = 100%.** Convicción = etiqueta de gobernanza *(0%, techo 14%)*, nunca fila.

---

## 2. LAS CUATRO CONCILIACIONES OBLIGATORIAS

### 2.1 🌍 Emergentes — 🔴 DECISIÓN PENDIENTE *(la única no resuelta)*

**Qué dice la evidencia:** el registro nunca cerró formalmente este vehículo — en el
documento de implementación figura como **«candidato»** *(clase S `IE000QAZP7L2`, 0,16%)*,
no como cerrado; y el X-Ray se hizo con la **clase D** del mismo fondo porque la S no
estaba en la base de la herramienta.

**Qué falta exactamente para resolver:**
1. **VETO 0 — confirmar que la clase S es realmente contratable** para la plataforma, el
   tipo de inversor y el importe previsto *(la S es una clase de creación reciente; su
   contratabilidad efectiva no está confirmada en el registro)*;
2. **decisión formal del equipo** cerrando el vehículo *(nunca pasó de candidato)*;
3. la **documentación primaria oficial** de la clase elegida.

**Mientras tanto:** la exposición *(índice MSCI Emerging Markets)* es firme; el look-through
de la clase D es válido *(misma cartera interna)*; **el TER que se publica es el de la
clase S (0,16%) con esa salvedad**. Y la regla de lectura se mantiene: **7% = decisión
dedicada ≠ exposición total** *(el All-World añade más; se mide en el cap. 16)*.

### 2.2 ⚡ Small Caps — 🟢 resuelto por D77

**Real:** fondo Vanguard `IE00B42W4L06` *(EUR Acc, 0,30%)*. **X-Ray:** ETF SPDR
`IE00BCBJG560` *(0,45%)* como **proxy analítico** — mismo índice MSCI World Small Cap.
**Regla de atribución vigente:** del proxy se toman geografía, sectores y estilo;
**nunca** coste, fiscalidad ni condiciones contractuales.

### 2.3 🥇 Oro — 🟢 resuelto *(proxy de clase)*

**Real:** WisdomTree **Core** Physical Gold `JE00BN2CJ301` *(0,12%)* — cerrado en el
registro el 11-ago como el más barato de los ETC de oro físico del catálogo. **X-Ray:**
la clase estándar `JE00B1VS3770` *(0,39%)*. **Mismo oro físico asignado; el look-through
no cambia; el coste que cuenta en todo cálculo es el del Core.**

### 2.4 🥇 Cobre — 🟢 resuelto *(con limitación permanente)*

**Real:** WisdomTree Copper `GB00B15KXQ89`, **sin cobertura de divisa** — verificado en
catálogo *(D76-D77)*. **X-Ray:** la clase **EUR Daily Hedged**. Es la única divergencia
de toda la tabla que **cambia el comportamiento del activo** *(cubrir el dólar altera
rentabilidad y volatilidad)*: **ninguna cifra de rentabilidad/volatilidad del cobre del
X-Ray se traslada al vehículo real**, y esa limitación acompaña a toda mención del cobre.

---

## 3. REGLAS DE USO DE ESTE DOCUMENTO

1. Los capítulos 11 y 14 del Investment Book **citan esta tabla** y no la duplican con
   variaciones.
2. Cualquier cambio de vehículo posterior **actualiza esta tabla primero** *(y la versión:
   v1.1, v1.2…)* con su decisión registrada.
3. Los estados 🟠/🔴 de esta tabla son **las dos únicas cuestiones de vehículo abiertas**:
   PIMCO *(revisión por coste)* y Emergentes *(cierre formal + VETO 0)*.

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-14 | **Creación.** Conciliación completa implementación ↔ X-Ray *(14 filas)*. Emergentes marcado **DECISIÓN PENDIENTE** con los tres requisitos exactos *(VETO 0 de contratabilidad, cierre formal, documentación primaria)* — la evidencia del registro muestra «candidato», nunca cierre. Small Caps, Oro y Cobre reconciliados con su evidencia *(D77, registro 11-ago, D76-D77)*. PIMCO vigente sujeto a revisión sin tocar la función |
