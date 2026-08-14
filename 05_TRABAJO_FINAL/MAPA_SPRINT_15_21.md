# 🗺️ MAPA DEL SPRINT 15-21 — PREPARACIÓN SIN REDACCIÓN

## 14 de agosto de 2026 · Bloques A (15-18) y B (19-21)

> **Nada de este sprint está redactado.** Este mapa dice qué hay, qué falta y qué hay que
> calcular — sin inventar ningún resultado. **Precondición declarada:** las dos decisiones
> de `IMPACTO_DECISIONES_PRE_XRAY.md` *(PIMCO, Emergentes)* conviene cerrarlas antes del
> Bloque A, porque sus escenarios de impacto máximo regeneran el X-Ray sobre el que se
> escribe todo el bloque.

**Leyenda:** ✅ = ya disponible en el X-Ray oficial u otro documento del proyecto ·
🔧 = requiere cálculo nuevo · 📚 = requiere evidencia externa.

---

# BLOQUE A — RADIOGRAFÍA, COMPOSICIÓN, RIESGO Y CORRELACIONES (15-18)

## Capítulo 15 — El X-Ray oficial: metodología y salvedades

| | |
|---|---|
| **Pregunta que responde** | ¿Cómo se hizo la radiografía de la cartera y qué limitaciones tiene su lectura? |
| **Datos disponibles** | ✅ Informe Morningstar 13-ago *(12 posiciones, 100% del 97%)* · ✅ regla de lectura ×0,7693 *(países/sectores sobre la parte de acciones)* · ✅ reescalado 97%→100 con factor ×0,97 · ✅ tabla de conciliación real↔analizado *(fuente de verdad)* · ✅ las salvedades registradas *(clases proxy, cobre cubierto, fechas de datos)* |
| **Cálculos necesarios** | Ninguno — es el capítulo metodológico del bloque |
| **Evidencia externa** | 📚 Ninguna imprescindible *(la metodología Morningstar se describe por lo observado en el propio informe, sin atribuirle internals no publicados)* |
| **Gráficos** | Esquema del flujo cartera→reescalado→informe→conversión · tabla de salvedades |
| **Dependencias** | 🔴 **Las dos decisiones previas** *(si regeneran X-Ray, este capítulo describe el nuevo)* |
| **Huecos actuales** | Ninguno de contenido; solo la precondición |
| **Fran debe poder explicar** | Por qué el informe cubre el 97% y cómo se convierte *(×0,97)* · por qué «% de acciones» ≠ «% de cartera» *(×0,7693)* · qué es un proxy y qué se toma de él |

## Capítulo 16 — Composición: geografía, sectores, estilo y mayores posiciones

| | |
|---|---|
| **Pregunta que responde** | ¿Qué tenemos realmente — países, sectores, empresas — y coincide con lo que decidimos? |
| **Datos disponibles** | ✅ EEUU 66,41% de las acciones *(≈51,2% del patrimonio)* · ✅ los 10 países · ✅ sectores *(tecnología 26,70% de acciones, salud 15,97…)* · ✅ estilo *(P/B 3,48 · P/E 17,87)* · ✅ 10 mayores posiciones *(oro 7,22 · NVIDIA 2,82 · Apple 2,44…)* · ✅ distribución de activos *(acciones 77,01 · efectivo neto −1,90)* |
| **Cálculos necesarios** | 🔧 **Exposición emergente TOTAL** *(bloque 7% + contenido del All-World — el dato que los caps. 6 y 11 remiten aquí)* · 🔧 **exposición tecnológica auditada** con fuente/fecha/denominador *(cierra la cifra histórica retirada del cap. 6)* · 🔧 EEUU total con y sin el tilt *(cuánto añade el S&P 500 al ancla)* |
| **Evidencia externa** | 📚 Ninguna nueva *(todo sale del informe + desgloses de los fondos ya consultados)* |
| **Gráficos** | Mapa/barras de países · barras de sectores con la doble escala *(% acciones / % cartera)* · top-10 posiciones |
| **Dependencias** | Cap. 15 *(metodología)* · decisión Emergentes *(escenario C lo cambia)* |
| **Huecos** | Los tres cálculos 🔧 — factibles con datos ya en el repo |
| **Fran debe poder explicar** | «Tenemos ~la mitad del patrimonio en EEUU y es una decisión, no un accidente» · el 7% de Emergentes vs la exposición total · por qué el efectivo neto sale negativo *(derivados del fondo de renta fija — sin alarmismo)* |

## Capítulo 17 — Rentabilidad y métricas de riesgo

| | |
|---|---|
| **Pregunta que responde** | ¿Cómo se ha comportado esta composición y cuánto riesgo lleva — medido, no supuesto? |
| **Datos disponibles** | ✅ Las 21 cifras del informe: rentabilidad 3a 14,28% *(+1,31 vs índice)* · 5a 10,71% *(+2,14)* · volatilidad 9,61/9,94 · Sharpe 1,14/0,88 · alfa 2,77/3,42 · beta 0,84/0,78 · R² 93,77/92,72 · IR 0,50/0,64 · TE 3,00/3,74 · ✅ peores ventanas *(1 año −7,96%; ninguna ventana de 3/5 años negativa)* · ✅ salvedad del All-World a 5 años *(registrada: métricas 3a con confianza, 5a con advertencia)* |
| **Cálculos necesarios** | 🔧 **Sortino** *(pendiente de la rúbrica — necesita serie de retornos; declarar método)* · 🔧 qué métricas admiten agregación lineal y cuáles no *(desarrollo prometido por el cap. 6 §6.8)* |
| **Evidencia externa** | 📚 Definiciones citables de las métricas *(pueden resolverse con el glosario — anexo G)* |
| **Gráficos** | Tabla 3a/5a con el benchmark · barras de peores ventanas |
| **Dependencias** | Cap. 15 · decisión PIMCO *(escenario B altera las métricas)* |
| **Huecos** | Sortino · la salvedad 5a sigue PENDIENTE DE VERIFICACIÓN *(cómo agrega Morningstar cuando una posición no tiene serie completa — no afirmar)* |
| **Fran debe poder explicar** | Qué significan beta 0,84 y alfa en lenguaje llano · por qué usamos 3 años con confianza y 5 con salvedad · que rentabilidad pasada ≠ promesa |

## Capítulo 18 — Correlaciones, concentración y divisa

| | |
|---|---|
| **Pregunta que responde** | ¿Cuántas fuentes de comportamiento independientes hay de verdad, y qué pasa con el dólar? |
| **Datos disponibles** | ✅ Matriz de correlaciones del informe *(10 posiciones)*: S&P↔All-World **0,97** · oro↔Motor ~0,01 · monetario ~0 · Robeco↔Multifactor y parejas de Aceleración elevadas · ✅ concentración top-10 · ⚠️ ventana/frecuencia de la matriz **no documentadas por el informe** — publicar con esa salvedad |
| **Cálculos necesarios** | 🔧 **Riesgo de divisa cuantificado**: % del patrimonio con exposición económica a USD *(sumando fondos sin cubrir)* + sensibilidad simple *(«si el dólar cae X%, el efecto directo aproximado es…» — con supuestos declarados)* · 🔧 lectura funcional de la matriz *(funcional ≠ estadístico — cierra I4 del cap. 9)* |
| **Evidencia externa** | 📚 Ninguna imprescindible; 📚 opcional: referencia sobre correlaciones que suben en crisis *(si se afirma, citar)* |
| **Gráficos** | Matriz coloreada · mapa de «cuántas fuentes reales» · barra de exposición por divisa |
| **Dependencias** | Cap. 16 *(composición por divisa sale de sus desgloses)* · decisión PIMCO *(cambia la pata cubierta a EUR)* |
| **Huecos** | 🔴 **Todo el análisis de divisa es cálculo nuevo** · la ventana de la matriz |
| **Fran debe poder explicar** | «El 0,97 del Motor es la prueba del tilt, no un fallo» · «el oro es lo que menos se parece a todo lo demás» · cuánto pesa el dólar y por qué no lo cubrimos *(coste de cobertura, horizonte)* — sin prometer que no duela |

---

# BLOQUE B — CUATRO CAJAS, STRESS HISTÓRICO Y ESCENARIOS (19-21)

## Capítulo 19 — El marco macro: cuadrante crecimiento × inflación

| | |
|---|---|
| **Pregunta que responde** | ¿Qué cubre la cartera en cada clima económico — y hay alguna caja huérfana? |
| **Datos disponibles** | ✅ Solo el **mapa módulo→régimen del cap. 4 como HIPÓTESIS de diseño** *(sin validar)* · ✅ la estructura conceptual *(Browne/All Weather, cap. 8)* |
| **Cálculos necesarios** | 🔧 **TODO ES CONSTRUCCIÓN NUEVA:** definir las cuatro cajas · **datar históricamente** los regímenes *(qué años fueron qué caja — con criterio explícito: crecimiento e inflación vs expectativas)* · asignar cada módulo a su(s) caja(s) con justificación · verificar que ninguna caja queda huérfana *(la estanflación es la crítica)* |
| **Evidencia externa** | 📚 **Series macro históricas** *(inflación y crecimiento — FRED/OCDE/INE como fuentes primarias a citar)* · 📚 comportamiento por régimen de clases de activo *(citar, no afirmar de memoria)* |
| **Gráficos** | 🔑 **El cuadrante 2×2 con los módulos situados** *(el visual más importante de la Parte IV)* · línea temporal de regímenes datados |
| **Dependencias** | Ninguna interna al bloque — puede empezar en paralelo al Bloque A |
| **Huecos** | 🔴 **La dimensión 11 de la rúbrica entera: 0/5.** El capítulo ES el hueco |
| **Fran debe poder explicar** | Las cuatro cajas en 30 segundos con un dibujo · qué módulo defiende la estanflación *(oro/cobre + revisar linkers)* · que el mapa es diseño verificado con datos, no adivinación |

## Capítulo 20 — Stress por regímenes históricos

| | |
|---|---|
| **Pregunta que responde** | ¿Qué le habría pasado a esta cartera en 1973-74, 2000-02, 2008-09 y 2022 — con shocks auditados? |
| **Datos disponibles** | ⚠️ `D47a` **PROVISIONAL**: método verificado *(reproduce el −43,17% publicado)* pero **tres shocks heredados de bloques que cambiaron** *(Motor ACWI vs composición actual · Emergentes «EM+Japón» · Aceleración «solo small caps»)* · ✅ el −43,45% como cifra provisional declarada · ✅ peores ventanas del X-Ray *(insuficientes: solo 2015-2026)* |
| **Cálculos necesarios** | 🔧 **AUDITAR LOS SHOCKS** *(D47a — el pendiente rojo)*: shock por bloque coherente con la composición v1.0 · 🔧 los **cuatro episodios por régimen** con series largas *(el X-Ray no llega a 1973 ni 2000: hacen falta índices, no productos)* · 🔧 el caso **2022** *(acciones y bonos cayendo a la vez — el que rompe al 60/40)* |
| **Evidencia externa** | 📚 **Series históricas largas** *(retornos por clase de activo desde ~1970: Damodaran/Shiller como fuentes citables)* · 📚 caídas de los episodios con fuente |
| **Gráficos** | Barras por episodio y por módulo · la cascada del escenario severo |
| **Dependencias** | **Cap. 19** *(los episodios se eligen por régimen)* · decisión PIMCO *(cambia la pata de bonos en 2022)* |
| **Huecos** | 🔴 D47a entero · 🔴 los cuatro episodios · **prohibido publicar el −43,45% como definitivo** |
| **Fran debe poder explicar** | «Nuestra pérdida estimada en un escenario tipo 2008 es provisional y por qué» · qué pasó en 2022 y por qué nos importa · que el estrés es diseño, no predicción |

## Capítulo 21 — Escenarios de despliegue de Convicción

| | |
|---|---|
| **Pregunta que responde** | ¿Cómo puede evolucionar la capa de Convicción en 3 años según lo que ofrezca el mercado — sin prometer ninguno? |
| **Datos disponibles** | ✅ El alcance fijado *(D53/protocolo)*: cuatro escenarios — sin oportunidades · lento · central · gran dislocación · ✅ la mecánica de financiación *(aportación + Reserva, cap. 13)* · ✅ el techo del despliegue *(gradual por diseño; ~11 meses para el 14% completo)* |
| **Cálculos necesarios** | 🔧 **D53 entero**: la aritmética de cada escenario *(cuánto capital entra a la capa por año con la mecánica real)* · 🔧 el impacto proporcional en el presupuesto de alfa *(usando la regla acotada del cap. 12)* |
| **Evidencia externa** | 📚 Frecuencia histórica de correcciones del mercado *(si se cita, con fuente — es el dato «cada cuánto hay rebajas»)* |
| **Gráficos** | Las cuatro sendas de despliegue *(área apilada Motor ordinario/Convicción)* |
| **Dependencias** | Cap. 12 cerrado ✅ · cap. 13 cerrado ✅ · **NO depende de IDC concretos** *(escenarios de mecánica, no de empresas — pero sin Fecha Cero no puede ilustrarse con candidatas reales)* |
| **Huecos** | 🔴 D53 entero · la ilustración con candidatas espera a la Fecha Cero |
| **Fran debe poder explicar** | «No sabemos cuál escenario ocurrirá y no prometemos ninguno» · por qué el despliegue completo tarda ~un año de oportunidades · que Convicción al 0% en 3 años seguiría siendo un resultado válido |

---

# 📊 RESUMEN DEL SPRINT

| | Con el X-Ray existente | Cálculo nuevo | Evidencia externa |
|---|---|---|---|
| **15** | ✅ ~100% | — | — |
| **16** | ✅ ~70% | 🔧 3 cálculos *(EM total, tech auditada, EEUU con/sin tilt)* | — |
| **17** | ✅ ~80% | 🔧 Sortino + reglas de agregación | 📚 glosario |
| **18** | ✅ ~50% | 🔴 **divisa entera** + lectura funcional | 📚 opcional |
| **19** | ❌ ~5% | 🔴 **construcción completa** | 📚 series macro |
| **20** | ❌ ~10% | 🔴 **D47a + 4 episodios** | 📚 series largas |
| **21** | ✅ ~40% *(mecánica)* | 🔴 **D53 entero** | 📚 opcional |

**Orden natural:** decisiones previas → Bloque A *(15→16→17→18)* con el 19 arrancando en
paralelo *(no depende del X-Ray)* → 20 → 21. **El Bloque B es donde viven los tres rojos
de la rúbrica** *(dimensiones 5 y 11)*.
