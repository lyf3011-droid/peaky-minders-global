# 🔬 AUDITORÍA DE INTEGRACIÓN — PMMA → INVESTMENT BOOK

## 13 de agosto de 2026 · sobre `Peaky Minders Modular Architecture.pdf` (40 págs., 34 secciones)

> **Leído íntegro antes de esta auditoría.** Nada modificado: ni pesos, ni módulos, ni
> vehículos, ni X-Ray. **Este documento es la entrega A-G previa a la redacción del libro.**

---

# A. VALOR DEL DOCUMENTO

## A.1 Aportación metodológica real — el núcleo que va al cuerpo principal

| § PDF | Aportación | Por qué es núcleo |
|---|---|---|
| **§3** | **Principio de Función Dominante** | Es LA tesis. Todo lo demás cuelga de aquí |
| **§5** | **Dos capas transversales** (Overlay / Execution) | Separa asignación de gestión y de ejecución — la distinción menos común del mercado |
| **§7 · §10** | **Position Mode vs Look-Through Mode** + *«la arquitectura expresa la intención; el X-Ray verifica el resultado»* | Resuelve el problema real de intención vs exposición |
| **§14** | **Árbol de clasificación** (8 preguntas ordenadas) | Convierte la intuición en procedimiento auditable. **El orden de las preguntas ES el método** |
| **§15** | **Protocolo de Extensión** | Reconocer que algo no encaja > falsear la taxonomía. Fortaleza y límite a la vez |
| **§16** | **Modelo de datos** (26 campos) | El puente a Excel/HARVISS. Auditado en A.4 |
| **§18-19** | **Target vs actual · dos vistas del capital** | *«Un target transforma una colección en una política»* — frase de libro |
| **§27** | **Gate de aceptación** (10 preguntas) | El elemento visual y metodológico más fuerte. Global 10Y debe pasarlo explícitamente |
| **§29** | **10 principios de gobernanza** | Condensan el método en reglas verificables |
| **§31-33** | **Definición formal + cadena OBJETIVO→…→CONTROL** | El esqueleto de la Parte I |

## A.2 Explicación (se sintetiza, no se reproduce)

**§4** *(descripciones de los 7 módulos: se sintetizan a ficha + pregunta de control)* · **§8**
*(proceso en 7 pasos: bueno pero estándar — se condensa)* · **§9** *(diversificación funcional
vs aparente: una página)* · **§17** *(ficha estándar: plantilla, va donde se use)* ·
**§20-24** *(rebalanceo, solapamiento, riesgo, acciones, bitcoin: se funden con el material
ya existente del proyecto, que es MÁS detallado que el PDF)*.

## A.3 Anexo técnico

**§11-13 detalle completo** *(las 8 carteras históricas — al cuerpo va la síntesis y la tabla;
el desarrollo, a anexo tras verificar fuentes)* · **§16 tabla completa de campos** · **§25**
*(multicuenta — fuera del alcance del mandato actual)* · **§26** *(niveles 1-4 de
escalabilidad — anexo: el libro solo demuestra el nivel 2-3)* · **§30** *(expediente — se usa
como checklist del propio libro, no como capítulo)*.

## A.4 Auditoría del modelo de datos — **faltan 9 campos, y 4 son lecciones de este proyecto**

| Campo ausente | Por qué es esencial |
|---|---|
| 🔴 **ISIN** | El proyecto entero se gobierna por ISIN; el ticker es ambiguo en UCITS multi-listing |
| 🔴 **Clase de participación** | La lección S/D del Motor y Emergentes: misma cartera, distinta clase, distinto TER |
| 🔴 **Proxy analítico** *(sí/no + cuál)* | La lección D77: sin este campo la regla de atribución no es registrable |
| 🔴 **Cobertura de divisa** *(hedged/unhedged)* | La lección del cobre: es el único caso no equivalente del X-Ray |
| 🟠 **Traspasabilidad fiscal** | Decidió D77 (fondo vs ETF). En España es un atributo de primer orden |
| 🟠 **Acumulación/distribución** | Está en la lista del §8 paso 5 pero NO en el modelo de datos |
| 🟠 **Fuente y fecha del dato** | «TER 1,45% (Morningstar, 13-ago; KIID pendiente)» — sin esto no hay nivel de verificación |
| 🟡 **Confianza de clasificación** *(alta/media/ambigua + justificación)* | La propuesta del mandato: convierte la subjetividad en dato auditable. **Sí aporta valor: adóptese** |
| 🟡 **Contribución al riesgo** | El §22 lo exige conceptualmente pero el modelo no lo almacena |

---

# B. CONTRADICCIONES — enumeradas · ✅ **B1, B2, B3 y B8 RESUELTAS POR D78 el 13-ago**

> **B1:** modos de gestión ①-④; Robeco = Aceleración + activa delegada; Convicción Directa ≠ toda gestión activa.
> **B2:** política permanente, capital transitorio, capacidad 3%.
> **B3:** Structural Exposure View *(módulo + tag)* / Governance-Funding View *(47% en revisión)*.
> **B8:** cap. 19 desarrolla las cuatro cajas; el cap. 4 solo lleva el mapa módulo→régimen como hipótesis de diseño.
> **Índice de 27 capítulos: APROBADO.** Quedan abiertas B4-B7, B9 *(tratamiento ya definido en la tabla)*.

| # | Contradicción | Gravedad |
|---|---|---|
| **B1** | **PMMA §5.1 etiqueta al Robeco como «Active Overlay / Convicción»**. D63/D67 y el propio mandato de integración dicen lo contrario: Robeco = **Aceleración + gestión activa delegada**, NUNCA Convicción. El PDF además titula «🎯 CONVICCIÓN — ACTIVE OVERLAY» como identidad. **Resolución pendiente de aprobar:** Active Overlay = categoría universal PMMA con DOS subtipos — *selección directa discrecional* (= Convicción en Global 10Y) y *gestión activa delegada* (Robeco, PIMCO). El ejemplo del Robeco en §5.1 debe reescribirse | 🔴 |
| **B2** | **PMMA §5.2 define Reserva como «capital temporalmente disponible… esperando ser invertido»**. En Global 10Y (D50, D56, D75) la Reserva Operativa es una capa **permanente con objetivo del 3%** que participa en el ranking de infraponderación y se reconstruye tras usarse. No es tránsito: es infraestructura estable. **Hay que reconciliar:** la definición PMMA admite ambas si se redacta «capital destinado a ejecución, transitorio o permanente por política» | 🔴 |
| **B3** | **La composición de Global 10Y presenta Convicción como FILA de la tabla estructural** (Motor 44 · … · Convicción 0-14 = 100). **PMMA §2/§5 prohíbe sumar el overlay como clase de activo**: el capital cuenta una vez en su módulo y el overlay es una marca. Con Convicción al 0% no hay conflicto aritmético, pero **al desplegarse, ¿la compra de MSFT es una fila nueva o capital del Motor marcado como overlay?** El macrobloque del 47% (D48) apunta a lo segundo; las tablas publicadas muestran lo primero. **Debe decidirse UNA representación antes de redactar** | 🔴 |
| **B4** | **PMMA §4.4 regla de no duplicidad de Emergentes** *(«si ya forman parte de un índice global, no deben contabilizarse nuevamente»)* choca retóricamente con el Motor B: el All-World lleva emergentes Y existe el bloque Emergentes al 7%. D73 lo declara «sobreponderación estratégica independiente». **No es contradicción en Position Mode** (el All-World se asigna 100% a Motor), **pero el tribunal puede citar la regla del propio PDF contra la cartera.** El libro debe anticiparlo con la distinción Position/Look-Through | 🟠 |
| **B5** | **PMMA §4.2 lista Quality en Defensivos y §4.3 lista los factor tilts en Aceleración.** Quality es ambiguo entre ambos — y es EXACTAMENTE el activo que este proyecto probó y descartó (correlación 0,96). El árbol §14 lo resuelve por orden (defensivo antes que factor) + tesis registrada, **pero el PDF no lo dice explícitamente** | 🟠 |
| **B6** | **PMMA §13 usa como «ejemplo conceptual» Motor 45 / Freno 10 / Reales 10** — casi idéntico pero NO igual a la parametrización real (44/9/9). Riesgo de que un lector lo tome por la cartera. Debe etiquetarse «ejemplo didáctico, no la implementación» o cambiarse | 🟡 |
| **B7** | **Las 8 traducciones históricas del §11 carecen de verificación de fuente primaria en el repo.** Mis comprobaciones de memoria: Browne 4×25 ✓ · Buffett carta 2013 90/10 ✓ · All Seasons (Robbins) 30/40/15/7,5/7,5 ✓ · Swensen 30/15/5/20/15/15 ✓ · Faber 5×20 + SMA 10 meses ✓ · Golden Butterfly 5×20 ✓. **Pero «coincide con mi memoria» NO es fuente primaria.** Pendiente T-nueva: verificar los 8 contra originales y distinguir All Weather institucional de All Seasons divulgada | 🟠 |
| **B8** | **El marco de cuatro cajas (crecimiento × inflación) exigido por el enunciado del concurso y por la rúbrica (dimensión 11, hoy 0/5) NO existe en PMMA.** Son dos principios organizadores distintos (función vs régimen macro). **El libro debe mapear módulos → cajas y demostrar que ninguna caja queda huérfana**, o la dimensión 11 sigue en 0 | 🔴 |
| **B9** | **PMMA §19 «Strategic Allocation» renormaliza los 7 módulos excluyendo la Reserva.** El X-Ray oficial renormaliza el 97% **incluyendo el AXA del Freno pero excluyendo la Reserva** — compatible, pero son dos convenciones de normalización que deben declararse como la misma con nombre distinto | 🟡 |
| **B10** | El índice maestro vigente (D71) tiene **62 capítulos**; el mandato de integración exige **27 + anexos**. No es contradicción de contenido sino de estructura — se resuelve en la sección D degradando los 62 a subcapítulos/checklist | 🟡 |

---

# C. FORTALEZAS Y DEBILIDADES ACADÉMICAS — crítica hostil

## C.1 La pregunta del tribunal, respondida sin trampas

> *«¿Por qué necesitáis crear PMMA si ya existen asset allocation, core-satellite, factor
> investing y risk parity?»*

**Respuesta honesta:** PMMA **no** aporta una teoría nueva de precios de activos ni una
taxonomía conceptualmente inédita. Lo que existe disperso —roles de cartera de Morningstar,
core-satellite, goals-based investing, la lógica funcional de Swensen— **PMMA lo integra en
un pipeline único y auditable**: mandato → funciones → pesos → exposiciones → vehículos →
X-Ray → riesgo → ejecución → control, con **árbol de clasificación, protocolo de excepciones,
modelo de datos, gate de aceptación y decision log**. **La aportación es organizativa y de
trazabilidad, no teórica.** Si el libro reclama más que eso, el tribunal gana. Si reclama
exactamente eso, es defendible — porque el expediente D1-D77 DEMUESTRA el pipeline funcionando.

## C.2 Debilidades que hay que declarar (no maquillar)

| # | Debilidad | Tratamiento |
|---|---|---|
| **1** | **Subjetividad del Principio de Función Dominante.** Dos analistas pueden clasificar distinto el mismo activo (Quality: ¿Defensivos o Aceleración?) | Mitigada, no eliminada: árbol ordenado + pregunta de control + tesis registrada + **campo de confianza de clasificación** + segunda revisión en ambigüedad. Se declara residual |
| **2** | **Riesgo de infalsabilidad.** Un marco descriptivo nunca «falla». ¿Qué falsaría a PMMA? | Proponer el criterio: *si la clasificación funcional no agrupa mejor el comportamiento (correlaciones, drawdowns) que la clasificación por tipo de producto, el marco añade nombres sin información*. Y admitir la evidencia propia: **Aceleración correlaciona 0,70-0,91 con el Motor** — la separación funcional NO es separación estadística, y el marco lo reconoce (funcional ≠ aparente) |
| **3** | **Riesgo de racionalización ex post.** PMMA se escribió en paralelo a la cartera: puede parecer una justificación retrospectiva | Defensa: el decision log fechado (D1-D77) y la validación sobre 8 carteras ajenas. Pero la validación la hicimos NOSOTROS: es capacidad descriptiva, no aval de terceros. Se dice así |
| **4** | **«Taxonomía con nombres propios».** Con otros siete nombres el método funciona igual | Cierto y se admite: **el valor no está en los nombres sino en las separaciones** (función/producto · estructura/overlay/ejecución · position/look-through · target/actual) |
| **5** | **Generalización no demostrada.** 8 carteras traducidas ≠ universalidad | Formulación obligada: *«se evalúa la capacidad descriptiva del marco sobre arquitecturas heterogéneas»*. Prohibido «universal» como hecho. «Generalizable/escalable, sujeto a limitaciones» |
| **6** | **Comparabilidad entre analistas no testada.** Nadie ajeno ha clasificado nada con PMMA | Límite declarado + propuesta de extensión futura (test inter-analista) |

## C.3 Fortalezas genuinas

**①** La cadena completa mandato→control con un artefacto verificable en cada eslabón *(el
expediente §30 = literalmente lo que este proyecto ya tiene)* · **②** el Protocolo de
Extensión — reconocer límites como regla del sistema · **③** Position/Look-Through como
resolución explícita de intención vs exposición · **④** la separación overlay/estructura que
permite describir el GTAA de Faber sin romper la arquitectura · **⑤** que la implementación
Global 10Y ya lo cumple casi todo: **el libro no promete un método, lo exhibe funcionando.**

---

# D. ÍNDICE MAESTRO REVISADO — 27 capítulos + anexos

*(Los 62 elementos de D71 quedan como subcapítulos y checklist Cum Laude; la rúbrica de 12
dimensiones sigue vigente como vara de medir.)*

| # | Título | Objetivo / qué demuestra | Material PMMA | Material previo | Evidencia pendiente | Visual | Estado |
|---|---|---|---|---|---|---|---|
| **PARTE I — PROBLEMA, MANDATO Y MARCO** | | | | | | | |
| 1 | Resumen ejecutivo | Síntesis — **se escribe el último** | §33 | — | todo | 1 pág. visual | 🔴 |
| 2 | El problema: carteras como listas de productos | Motivar el método | §1, §9 | — | — | comparativa lista/sistema | 🟡 |
| 3 | Mandato Peaky Minders Global 10Y | 100k · 1k/mes · 10a · agresivo · ventana de retirada | §8 paso 1 | `PROTOCOLO §0` · D54 | **tensión 10 años/agresivo** | ficha de mandato | 🟠 |
| 4 | PMMA: función dominante y los siete módulos | El núcleo del método | §2-4, §31-34 | D75 · D78-D79 | — | esquema de capas | 🟢 **CERRADO v2** |
| 5 | Capas transversales: Convicción y ejecución | Estructura ≠ gestión ≠ gobernanza ≠ ejecución | §5 | D50 · D63 · D78-D80 | — | diagrama 3 capas | 🟢 **CERRADO v2** |
| 6 | Los dos modos de análisis: por posición y mirando dentro | Intención vs resultado | §7, §10 | D52 · D62 · D73 · D77 · D81 | — | doble vista | 🟢 **CERRADO v2** |
| 7 | Las herramientas del método: clasificar, registrar y comprobar | El método es procedimiento, no intuición | §14-16, §27, §29 | D75 · D77-D79 · D82 | — | árbol + control final | 🟢 **CERRADO v2** |
| 8 | Validación descriptiva: 8 arquitecturas históricas | Capacidad descriptiva, no universalidad | §11-13 | — | 🔴 **fuentes primarias (B7)** | tabla comparativa | 🟠 |
| 9 | Limitaciones del marco | Subjetividad, falsabilidad, ex post | §28 | C.2 de esta auditoría | — | — | 🟡 |
| **PARTE II — IMPLEMENTACIÓN: GLOBAL 10Y** | | | | | | | |
| 10 | Del mandato a la parametrización | Los pesos como instancia, no como regla | §8 pasos 2-3, §18 | D65 · D73 · D75 | — | target vs actual | 🔵 |
| 11 | Los siete módulos implementados *(7 secciones)* | Ficha §17 por módulo, con «dónde falla» | §17 | D73 · D67 · fichas | D67 ①-④ sin responder | 7 fichas | 🟠 |
| 12 | Convicción: overlay condicional con IDC | El overlay más regulado del libro | §5.1 | D45-D61 · `PROTOCOLO` | fichas IDC (≥3) | árbol de compra | 🔵 |
| 13 | Reserva Operativa y flujo de aportaciones | *«La aportación no replica: rebalancea»* | §5.2, §20 | D56-D59 | — | árbol mensual | 🟢 |
| 14 | Vehículos, proxies y descartados | Real vs proxy con regla de atribución | §8 paso 5 | D77 · `VEHICULO_REAL_VS_XRAY` · X-Ray §9 | **13 KIID** | tabla conciliación | 🔵 |
| **PARTE III — VALIDACIÓN CUANTITATIVA** | | | | | | | |
| 15 | X-Ray oficial: metodología y salvedades | La verificación del §10 PMMA aplicada | §10 | `XRAY_OFICIAL` §1, §10 | salvedad 5a All-World | — | 🔵 |
| 16 | Composición: geografía, sectores, estilo, holdings | Intención confirmada/desmentida | §7 | X-Ray §3-4 | — | mapas + barras | 🔵 |
| 17 | Rentabilidad y riesgo | Las 21 cifras + regla ×0,7693 | — | X-Ray §4 · D62 | Sortino | tabla 3a/5a | 🔵 |
| 18 | Correlaciones, concentración y divisa | Funcional ≠ estadístico (honesto) | §9, §22 | X-Ray §5 · D66 | 🔴 **divisa sin cuantificar** | matriz | 🟠 |
| **PARTE IV — ROBUSTEZ** | | | | | | | |
| 19 | Marco macro: cuadrante crecimiento × inflación | Ninguna caja huérfana *(cierra B8)* | — | **NO EXISTE** | 🔴 **construir** | cuadrante 4 cajas | 🔴 |
| 20 | Stress por régimen: 1973 · 2000 · 2008 · 2022 | La cartera bajo regímenes reales | — | `D47a` **provisional** | 🔴 **auditar shocks** | barras por régimen | 🔴 |
| 21 | Escenarios de despliegue de Convicción | D53 | — | **NO EXISTE** | 🔴 **construir** | 4 sendas | 🔴 |
| **PARTE V — OPERATIVA Y GOBERNANZA** | | | | | | | |
| 22 | Costes y fiscalidad | ≈0,23% estimado → verificado · bruto vs neto | §8 paso 5 | D64 · D76 · D77 | 🔴 **13 KIID · bruto/neto** | cascada de costes | 🟠 |
| 23 | Rebalanceo y política de venta | Bandas + aportaciones · D47b | §20 | D56 · `PROTOCOLO §8-12` | 🔴 **D47b** | — | 🟠 |
| 24 | Benchmark, alfa, Fecha Cero y cohorte real | Medición sin hindsight | — | D60-D61 · `PROTOCOLO §15-19` | tabla Fecha Cero | — | 🔵 |
| 25 | Gobernanza y decision log | D1-D77 como evidencia del método | §29-30 | `ESTADO §3` · `REVISIONES` | — | línea temporal | 🟢 |
| **PARTE VI — AUTOCRÍTICA Y CONCLUSIONES** | | | | | | | |
| 26 | El Gate aplicado a Global 10Y + qué nos haría cambiar | Las 10 preguntas respondidas con evidencia | §27 | X-Ray · D66 · salvedades | pasar el Gate | tablero 10 semáforos | 🔴 |
| 27 | Conclusiones y extensiones | Principios que sobreviven a los productos | §34 | — | todo lo anterior | — | ⚫ |

**ANEXOS:** A) Manual PMMA íntegro *(el PDF, con las correcciones B1/B6)* · B) Registro
D1-D77 · C) Informes X-Ray *(oficial + alternativa Motor A + históricos)* · D) Fichas de los
13 vehículos · E) Alternativas descartadas · F) Fuentes · G) Glosario · H) Modelo de datos
completo *(26 + 9 campos)*.

---

# E. MAPA PDF → INVESTMENT BOOK — las 34 secciones, ninguna sin destino

| § PMMA | → Capítulo | Cuerpo/Anexo | Acción |
|---|---|---|---|
| 1 Propósito | 2 | Cuerpo | Integrar |
| 2 Tesis central | 4 | Cuerpo | Integrar *(corregir «Convicción = Active Overlay» → B1)* |
| 3 Función dominante | 4 | Cuerpo | Integrar |
| 4.1-4.7 Módulos | 4 + 11 | Cuerpo (síntesis) | Sintetizar a ficha; resolver ambigüedad Quality (B5) |
| 5.1 Overlay | 5 | Cuerpo | 🔴 **Reescribir el ejemplo Robeco** (B1) |
| 5.2 Execution | 5 + 13 | Cuerpo | 🔴 **Reconciliar definición de Reserva** (B2) |
| 6 Peso 0% | 4 | Cuerpo | Integrar — explica Convicción 0% |
| 7 Dos modos | 6 | Cuerpo | Integrar |
| 8 Proceso 7 pasos | 10 | Cuerpo (condensado) | Sintetizar |
| 9 Diversificación funcional vs aparente | 2 + 18 | Cuerpo | Integrar con la evidencia 0,70-0,91 |
| 10 X-Ray verificación | 6 + 15 | Cuerpo | Integrar — frase central |
| 11.1-11.8 Carteras históricas | 8 | Cuerpo (síntesis) + Anexo | 🔴 **Verificar fuentes primarias** (B7) |
| 12 Tabla comparativa | 8 | Cuerpo | Integrar tras verificación |
| 13 Qué demuestra | 8 | Cuerpo | Integrar con la formulación no-universal |
| 14 Árbol | 7 | Cuerpo + visual | Integrar |
| 15 Extensión | 7 | Cuerpo | Integrar |
| 16 Modelo de datos | 7 + Anexo H | Anexo (tabla completa) | **Ampliar con 9 campos** (A.4) |
| 17 Ficha de módulo | 11 | Cuerpo (plantilla) | Usar como formato de las 7 fichas |
| 18 Target vs actual | 10 | Cuerpo | Integrar |
| 19 Dos vistas | 10 + 15 | Cuerpo | Integrar; unificar con la convención 97% (B9) |
| 20 Rebalanceo | 23 | Cuerpo | Fundir — el material propio (D56) es superior |
| 21 Solapamiento | 18 | Cuerpo | Integrar (3 preguntas) |
| 22 Control de riesgo | 18 | Cuerpo | Integrar |
| 23 Acciones individuales | 12 | Cuerpo | Integrar — conecta con Convicción |
| 24 Bitcoin | 11 (Asimetría) | Cuerpo | Integrar |
| 25 Multicuenta | Anexo | Anexo | Mover — fuera del mandato actual |
| 26 Escalabilidad niveles | Anexo | Anexo | Mover — el libro demuestra nivel 2-3 |
| 27 Gate | 7 + 26 | Cuerpo ×2 | Integrar: definición en 7, **aplicación en 26** |
| 28 Qué no es PMMA | 9 | Cuerpo | Integrar |
| 29 Principios | 7 + 25 | Cuerpo | Integrar |
| 30 Expediente | 25 | Cuerpo (checklist) | Usar como autocomprobación del libro |
| 31 Definición formal | 4 | Cuerpo | Integrar literal |
| 32 Formulación corta | 4 | Cuerpo | Integrar |
| 33 Idea central | 1 + 4 | Cuerpo | Integrar |
| 34 Principio final | 27 | Cuerpo | Cierre de conclusiones |

**Descartes justificados: ninguno.** Todo tiene destino; 3 secciones van a anexo.

---

# F. MAPA DE TRAZABILIDAD GENERAL

| Decisión / documento | → Capítulo | Evidencia | Estado |
|---|---|---|---|
| D54 mandato · `MANDATO.md` | 3 | PROTOCOLO §0 | 🔵 |
| D75 arquitectura modular | 4-5 | `ARQUITECTURA_MODULAR_v1` | 🔵 |
| D63 tres niveles de gestión | 5 | PROTOCOLO §1.1 | 🔵 *(pend. B1)* |
| D50 · D56-D59 Reserva y flujo | 13 | PROTOCOLO §8-11 | 🟢 |
| D45-D49 · D55 · D57-D61 Convicción/IDC | 12 | `D45` · PROTOCOLO §2-7 | 🔵 |
| D73 Motor tilt USA + tesis | 11 | `XRAY_OFICIAL` · dossier macro pendiente | 🟠 |
| D72 evidencia A/B | 11 + Anexo C | `XRAY_ALTERNATIVA_MOTOR_A` | 🟢 |
| D77 vehículo real vs proxy | 14 | `VEHICULO_REAL_VS_XRAY` | 🟢 |
| D62 X-Ray oficial + regla lectura | 15-17 | `XRAY_OFICIAL_2026-08-13` | 🔵 |
| D66 hallazgos materiales | 18 + 26 | X-Ray §4-5 | 🔵 |
| D64 · D76 coste | 22 | cálculo peso×coste | 🟠 *(13 KIID)* |
| D47a estrés | 20 | `D47a` provisional | 🔴 |
| D47b ventas | 23 | no existe | 🔴 |
| D53 escenarios | 21 | no existe | 🔴 |
| D67 preguntas Robeco/PIMCO | 11 | sin responder | 🟠 |
| D68 PIMCO identificado | 14 · 22 | ficha Morningstar | 🟡 |
| Rúbrica D71 | transversal | `INDICE_MAESTRO_CUM_LAUDE` | vigente como checklist |

---

# G. ORDEN DE REDACCIÓN — columna vertebral primero

```
FASE 1 · COLUMNA METODOLÓGICA (nada la bloquea)
  4 → 5* → 6 → 7 → 2 → 9        *5 exige resolver antes B1, B2 y B3
                                  (una decisión de 30 min, no trabajo nuevo)

FASE 2 · VALIDACIÓN DEL MÉTODO
  8   ← tras verificar las 8 fuentes primarias (B7, delegable T-nueva)
  3   ← exige cerrar en grupo la tensión 10 años / agresivo

FASE 3 · IMPLEMENTACIÓN (demuestra la Fase 1)
  10 → 13 → 12 → 14 → 11        11 el último: necesita D67 y dossier macro D73

FASE 4 · VALIDACIÓN CUANTITATIVA
  15 → 16 → 17 → 18             18 exige cuantificar divisa

FASE 5 · ROBUSTEZ (los tres huecos duros)
  19 (cuatro cajas) → 20 (D47a) → 21 (D53)

FASE 6 · OPERATIVA
  22 (KIID) → 23 (D47b) → 24 → 25

FASE 7 · CIERRE
  26 (Gate aplicado) → 27 → 1
```

**Regla del orden:** primero el lenguaje (Parte I), porque cada capítulo posterior se escribe
EN ese lenguaje. Escribir el cap. 11 antes que el 4 obligaría a reescribirlo.

## Las 3 decisiones que hay que aprobar antes de la primera línea

| # | Decisión | Origen |
|---|---|---|
| **1** | ✅ **RESUELTA (D78)** — modos de gestión · política/capital · dos vistas contables | Contradicciones 🔴 |
| **2** | ✅ **RESUELTA (D78)** — cap. 19 completo; cap. 4 solo el mapa módulo→régimen como hipótesis | Rúbrica dim. 11 |
| **3** | ✅ **APROBADO (D78)** — 27 capítulos / 6 partes + anexos | Este documento |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Creación.** PDF PMMA (40 págs., 34 §§) leído íntegro y auditado: valor por secciones, **10 contradicciones enumeradas sin corregir** (3 rojas: Robeco/Convicción, definición de Reserva, representación del overlay), crítica académica hostil con la respuesta honesta a la pregunta del tribunal, índice revisado de **27 capítulos en 6 partes**, mapa completo de las 34 secciones sin pérdidas, trazabilidad D1-D77 → capítulos y orden de redacción en 7 fases. **Nada del libro redactado. Ninguna arquitectura modificada** |
