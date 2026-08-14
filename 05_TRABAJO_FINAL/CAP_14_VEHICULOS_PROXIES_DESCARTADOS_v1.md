# CAPÍTULO 14 — VEHÍCULOS, PROXIES Y ALTERNATIVAS DESCARTADAS

## Investment Book · Parte II · Borrador v1 · 13 de agosto de 2026

> **Convención:** **[MODELO]** = decisión propia · **[EVIDENCIA EXTERNA]** = requiere
> fuente. Datos de producto: ✅ fuente primaria *(KID/documento oficial)* · 🟡 fuente
> secundaria *(catálogo del distribuidor / plataforma de análisis, consultados el
> 13-ago-2026)*, pendiente de primaria · 🔴 no usar.
>
> **El último eslabón de la cadena.** Mandato, funciones y pesos ya están; este capítulo
> documenta con qué productos concretos se implementa cada función — y con qué criterios,
> qué sustitutos analíticos y qué descartes por el camino.

---

## 14.1 Los criterios de selección

**[MODELO]** Para cada función, los vehículos candidatos se compararon con una lista
estable de criterios — en este orden aproximado de peso:

1. **Fidelidad a la exposición buscada** *(índice o mandato correctos)*;
2. **Coste total**;
3. **Estructura y tamaño** *(patrimonio, réplica, antigüedad)*;
4. **Operativa con el mandato** *(aportaciones mensuales por importe, divisa, clase de
   acumulación)*;
5. **Tratamiento fiscal del vehículo** — ⚠️ atributo relevante en España cuya
   documentación formal se realiza en el capítulo 22; hasta entonces no se usan
   afirmaciones fiscales categóricas;
6. **Disponibilidad real en la plataforma de contratación.**

Un criterio que NO está en la lista: la rentabilidad reciente del producto. Dos vehículos
que replican el mismo índice rinden lo mismo salvo coste y calidad de réplica; elegir por
el histórico corto es elegir ruido.

---

## 14.2 La tabla de vehículos — versión de referencia v1.0

**Estado de verificación: todos los datos proceden de fuente secundaria** *(catálogo,
13-ago-2026)*; **los 13 documentos oficiales (KID) están pendientes** — por eso ninguna
fila lleva ✅ todavía. El coste total estimado de la cartera se mantiene como **estimado**
hasta cerrar esa verificación.

| Módulo | Vehículo | ISIN | Coste | Estado |
|---|---|---|---|---|
| 🚀 Motor · tilt EEUU 22% | iShares Core S&P 500 UCITS ETF | `IE00B5BMR087` | 0,07% | 🟡 |
| 🚀 Motor · ancla global 22% | Vanguard FTSE All-World UCITS ETF Acc | `IE00BK5BQT80` | 0,14% | 🟡 |
| 🌿 Defensivos · consumo 6% | Xtrackers MSCI World Consumer Staples | `IE00BM67HN09` | 0,25% | 🟡 |
| 🌿 Defensivos · salud 6% | iShares S&P 500 Health Care | `IE00B43HR379` | 0,15% | 🟡 |
| ⚡ Aceleración · tamaño 4% | Vanguard Global Small-Cap Index EUR Acc | `IE00B42W4L06` | 0,30% | 🟡 |
| ⚡ Aceleración · valor 4% | Robeco BP Global Premium Eq **D Acc EUR** | `LU0203975437` | 1,46% | 🟡 |
| ⚡ Aceleración · multifactor 4% | iShares STOXX Europe Equity Multifactor | `IE00BZ0PKV06` | 0,25% | 🟡 |
| 🌍 Emergentes 7% | iShares Emerging Markets Index **clase S** | `IE000QAZP7L2` | 0,16% | 🟡 · ⚠️ clase pendiente de confirmación contractual |
| ⚓ Freno · monetario 6% | AXA Trésor Court Terme C | `FR0000447823` | 0,06% | 🟡 |
| ⚓ Freno · renta fija 3% | PIMCO GIS Income E EUR (H) Acc | `IE00B84J9L26` | 1,45% | 🟡 *(plataforma de análisis)* · 🔴 KID pendiente · ⚠️ **vehículo vigente sujeto a revisión de implementación por coste** |
| 🥇 Reales · oro 7% | WisdomTree **Core** Physical Gold | `JE00BN2CJ301` | 0,12% | 🟡 |
| 🥇 Reales · cobre 2% | WisdomTree Copper | `GB00B15KXQ89` | 0,49% | 🟡 |
| 💥 Asimetría 4% | 21Shares Bitcoin Core ETP | `CH1199067674` | 0,10% | 🟡 |
| 💧 Reserva 3% | Efectivo remunerado | — | — | — |

**Coste ponderado estimado de la cartera: ≈0,23%** *(cálculo peso × coste sobre los datos
anteriores; cifra **estimada** hasta las 13 verificaciones primarias — el detalle del
cálculo y su sensibilidad, en el capítulo 22)*.

---

## 14.3 Vehículo real y vehículo analizado: la tabla de conciliación

**[MODELO]** El análisis mirando dentro *(el X-Ray oficial de la Parte III)* no siempre
pudo usar el vehículo exacto contratable. La conciliación completa, posición a posición:

| Posición | Vehículo real | Vehículo del análisis | Situación |
|---|---|---|---|
| Motor · ambas piezas | Los de la tabla | Los mismos | ✅ idénticos |
| Defensivos · ambas | Los de la tabla | Los mismos | ✅ idénticos |
| Aceleración · multifactor | El de la tabla | El mismo | ✅ idéntico |
| Aceleración · valor | Robeco D Acc EUR | Robeco D EUR | ✅ mismo fondo |
| Freno · ambas | Los de la tabla | Los mismos | ✅ idénticos |
| Asimetría | El de la tabla | El mismo | ✅ idéntico |
| **Aceleración · tamaño** | **Vanguard** `IE00B42W4L06` | **SPDR MSCI World Small Cap** `IE00BCBJG560` | 🟡 **proxy declarado (D77)** — mismo índice; del proxy se toman geografía, sectores y estilo; **nunca coste, fiscalidad ni condiciones contractuales** |
| **Emergentes** | Clase S | **Clase D del mismo fondo** | 🟡 proxy de clase — misma cartera interna; el coste que se publica es el de la clase contratada |
| **Reales · oro** | WisdomTree **Core** *(0,12%)* | WisdomTree Physical Gold *(clase estándar)* | 🟡 mismo oro físico; **el coste que cuenta es el del Core** |
| **Reales · cobre** | Sin cobertura de divisa | **Clase cubierta a euro** | 🔴 **la única discrepancia que cambia el comportamiento** — la cobertura altera rentabilidad y volatilidad; limitación declarada en toda cifra del cobre |
| Reserva | Efectivo | No representada | — fuera del análisis por diseño *(se analiza el 97% y se reescala)* |

La regla que gobierna la tabla es la de D77, y vale para todos los casos:

> **Del proxy solo se toma aquello para lo que es realmente equivalente.**

---

## 14.4 Las alternativas descartadas — el archivo que da credibilidad

**[MODELO]** Una cartera sin descartes documentados es sospechosa: significa que se compró
lo primero que apareció. Ésta lleva su archivo — cada descarte con su motivo y su rastro
en el registro:

| Alternativa estudiada | Para | Por qué se descartó |
|---|---|---|
| **Fondo de calidad global** | Aceleración | El análisis cuestionó que aportara suficiente diferenciación respecto al núcleo: la medición interna del proyecto arrojó una correlación con el Motor de 0,96 🟡 *(medición propia del 12-ago-2026 sobre datos de plataforma; ventana no documentada — pendiente de re-verificación formal)*. Al retirarlo, varias métricas de la cartera mejoraron |
| **Vehículo único de desarrollados** *(Motor «A»)* | Motor | Estudiado con análisis completo propio; descartado por decisión de equipo a favor del tilt declarado *(D73)* — expediente íntegro conservado |
| **Bloque tecnológico específico** | — | El análisis mirando dentro mostró exposición tecnológica ya material por varias vías *(caso del cap. 6; cifra auditada en el cap. 16)* |
| **Japón como pieza separada** | Emergentes/desarrollados | La exposición deseada quedaba razonablemente cubierta; su peso se reasignó |
| **Fondo de salud de gestión activa** | Defensivos | La clase contratable resultaba cara frente al indexado comparable; la comparación quedó registrada |
| **Mineras de oro** | Activos Reales | Disponibles, pero descartadas **por diseño**: son renta variable, con volatilidad muy superior al metal — no cumplen la función del módulo |
| **Cesta amplia de materias primas** | Activos Reales | Mezcla exposiciones no buscadas *(energía, agrícolas)* |
| **Clase estándar del oro** *(0,39%)* | Activos Reales | El mismo oro a más del triple de coste que la clase Core |
| **Cesta diversificada de criptoactivos** | Asimetría | Histórico de caídas peor que el del activo principal en la comparación registrada |
| **Renta fija indexada global de corto plazo** | Freno | Fue la pieza de referencia anterior; sustituida por el vehículo vigente — **y es candidata natural de vuelta si la revisión por coste del PIMCO concluye en contra** |

**[MODELO]** Nótese la asimetría sana del archivo: hay descartes por coste, por función,
por redundancia y por diseño — y uno de ellos *(la renta fija indexada)* puede volver.
**Descartar no es condenar: es documentar por qué hoy no.**

---

## 14.5 Síntesis

> **Trece vehículos con sus códigos y costes en fuente secundaria a la espera de trece
> documentos oficiales; cuatro sustitutos analíticos con su regla de atribución —de los
> cuales solo uno altera el comportamiento y queda señalado—; y un archivo de diez
> descartes con motivo y rastro. El eslabón final de la cadena está documentado: qué se
> compra, por qué eso, y por qué no lo otro.**

---

## CIERRE — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes | Remisiones |
|---|---|---|---|---|---|
| D73 *(Motor)* · D77 *(proxy y regla de atribución)* · D68 *(identificación del vehículo de renta fija)* · D67 *(preguntas de coste abiertas)* · registro de descartes del proyecto | La tabla de 13 vehículos con estado por fila · la conciliación posición a posición · el archivo de 10 descartes trazados | **Ningún dato de producto en fuente primaria todavía** · PIMCO en revisión por coste · clase de Emergentes pendiente de confirmación · la discrepancia de cobertura del cobre afecta a toda cifra suya · la correlación del caso calidad es medición propia sin ventana documentada | ① La tabla de vehículos con semáforos ② La conciliación real↔analizado ③ El archivo de descartes | 🔴 **13 KID** — la mayor pendencia del capítulo · 🟠 revisión por coste del vehículo de renta fija *(alternativa indexada identificada)* · 🟡 confirmación contractual de la clase de Emergentes · 🟡 re-verificación formal de la correlación del caso calidad | **Cap. 22** *(costes y fiscalidad con fuente primaria)* · **Caps. 15-18** *(el análisis que usa los proxies)* · **Cap. 11** *(la función de cada vehículo)* · **Anexo D** *(descartes en detalle)* |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Borrador v1** — criterios de selección *(la rentabilidad reciente excluida a propósito)*, tabla de 13 vehículos íntegramente en 🟡 con los KID en 🔴, conciliación real↔analizado con el cobre como única discrepancia de comportamiento, y archivo de 10 descartes — incluida la candidatura de retorno de la renta fija indexada si la revisión del PIMCO concluye en contra |
