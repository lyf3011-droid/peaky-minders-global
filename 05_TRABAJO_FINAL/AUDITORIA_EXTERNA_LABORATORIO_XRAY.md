# 🔬 INFORME DE AUDITORÍA EXTERNA DEL LABORATORIO X-RAY

## Peaky Minders Global 10Y · **v2** · 15 de agosto de 2026 · auditor metodológico externo

> **v2 — auditoría de la auditoría aplicada.** Se **retira** un hallazgo erróneo *(D-6)*, se
> **reformulan** dos que estaban sobredimensionados *(H-2, H-3)*, se **añade un bloqueo
> material no detectado en v1** *(H-4: commodities frente al capítulo 19)* y se acota el
> recuento de pruebas. **v1 se conserva en el historial de git.**

> **Nada se ha modificado.** Ni cartera oficial, ni Investment Book, ni capítulos, ni pesos,
> ni vehículos, ni decisiones Dxx. **PMMA Universal no se ha abierto.** No se han ejecutado
> nuevas pruebas X-Ray ni la validación histórica.
>
> **Convención de categorías, aplicada en todo el informe:** **[DATO]** medido por
> Morningstar o ficha · **[RESULTADO]** calculado o comparado por el laboratorio ·
> **[INTERPRETACIÓN]** inferencia · **[HIPÓTESIS]** pendiente de prueba · **[DECISIÓN]**
> aprobado. **Ninguna categoría se convierte en otra.**

---

# 0. Qué he leído y cómo lo he verificado

Los tres documentos, **íntegros**. Los tres PDF llegaron como archivo sin texto legible en
mi contexto, así que **extraje su contenido** *(PyMuPDF)* antes de auditarlos, en lugar de
opinar sobre documentos que no había leído.

| Fuente | Documento | Verificación realizada |
|---|---|---|
| **1** | `INFORME_COMPLETO.md` *(1.091 líneas)* | Leído íntegro |
| **2** | `FICHA_CARTERA_GANADORA.pdf` *(12 págs.)* | Extraído y **cotejado cifra a cifra contra el X-Ray 34** |
| **3** | Síntesis 29 pruebas *(15 págs.)* | Extraído y cotejado |
| **+** | `34_GANADOR_FINAL…pdf` *(4 págs.)* | **Fuente primaria: usada para verificar las otras dos** |

**Verificación de las 14 métricas del §9 de tu encargo contra el X-Ray oficial:** vol 3a
9,71 ✓ · vol 5a 10,21 ✓ · media 3a 14,71 ✓ · media 5a 11,06 ✓ · Sharpe 1,22 / 0,90 ✓ ·
alfa 3,64 / 3,65 ✓ · beta 0,83 / 0,80 ✓ · R² 91,31 / 92,16 ✓ · IR 3a 0,72 ✓ · TE 3a
3,39 ✓. **Las catorce coinciden exactamente con el informe oficial.**

## 0.1 ⚠️ Aclaración necesaria: el X-Ray publica DOS rentabilidades distintas

**[DATO] verificado en el X-Ray 34.** El informe contiene dos bloques con cifras de
rentabilidad que **no son el mismo campo**:

| Bloque del informe | 3 años | 5 años |
|---|---:|---:|
| **Rentabilidades Acumuladas** *(anualizado)* | **15,23** | **11,08** |
| **Estadísticas de Rentabilidad y Riesgo** *(«Medio»)* | **14,71** | **11,06** |

**Esto explica dos aparentes discrepancias del corpus y ninguna de las dos es un error:**
`INFORME_COMPLETO` usa el bloque de **Rentabilidades Acumuladas** cuando habla de
«rentabilidad anualizada» *(11,08; y 15,72 para la BASE a 3 años)*; la **FICHA** usa
**«Medio»** *(11,06)*. **Ambos son datos oficiales del mismo informe.**

⚠️ **Recomendación de redacción:** citar siempre **qué campo** se está usando. Un tribunal
que vea 11,06 y 11,08 en dos documentos del mismo trabajo preguntará, y la respuesta debe
ser inmediata.

---

# A. RESUMEN EJECUTIVO

**El laboratorio está metodológicamente por encima de lo que se ve en trabajos de este
nivel.** Tiene base fija, cambio único por prueba, criterios escritos antes de mirar,
**una prueba de control deliberada**, preservación de descartes, errores publicados y
límites declarados. La verificación externa contra MAPFRE y el cuadre de India por dos
caminos *(5,22 calculado vs 5,24 medido)* son trabajo serio.

**Y aun así, cuatro hallazgos impiden aprobar la candidata tal como está.**

> ## 🔴 **H-1 · La BASE del laboratorio no es la cartera oficial.**
> El Freno de la BASE v10 es **un ETF de bonos globales agregados al 9%**
> *(`IE00BF1QPL78`)*. El Freno oficial es **6% de fondo monetario en euros
> (`FR0000447823`) + 3% de renta fija flexible (`IE00B84J9L26`)**. **Son instrumentos
> distintos con duración, crédito y divisa distintos.** El CAMBIO 3 —financiar
> commodities «desde el Freno»— **se probó sobre un Freno que la cartera oficial no
> tiene**. La conclusión no es trasladable sin repetir la prueba.

> ## 🔴 **H-2 · La reclasificación de Robeco no puede aprobarse con la evidencia aportada.**
> **Error factual:** `INFORME_COMPLETO` justifica el cambio diciendo que *«su volatilidad
> (15,92) es la de un fondo de núcleo»*. **15,92 no es su volatilidad: es su rentabilidad
> media a 3 años.** Su volatilidad real es **9,88**.
> **Formulación del bloqueo:** *«La reclasificación de Robeco no puede aprobarse únicamente
> por correlaciones y volatilidad. Debe justificarse por función económica y reconciliarse
> además con el protocolo del macrobloque 47%.»*
> **Incompatibilidad de gobernanza:** el protocolo vigente fija **Motor 44 + Reserva 3 +
> Convicción 0 = 47%**. Reclasificar el 4% de Robeco a Motor lo llevaría a **48%** y **exige
> resolver expresamente esa gobernanza antes de cualquier ejecución**.

> ## 🔴 **H-3 · El criterio de selección no es suficiente por sí solo.**
> Se eligió por **R² a la baja y tracking error al alza**. **Ambas métricas capturan
> diferenciación respecto del benchmark y están parcialmente relacionadas; no constituyen
> criterios independientes suficientes de mejora. Deben evaluarse junto con volatilidad,
> drawdown/estrés, función económica, concentración, costes y evidencia independiente.**
> Con 33 configuraciones examinadas sobre la misma muestra, **la objeción de *data
> snooping* no queda neutralizada por estas dos métricas**.

> ## 🔴 **H-4 · La narrativa de commodities contradice el capítulo 19 ya cerrado.**
> `INFORME_COMPLETO` presenta un cuadro de amenazas en el que **«shock de inflación → nadie
> → ❌ no cubierto»** y llama a las materias primas **«el seguro que faltaba»**. **Eso no es
> compatible con el capítulo 19**, que encontró que **el oro presentó comportamiento
> relativo medio favorable en las dos cajas de inflación alta** y **consistencia mayoritaria
> entre episodios en crecimiento débil + inflación alta**.
> **La cartera no estaba descubierta frente a la inflación: tenía una pata de oro con apoyo
> histórico.** Presentar las commodities como el primer o único seguro **ignora evidencia
> propia ya validada y cerrada**. *(Formulación correcta en D-9.)*

**Veredicto:** 🟡 **NECESITA CORRECCIONES ANTES DE VALIDAR** *(desarrollado en §N)*.

---

# B. RECONSTRUCCIÓN DEL PROCESO

```
BASE v10 (12 posiciones + 3% reserva)
   │
   ├─ A · 01-02  commodities ampliadas ................ 2 descartes
   ├─ B · 03-06  rediseño de Defensivos ............... 4 descartes  ← incluye el mejor descarte (biotech)
   ├─ C · 07-11  Aceleración, 1ª ronda ................ 5 descartes  ← empate → no tocar (regla 4)
   ├─ D · 12-15  tanda de IA .......................... 4 descartes  ← 1 a lista de espera por histórico
   ├─ E · 16-18  Robeco + Asia + control .............. 3 descartes + RECLASIFICACIÓN de Robeco
   │                                                     └─ prueba 18 = CONTROL metodológico
   ├─ F · 19-22  búsqueda de huecos ................... 3 descartados sin gastar X-Ray + INDIA SUPERA
   ├─ G · 23-26  ¿y China? ............................ China 0% + corrección del error del 20%
   ├─ H · 27-28  dosis de India ....................... A100 (4%) domina
   └─ I · 30-33  el seguro que faltaba ................ commodities desde Freno (31) elegida
                                                         33 = tirada diagnóstica, NO es cartera
   ▼
34 · CANDIDATA FINAL — India 4% + commodities 1%
```

**Cuatro supervivientes de ~33 pruebas.** Dos son cambios reales de producto *(India,
commodities)*, uno es reclasificación contable *(Robeco)* y otro es cambio de clase del
mismo fondo *(Emergentes)*.

---

# C. FORTALEZAS METODOLÓGICAS — lo que está realmente bien hecho

| # | Fortaleza | Por qué cuenta |
|---|---|---|
| **C1** | **La prueba de control (18 · Polar Tecnología)** | Introducir a propósito el candidato con **mejores números retrospectivos** para comprobar que el método no lo elige. **Es la mejor pieza del laboratorio** y muy poco frecuente en trabajos de este nivel |
| **C2** | **Rechazar biotech (prueba 05) con Sharpe +0,07 y alfa +0,83** | Rechazar un ganador numérico por incumplimiento funcional demuestra que la regla «función antes que producto» **se aplicó de verdad**, no solo se enunció |
| **C3** | **Regla de empate a favor de lo existente (prueba 11)** | Reduce la rotación espuria y el sesgo de acción |
| **C4** | **Descartes sin gastar prueba** *(momentum, defensa europea, equiponderado)* | Aplicar el criterio de histórico insuficiente **también a la idea que más gustaba** *(defensa europea: 0% EEUU, 0% tecnología)* es coherencia poco común |
| **C5** | **Errores conservados y explicados** *(6 documentados)* | El error 3 —el «20% de India» que era China— **se detectó porque se pidió verificarlo**. Eso es control activo, no suerte |
| **C6** | **Cuadre de India por dos caminos** *(5,22 calculado vs 5,24 medido)* | **[RESULTADO]** verificado por mí: 6,80% de la parte en acciones × 77,02% = 5,24% del patrimonio. **Cuadra** |
| **C7** | **Validación externa del motor** *(MAPFRE, 4 productos, coincidencia a la centésima)* | Demuestra que la herramienta reproduce la fuente y no calcula nada propio |
| **C8** | **La síntesis de 29 pruebas cita literatura pertinente** *(White 2000 sobre data snooping; Bailey y López de Prado 2014 sobre inflación del Sharpe; DeMiguel-Garlappi-Uppal 2009 sobre 1/N)* | **El laboratorio se cita a sí mismo la objeción principal.** Eso es honestidad intelectual, no adorno |
| **C9** | **Tres controles de integridad del informe** *(cobertura 100%, presencia por nombre, cuadre del % en acciones)* | Invalidaron **cuatro informes** que parecían correctos |

---

# D. DEBILIDADES — lo que criticaría un profesor

## 🔴 D-1 · La BASE no es la cartera oficial *(hallazgo principal)*

| | Cartera oficial *(fuente de verdad, D73-D77)* | BASE v10 del laboratorio |
|---|---|---|
| **Freno 9%** | **6% AXA Trésor Court Terme** *(monetario EUR)* + **3% PIMCO GIS Income** *(renta fija flexible, cubierta)* | **9% SPDR Global Aggregate Bond EUR Hedged** `IE00BF1QPL78` |
| **Emergentes** | Clase S `IE000QAZP7L2` *(proxy en X-Ray: clase D `IE00BYWYCC39`)* | Clase Instl `IE00B3D07F16` |

**Consecuencias, en orden de gravedad:**

1. **El CAMBIO 3 pierde su base.** «Financiar 1% desde el Freno» significa, en la BASE del
   laboratorio, **quitar 1% de bonos agregados globales**. En la cartera oficial
   significaría quitarlo **del monetario o del PIMCO** — instrumentos con duración,
   crédito y comportamiento distintos. **La correlación −0,51 entre commodities y «bonos»
   es contra el SPDR, no contra el Freno oficial.**
2. **El X-Ray de la candidata no es comparable con el X-Ray oficial** *(`XRAY_OFICIAL_2026-08-13`)*,
   porque difieren en dos posiciones de partida.
3. **No es un error del laboratorio si la BASE v10 se declaró como tal** — pero **en ningún
   punto de los tres documentos se advierte de esta diferencia**, y el lector natural
   asume que BASE v10 = cartera oficial.

## 🔴 D-2 · Error factual en la justificación de la reclasificación de Robeco

`INFORME_COMPLETO` línea 377: *«su volatilidad (15,92) es la de un fondo de núcleo, no la
de un acelerador»*. **[DATO]** de la ficha y del X-Ray: Robeco **Media 3a = 15,92 · Volat.
3a = 9,88**. Se ha tomado la columna de rentabilidad por la de volatilidad.

**Qué implica el dato correcto —y qué no.** Robeco es **la posición de renta variable menos
volátil de la cartera** *(9,88 frente a 11,52 del All-World y 13,08 del S&P 500)*. Una
volatilidad de ese orden **es compatible con —e incluso refuerza descriptivamente— un perfil
de riesgo más parecido al del núcleo que al de un acelerador**.

⚠️ **Pero eso no demuestra que Robeco deba pertenecer al Motor.** Un perfil de riesgo
compatible no es una función económica. El bloqueo se formula así:

> **La reclasificación de Robeco no puede aprobarse únicamente por correlaciones y
> volatilidad. Debe justificarse por función económica y reconciliarse además con el
> protocolo del macrobloque 47%.**

**Incompatibilidad de gobernanza, explícita:** el protocolo vigente fija **Motor 44 +
Reserva 3 + Convicción 0 = 47%**. Con Robeco reclasificado, **Motor = 48%** y la identidad
deja de cumplirse. **Debe resolverse antes de cualquier ejecución**, no después.

## 🔴 D-3 · El criterio de decisión no es independiente de la hipótesis

**Ambas métricas capturan diferenciación respecto del benchmark y están parcialmente
relacionadas entre sí; no constituyen criterios independientes suficientes de mejora.**
Un R² más bajo y un TE más alto indican que la cartera se separa del índice, **no que la
separación sea beneficiosa**.

**Deben evaluarse junto con:** volatilidad · drawdown y comportamiento en estrés · función
económica del módulo · concentración · costes · y evidencia independiente fuera de la
ventana de decisión. **Ninguna de esas seis dimensiones pesó en la selección del ganador**,
y eso es lo que hace que el criterio, por sí solo, no cierre el argumento frente a 33
configuraciones examinadas.

## 🟠 D-4 · Colisión con la gobernanza del capítulo 5

Reclasificar Robeco a Motor lleva **Motor de 44% a 48%**. Pero la **bolsa del 47%** del
capítulo 5 *(D78/D80)* es una identidad de gobernanza: **44 Motor ordinario + 3 Reserva +
0 Convicción = 47**. **Con Motor 48 esa identidad deja de cuadrar** y habría que
reformular la vista C completa.

**[INTERPRETACIÓN]** No invalida la reclasificación; **obliga a decidir si el 47% se
define sobre el Motor «ordinario indexado» o sobre el módulo Motor completo.** El
laboratorio no lo menciona.

## 🟠 D-5 · El recuento de pruebas es inconsistente

| Documento | Dice |
|---|---|
| Síntesis *(F-3)* | **«29 pruebas»** · «de 29, 26 no aportaron evidencia» · **«3 decisiones sobrevivieron»** |
| `INFORME_COMPLETO` *(F-1)* | **«LAS 33 PRUEBAS»** · «de 33, cuatro cosas cambian» · «29 de 33 confirmaron» · pero también **«el único candidato de 29»** |
| Carpeta `xrays\` | **35 archivos** *(00-34)*, de los que 00 es la base, 33 es **diagnóstico y no cartera**, 34 es la configuración final |

**[INTERPRETACIÓN] revisada:** **no es una contradicción material**, sino **falta de
nomenclatura**. Los tres documentos describen fases distintas de un proceso que creció, y
cada uno contó lo que existía cuando se escribió.

### Nomenclatura única propuesta *(para eliminar la ambigüedad)*

| Nombre propuesto | Contenido | Archivos |
|---|---|---|
| **BASE v10** | Cartera de referencia del laboratorio *(no es la cartera oficial — ver D-1)* | `00` |
| **FASE 1 — 29 pruebas** | Bloques A-H: sustituciones, dosis de India y China | `01`-`29` |
| **FASE 2 — ampliación commodities** | Bloque I: tres fuentes de financiación | `30`-`32` |
| **TIRADA DIAGNÓSTICA** | ⚠️ **No es una cartera.** Solo para leer correlaciones | `33` |
| **CANDIDATA FINAL** | Configuración resultante, confirmada por X-Ray | `34` |

**Con esta nomenclatura, las tres cifras del corpus dejan de contradecirse:** «29 pruebas»
= FASE 1 · «33 pruebas» = FASE 1 + FASE 2 + diagnóstica · «35 archivos» = todo lo anterior
más base y candidata. **Recomiendo adoptarla en los tres documentos.**

## ⬜ D-6 · **RETIRADO — no había discrepancia**

*(Hallazgo de la v1, eliminado tras verificación.)* Se señaló como error que
`INFORME_COMPLETO` usara **11,08** y la FICHA **11,06** para la rentabilidad a 5 años.
**No es un error: son dos campos distintos del mismo informe oficial** — *Rentabilidades
Acumuladas · 5 años anualizado = 11,08* frente a *Estadísticas · Medio 5a = 11,06*
**(verificado en el X-Ray 34, §0.1)**. Cada documento usa uno de forma consistente.

**Queda solo una recomendación de redacción, no un hallazgo:** citar siempre qué campo se
está usando.

## 🟠 D-7 · El «peor trimestre» empeora, y es la métrica más cercana a lo que se promete

**[DATO]** Peor trimestre: BASE −15,99 → candidata **−16,44** *(−0,45)*. La candidata
introduce commodities **como seguro** y **empeora la única métrica de tensión disponible**.

El informe lo declara con honestidad y lo explica *(las commodities no protegen del
pánico)*. **[INTERPRETACIÓN] mía:** esa explicación es plausible, pero **convierte el
argumento en no falsable con los datos disponibles** — si la protección no aparece ni en
el peor trimestre ni en el peor año, no hay en todo el X-Ray ninguna métrica que pueda
mostrarla.

## 🔴 D-9 · La narrativa de commodities contradice el capítulo 19 *(bloqueo nuevo)*

**Lo que dice `INFORME_COMPLETO`** *(bloque I)*:

| Amenaza | Quién protege | ¿Cubierta? |
|---|---|---|
| Shock de crecimiento | Freno | ✅ |
| Miedo monetario | Oro | ✅ |
| **Shock de inflación** | **nadie** | ❌ |

…y titula el bloque **«El seguro que faltaba»**.

**Lo que dice el capítulo 19, cerrado y validado** *(D97, D103)*: **el oro presentó
comportamiento relativo medio favorable en las dos cajas de inflación alta**, y **en
crecimiento débil + inflación alta mostró además consistencia mayoritaria entre episodios**
— bajo dos clasificadores y dos convenciones de precio. **La evidencia apoya exclusivamente
la pata de oro, no el módulo Activos Reales completo.**

> ### 🔴 **La casilla «shock de inflación → nadie» es incorrecta según la evidencia propia
> ### del trabajo.** No es que la cartera careciera de cobertura de inflación: **tenía la
> ### única pata con apoyo histórico contrastado de todo el capítulo 19.**

**Formulación que debe sustituir a la narrativa actual:**

> **La cartera ya dispone de una pata de oro con apoyo histórico en entornos de inflación
> alta. La hipótesis de commodities es que una cesta amplia podría añadir una segunda
> fuente de comportamiento diferenciada frente a determinados shocks inflacionarios o de
> oferta. Esa función adicional todavía debe validarse históricamente.**

**Por qué es un bloqueo y no una cuestión de estilo:** la prueba 30 —financiar commodities
**desde el oro**— se descartó porque *«quitas un activo descorrelacionado para meter otro»*.
**Con la narrativa corregida, esa prueba cambia de sentido**: no se trata de sustituir un
seguro por otro, sino de decidir **si la segunda fuente añade algo sobre la primera, que ya
tiene apoyo**. Es una pregunta distinta y **no se ha respondido**.

## 🟡 D-8 · Otras

**D-8a** · **La «lista de espera» no tiene fecha de revisión** *(WPAI, defensa europea,
equiponderado)*: sin plazo, es un descarte con otro nombre.
**D-8b** · **Coste sin verificar en el 10% de la cartera** *(Salud y Bitcoin, n/d)* — bien
declarado, pero el coste total publicado *(0,19%)* cubre solo el 87%.
**D-8c** · **Robeco aporta el 31% del coste verificado pesando el 4%** *(FICHA)*. El
laboratorio lo publica como dato sin valoración, **pero no lo cruza con la reclasificación
a Motor**: un Motor con una pata al 1,46% es una decisión de coste, no solo de etiqueta.
**D-8d** · **Dos posiciones replican por swap** *(commodities y cobre)* — riesgo de
contrapartida declarado en la FICHA, **ausente en `INFORME_COMPLETO`**.
**D-8e** · **Formulación a corregir:** `INFORME_COMPLETO` lista como sacrificio *«materias
primas: sin retorno real esperado»*. Es una afirmación más fuerte de lo que puede
sostenerse. **Formulación correcta:** *«No se incorpora bajo una hipótesis de crecimiento
productivo comparable a la renta variable; su eventual inclusión se justificaría por función
de diversificación/cobertura y no por una previsión de rentabilidad superior.»*

---

# E. SESGOS POTENCIALES

| Sesgo | Exposición del laboratorio | Mitigación existente | Suficiencia |
|---|---|---|---|
| **Data snooping / multiple testing** | 🔴 **Alta** — 33 configuraciones sobre la misma muestra | Criterios previos · función antes que producto · control · descartes conservados | ⚠️ **Insuficiente.** Ver §E.1 |
| **Selección retrospectiva** | 🟠 Media | Regla explícita de no elegir por rentabilidad | ✅ Aplicada con rigor *(pruebas 05 y 18)* |
| **Ventana temporal** | 🔴 **Alta** | Se publican 3a y 5a | ⚠️ **Solo dos ventanas, ambas terminando en el mismo mes.** No hay rolling ni submuestras |
| **Dependencia de proveedor único** | 🟠 Media | Declarado como limitación | ⚠️ La verificación MAPFRE **no es independiente**: MAPFRE también usa Morningstar |
| **Correlaciones inestables** | 🔴 **Alta** | Declarado *(«en crisis suben todas»)* | ⚠️ Ninguna medición en submuestras de crisis |
| **Sesgo de supervivencia del vehículo** | 🟡 Baja-media | — | India y commodities existen hoy; los ETF que cerraron no están en el universo |
| **Sesgo de confirmación en la narrativa** | 🟠 Media | Sacrificios publicados sin maquillar | ⚠️ El lenguaje del ganador *(«el descubrimiento que decide el bloque»)* es más fuerte que la evidencia |

## E.1 Por qué las mitigaciones **no bastan** contra el multiple testing

**[INTERPRETACIÓN]** Las seis reglas del laboratorio reducen el riesgo de elegir por
**rentabilidad** — y lo hacen bien. **No reducen el riesgo de elegir por diversificación
aparente**, que es exactamente lo que se hizo.

Tres razones concretas:

1. **El criterio ganador (R² / TE) favorece mecánicamente a cualquier candidato exótico**
   *(D-3)*. Con 33 intentos, encontrar uno que baje el R² 1,48 puntos no requiere que sea
   bueno: requiere que sea distinto.
2. **Las magnitudes son pequeñas frente al ruido de estimación.** Δvol −0,07, ΔSharpe
   +0,01 a 5 años, Δalfa +0,06. **Ninguna viene con intervalo de confianza ni error
   estándar.** Con 36 y 60 observaciones mensuales, esas diferencias son estadísticamente
   indistinguibles de cero.
3. **No hay corrección por número de pruebas** *(ni Bonferroni, ni White's Reality Check,
   ni deflated Sharpe)* — y la propia síntesis **cita a White (2000) y a Bailey y López de
   Prado (2014) sin aplicar ninguno de los dos**. Citar la objeción no es responderla.

---

# F. AUDITORÍA DE LOS CUATRO CAMBIOS

## CAMBIO 1 · Robeco: Aceleración → Motor

| Aspecto | Resultado |
|---|---|
| **Evidencia a favor** | **[DATO]** ρ(Robeco, All-World) = 0,69 y ρ(Robeco, Small Caps) = 0,81 · es un fondo de **renta variable global** *(no un satélite temático)* · **[DATO]** ρ con Consumo básico 0,70 · **[INTERPRETACIÓN]** su comportamiento es el de una cartera amplia con sesgo *value*, no el de una fuente de retorno ajena al núcleo |
| **Evidencia en contra** | 🔴 **La justificación publicada usa un dato equivocado** *(D-2: 15,92 es rentabilidad, no volatilidad)* — aunque **la volatilidad real (9,88) es compatible con un perfil de riesgo de núcleo**, un perfil compatible **no es una función económica** · **El argumento «correlaciona más con Small Caps que con el índice» es lógicamente reversible**: correlacionar 0,81 con su compañero de bloque argumenta **redundancia dentro de Aceleración**, no pertenencia al Motor · 🔴 **Incompatible con el macrobloque 47%** mientras no se resuelva la gobernanza |
| **Evidencia que falta** | Contribución al riesgo · solapamiento de posiciones subyacentes con el Motor *(el X-Ray puede darlo y no se usa)* · comportamiento en submuestras · criterio explícito y previo de qué correlación define «núcleo» |
| **Principal riesgo** | **Reclasificar por correlación convierte a PMMA en una taxonomía estadística.** El capítulo 4 dice literalmente lo contrario: la función la fija **la tesis**, no el instrumento ni su comportamiento *(«separación funcional ≠ separación estadística», limitación L3)* |
| **Confianza actual** | 🟡 **Media-baja** |
| **Veredicto** | ⚠️ **NO APROBAR COMO ESTÁ.** **La reclasificación no puede aprobarse únicamente por correlaciones y volatilidad: debe justificarse por función económica y reconciliarse con el protocolo del macrobloque 47%.** La conclusión puede acabar siendo correcta; la evidencia publicada no la sostiene |

## CAMBIO 2 · Europe Multifactor 4% → India 4%

| Aspecto | Resultado |
|---|---|
| **Evidencia a favor** | **[DATO]** El europeo correlaciona **0,91 con Robeco** y **0,71 con Small Caps**: **su propio bloque estaba cogido de la mano** · **[DATO]** India: 0,27 / 0,31 / 0,44 con All-World · **[DATO]** composición genuinamente distinta *(Emergentes 44,2% tecnología vs India 8,3%; India 27,4% financieras)* · **[DATO]** ρ(India, Emergentes) = 0,34 **es menor que** ρ(Emergentes, índice mundial) = 0,74 — **India no es «más emergentes»** · **[DATO]** único candidato que **baja** la volatilidad · **[RESULTADO]** cuadre de India efectiva por dos caminos ✓ · **[DATO]** coste 0,19% frente al 2,43% del fondo Goldman |
| **Evidencia en contra** | **Concentración:** India pasa a ser **el 2.º país** de la cartera *(5,24%)* · **divisa:** rupia sin cubrir, **no cuantificada en ningún documento** · **riesgo país** concentrado en un solo mercado emergente con gobernanza propia · **se pierde la única posición europea dedicada** *(Europa baja de 8,9% a 5,6%)* · **valoración:** el mercado indio ha cotizado con múltiplos elevados frente a otros emergentes — **[DATO] ausente en los tres documentos** · alfa 3a −0,31 e IR 3a −0,22 |
| **Evidencia que falta** | 🔴 **Correlación en submuestras** *(la de 3-5 años puede no sobrevivir a una crisis global)* · 🔴 **valoración de partida** *(PER/PB de India vs alternativas)* · **rendimiento en 2008 y 2013** *(el «taper tantrum» golpeó a India de forma específica)* · **contribución al riesgo**, no solo correlación · **efecto divisa cuantificado** |
| **Principal riesgo** | **Que la baja correlación de India sea un artefacto de la ventana 2021-2026** —un periodo en que India tuvo un ciclo doméstico desacoplado— **y desaparezca justo en la crisis global en que se necesita** |
| **Confianza actual** | 🟢 **Media-alta en el diagnóstico** *(el europeo era redundante: 0,91 es difícil de discutir)* · 🟡 **media en la solución** *(que el sustituto deba ser India)* |
| **Veredicto** | 🟡 **APROBABLE CONDICIONADO.** El problema detectado es real y bien documentado. **La elección del sustituto necesita validación fuera de la ventana** *(§K)*. **Alternativas no exploradas que un profesor preguntará:** ¿por qué no reducir Aceleración a una sola pata? ¿por qué no un factor value/quality no europeo? ¿por qué no small caps emergentes? |

## CAMBIO 3 · Freno 9% → 8% bonos + 1% commodities

| Aspecto | Resultado |
|---|---|
| **Evidencia a favor** | **[DATO]** Correlación negativa frente a **las nueve posiciones de renta variable, sin excepción** *(−0,07 a −0,39)* · **[DATO]** ρ(commodities, bonos) = **−0,51**, el valor más bajo de la matriz · **[DATO]** ρ(commodities, oro) = **0,20**: **no duplican** · **[RESULTADO]** la prueba 31 es **la única limpia** *(la parte en acciones queda idéntica, 77,02%)*, frente a la 32 que mezcla dilución · **[RESULTADO]** financiado desde oro **empeora** *(R² sube)* y desde Freno **mejora**: el laboratorio **probó su propia alternativa y la descartó** |
| **Evidencia en contra** | 🔴 **D-1: se financió desde un Freno que la cartera oficial no tiene** · 🔴 **D-9: la premisa de partida es incorrecta** — el cuadro «shock de inflación → nadie» contradice el capítulo 19, que **sí encontró apoyo para la pata de oro en las dos cajas de inflación alta**. La pregunta correcta no es «¿falta un seguro?», sino **«¿añade la cesta amplia algo sobre el oro, que ya tiene apoyo?»** — y esa pregunta no se ha respondido · 🔴 **la única evidencia de la función anti-inflación es 2022** · **[DATO]** el peor trimestre **empeora 0,45** · **1% aporta 0,28 puntos ante un +28%** · el propio laboratorio descartó posiciones del 1% como «residuo, no arquitectura» *(bloque H)* |
| **Evidencia que falta** | 🔴 **Comportamiento en más de un episodio inflacionario** *(1973-75, 1979-81 · el capítulo 19 ya tiene el marco para identificarlos)* · **la correlación −0,51 con bonos medida en submuestras** · **coste real de rolar futuros** *(contango/backwardation)*, ausente en los tres documentos · **por qué 1% y no 2% o 3%** — no hay prueba de dosis, cuando **sí la hubo para India** |
| **Principal riesgo** | **Confundir financiación con clasificación** *(tu propia pregunta, y es la correcta)*. La ubicación en Freno se justifica por **función declarada** *(«dos seguros contra dos amenazas»)*, pero **la evidencia aportada es de correlación, no de función**. Y con 1% de peso, **la decisión es simbólica en la cartera y sustantiva solo en la arquitectura** |
| **Confianza actual** | 🔴 **Baja** |
| **Veredicto** | 🔴 **NO APROBAR.** Tres bloqueos: **(a)** la base de financiación no es la real *(D-1)*; **(b)** un solo episodio no sostiene una función; **(c)** falta prueba de dosis. **La asimetría de rigor frente a India es la crítica más fácil de un tribunal**: a India se le exigieron cuatro dosis y a commodities ninguna |

## CAMBIO 4 · Emergentes: cambio de clase

| Aspecto | Resultado |
|---|---|
| **Evidencia a favor** | **[DATO]** Mismo fondo, misma cartera, mismo índice; solo cambia la clase · **[DATO]** coste 0,32% → **0,16%** · mantiene la traspasabilidad fiscal · **[RESULTADO]** es el cambio de mayor certeza del laboratorio |
| **Evidencia en contra** | Ninguna sustantiva |
| **Evidencia que falta** | 🔴 **La confirmación de que la clase de destino es CONTRATABLE** para plataforma, tipo de inversor e importe. ⚠️ **Y aquí hay un choque con el libro:** la fuente de verdad de la cartera **marca `IE000QAZP7L2` como «candidato», DECISIÓN PENDIENTE**, con tres requisitos sin cumplir *(VETO 0 de contratabilidad, cierre formal y documentación primaria)*. **El laboratorio lo presenta como «cambio 4 aprobado»; el libro lo tiene como pendiente** |
| **Principal riesgo** | Que la clase barata **no sea contratable** y el cambio no exista |
| **Confianza actual** | 🟢 **Alta en la equivalencia** · 🔴 **nula en la accesibilidad, que no se ha verificado** |
| **Veredicto** | 🟢 **APROBAR sujeto al VETO 0.** Además, **tres ISIN distintos circulan para «el mismo fondo»** en el corpus: `IE00B3D07F16` *(proxy del laboratorio)*, `IE00BYWYCC39` *(proxy del X-Ray del libro)* e `IE000QAZP7L2` *(destino)*. **Hay que fijar cuál es cuál antes de escribir nada** |

---

# G. AUDITORÍA DE MÉTRICAS — interpretaciones excesivas encontradas

| Métrica | Frase del corpus | Problema | Formulación correcta |
|---|---|---|---|
| **R²** | *«**Más BAJO = más diversificado**»* *(glosario de `INFORME_COMPLETO`)* | 🔴 **Interpretación excesiva.** R² mide **qué parte de la varianza explica el índice**, no diversificación. Una cartera con un único activo exótico tendría R² bajísimo y **cero** diversificación | «Menor R² indica menor proporción de variación explicada por el índice de referencia. Es **compatible** con mayor diferenciación, **no equivalente** a ella» |
| **R²** | *«La idea más importante de todo el trabajo: R² bajo y TE alto significan que la cartera tiene vida propia»* | 🔴 **El criterio de decisión elevado a tesis.** Ver D-3 | «Son indicadores de **diferenciación frente al índice**, no de calidad de la cartera» |
| **Tracking error** | *«Más ALTO = más independiente»* | 🟠 Excesiva. Mayor TE = mayor desviación, **en ambas direcciones**. Un TE alto por un activo que cae solo cuando el índice sube es peor, no mejor | «Mayor desviación respecto del índice; debe interpretarse junto con riesgo, retorno y función» |
| **Sharpe** | *«Sharpe 5 años **mejora** (+0,01)»* usado como argumento a favor | 🔴 **+0,01 es ruido.** Sin intervalo de confianza no significa nada; **Bailey y López de Prado (2014), citado por el propio laboratorio**, existe precisamente para esto | «Diferencia no distinguible de cero con la muestra disponible» |
| **Alfa** | *«el alfa mejora (+0,06)»* a 5 años | 🔴 Igual: +0,06 con 60 observaciones no es evidencia. Además **el alfa depende del índice elegido** *(RV Global Cap. Grande Blend)*, que **no es el benchmark natural de una cartera con 23% de no-acciones** | «Alfa frente a un índice de renta variable global; la cartera tiene 23% en activos no accionariales, lo que **infla mecánicamente el alfa**» |
| **Beta** | 0,83 presentada sin comentario | 🟠 La beta baja **refleja sobre todo el 23% no accionarial**, no habilidad | Declararlo |
| **Correlación** | *«Correlación negativa contra toda la renta variable, sin una sola excepción»* | 🟠 **[DATO]** correcto. Pero se usa como **[INTERPRETACIÓN]** de protección | «Relación histórica media en la ventana medida. No implica protección en un episodio futuro concreto» |
| **Volatilidad** | *«baja la volatilidad»* como mérito de India | 🟠 −0,07 sobre 9,78 es **0,7% relativo**: dentro del error de medición | Declarar la magnitud relativa |

## G.1 El problema del índice de referencia — no señalado en ningún documento

**[DATO]** El X-Ray compara contra **«RV Global Cap. Grande Blend»**, un índice de renta
variable pura. Alfa, beta, R², TE e IR de **toda** la cartera están calculados contra un
índice que **no incluye bonos, oro, bitcoin ni materias primas**, teniendo la cartera un
**23% en activos no accionariales**.

> **Tratamiento correcto:** el alfa de Morningstar es **una estadística descriptiva
> condicionada al benchmark**, no evidencia autónoma de habilidad ni de superioridad. Con
> esta composición, el alfa positivo y la beta baja reflejan **en buena parte la mezcla de
> activos**.

**Ninguno de los tres documentos lo advierte**, y es de las primeras cosas que preguntará un
profesor.

---

# H. AUDITORÍA DE LA MATRIZ AMPLIADA

## H.1 ¿Es defendible el método de las tiradas diagnósticas?

> ### ✅ **Sí. El argumento matemático es correcto.**

**[DATO]** La correlación de Pearson entre dos series de rendimientos mensuales
`ρ(X,Y) = Cov(X,Y)/(σx·σy)` es **una propiedad del par de series**. Los pesos de cartera
no entran en la fórmula. Inflar un activo del 1% al 9,28% **no puede alterar su
correlación con otro activo**.

**Y la verificación empírica está bien hecha:** **[RESULTADO]** nueve parejas compartidas
entre tiradas con pesos muy distintos devolvieron **el mismo valor sin variar una
centésima** *(S&P↔All-World 0,97 en 5 tiradas; S&P↔Oro −0,07 en 4; commodities↔India
−0,39 en 2)*. Eso convierte un supuesto en evidencia.

**Además, verifiqué las filas 1-10 de la FICHA contra el X-Ray 34 y coinciden exactamente.**

## H.2 Limitaciones que el método **no** salva

| # | Limitación | Consecuencia |
|---|---|---|
| **H-a** | 🔴 **La ventana de estimación no está documentada.** Morningstar no publica sobre cuántos meses calcula la matriz | **Si la ventana es el histórico común disponible, cambia según los constituyentes de cada tirada.** Que nueve parejas coincidieran es tranquilizador **pero no lo prueba**: esas parejas tenían histórico largo en todas las tiradas. **Es la comprobación que falta** |
| **H-b** | **Correlación media ≠ correlación condicional** | Una ρ media de −0,39 es compatible con ρ **positiva** en las caídas. **Nada en la matriz habla de comportamiento en crisis** |
| **H-c** | **13 posiciones = 78 pares**, estimados sobre ~36-60 observaciones | Error estándar apreciable. **Ningún valor lleva intervalo de confianza** |
| **H-d** | **Las tiradas diagnósticas no son carteras** — bien declarado | ✅ Riesgo de confusión bien gestionado *(el archivo 33 se llama literalmente `NO-ES-CARTERA`)* |

## H.3 Qué **no** permite concluir la matriz

**No permite concluir que la cartera esté diversificada**, solo que ciertos pares se
mueven distinto **en promedio, en el pasado reciente**. La diversificación depende de
**pesos × correlaciones × volatilidades**, y la matriz solo aporta el segundo factor.

---

# I. AUDITORÍA INDIA — hipótesis formal

> ## **H-INDIA**
> *«La sustitución de una exposición europea multifactor por una exposición a renta
> variable india de igual peso **reduce la redundancia interna del bloque Aceleración**,
> medida como correlación con las demás posiciones de la cartera, **sin aumentar el riesgo
> total**, y esa reducción **persiste fuera de la ventana 2021-2026**.»*

**Descomposición en tres afirmaciones independientes, porque tienen fuerza distinta:**

| # | Sub-hipótesis | Estado actual |
|---|---|---|
| **I-1** | El Europe Multifactor era redundante *(ρ 0,91 con Robeco, 0,71 con Small Caps)* | 🟢 **Bien sostenida.** Es el hallazgo más sólido del laboratorio |
| **I-2** | India presenta correlaciones sustancialmente menores *(0,27 / 0,31 / 0,44)* | 🟢 **[DATO] verificado** en la ventana medida |
| **I-3** | Esa diferencia **persiste** y **no es un artefacto de ventana** | 🔴 **Sin evidencia alguna.** Es la que sostiene la decisión y la única sin probar |

## I.1 Evidencia independiente necesaria

1. **Correlaciones rolling a 36 meses** de India frente a All-World, Robeco, Small Caps y
   Emergentes **desde 2005**, no solo el promedio de una ventana.
2. **Correlaciones condicionales en crisis**: 2008, 2011, 2013 *(taper tantrum — episodio
   específicamente adverso para India)*, marzo de 2020, 2022.
3. **Comparación con el contrafactual correcto:** no «India vs Europe Multifactor», sino
   **India vs *no tener nada* en ese 4%** y **vs las alternativas no probadas**
   *(small caps emergentes, value global no europeo, o simplemente ampliar el Motor)*.
4. **Valoración de partida** *(PER, P/B de India frente a su historia y a otros
   emergentes)* — **ausente en todo el corpus** y es la pregunta obvia sobre un mercado que
   ha subido mucho.
5. **Efecto divisa cuantificado:** rupia sin cubrir, con su contribución al riesgo.

---

# J. AUDITORÍA COMMODITIES — hipótesis formal

> ## **H-COMMODITIES**
> *«Una asignación del 1% a materias primas amplias, financiada desde el módulo Freno,
> **aporta protección frente a escenarios de inflación y shocks de oferta** que los bonos y
> el oro no proporcionan, **sin degradar la función estabilizadora del módulo**.»*

| # | Sub-hipótesis | Estado actual |
|---|---|---|
| **C-1** | Las commodities están descorrelacionadas de la renta variable de la cartera | 🟢 **[DATO]** en la ventana medida |
| **C-2** | No duplican al oro *(ρ 0,20)* | 🟢 **[DATO]**, y bien argumentado |
| **C-3** | **Protegen frente a shocks de inflación** | 🔴 **[HIPÓTESIS].** Única evidencia: **2022**. Un episodio |
| **C-4** | **El Freno es su ubicación funcional correcta** | 🔴 **[HIPÓTESIS] sin contrastar.** El argumento es de diseño, no de dato |
| **C-5** | **Financiar desde el Freno es preferible** | 🔴 **Probado sobre un Freno que no es el oficial** *(D-1)* |
| **C-6** | Un 1% es un peso suficiente para cumplir la función | 🔴 **No probado.** Sin prueba de dosis |

## J.1 Evidencia independiente necesaria

1. 🔴 **Comportamiento en ≥3 episodios inflacionarios**, no uno. **El capítulo 19 ya tiene
   el clasificador que los identifica** — es la sinergia evidente y nadie la ha usado.
2. **Rentabilidad real** *(descontada la inflación)*, no nominal: es la única forma de
   hablar de protección del poder de compra.
3. **Coste de rolar futuros**: en contango prolongado, un índice de commodities pierde
   valor de forma estructural. **No aparece en ningún documento** y es una objeción clásica.
4. **Prueba de dosis 0,5% / 1% / 2% / 3%**, con el mismo rigor que se aplicó a India.
5. **Repetir la financiación sobre el Freno real** *(monetario + PIMCO)*.
6. **Correlación condicional con bonos en episodios de tipos al alza**, no la media.

---

# K. PROTOCOLO DE VALIDACIÓN HISTÓRICA INDEPENDIENTE — **diseñado, NO ejecutado**

> **Criterios escritos ANTES de mirar datos.** Se registran aquí para que no puedan
> ajustarse después. **No se ha ejecutado ninguna medición.**

## K.1 Diseño común

| Elemento | Especificación |
|---|---|
| **Fuente** | **Independiente de Morningstar** — índices, no productos *(MSCI India, Bloomberg Commodity, MSCI World, agregado global)*. Rompe la dependencia de proveedor único |
| **Ventanas** | **Rolling de 36 meses**, paso mensual, desde 2005 · **más** 2000-2004 si hay datos |
| **Submuestras obligatorias** | 2008-09 · 2011 · **2013 taper tantrum** · 2015-16 · **2020 covid** · **2021-23 inflación** |
| **Clasificadores de régimen** | **Los dos ya congelados en el capítulo 19** *(mediana móvil de 40 trimestres y media de 10 años)* — evita crear un tercer criterio |
| **Moneda** | En euros **y** en dólares. La rupia sin cubrir es parte de la tesis |
| **Corrección por multiple testing** | **Obligatoria.** Declarar el número de configuraciones examinadas y aplicar al menos un ajuste *(White's Reality Check o Bonferroni sobre las decisiones finales)* |

## K.2 INDIA — criterios de decisión previos

| | Criterio |
|---|---|
| 🟢 **APOYO** | ρ(India, All-World) rolling **< 0,60 en ≥70% de las ventanas** desde 2005 · **y** ρ(India, Robeco) **< 0,55** en la mayoría · **y** en ≥3 de las 6 submuestras de crisis la correlación **no supera** la del Europe Multifactor en el mismo periodo · **y** la volatilidad total de la cartera **no aumenta** en la mayoría de ventanas |
| 🔴 **CONTRADICCIÓN** | ρ(India, All-World) **> 0,75 en ≥3 submuestras de crisis** *(la diversificación desaparece cuando se necesita)* · **o** ρ media rolling **> 0,60** · **o** el Europe Multifactor resulta **igual o menos correlacionado** que India en la mayoría de ventanas largas |
| ⚪ **INCONCLUSO** | Resultados que dependan del clasificador, de la moneda o de la ventana · **o** menos de 3 submuestras con datos utilizables |

## K.3 COMMODITIES — criterios de decisión previos

| | Criterio |
|---|---|
| 🟢 **APOYO** | Rentabilidad **real** positiva en **≥3 de 4 episodios de inflación alta** identificados por **los dos clasificadores del cap. 19** · **y** rentabilidad real superior a la de los bonos en esos mismos episodios · **y** ρ(commodities, bonos) **< 0** en ≥60% de las ventanas rolling · **y** el resultado se mantiene **tras descontar el coste de rolo** |
| 🔴 **CONTRADICCIÓN** | Rentabilidad real negativa en **la mayoría** de episodios de inflación alta · **o** ρ(commodities, bonos) **> 0 en la mayoría** de ventanas *(no serían dos seguros distintos)* · **o** el coste de rolo anula el diferencial frente a los bonos · **o** en los episodios de inflación alta el **oro** las domina *(entonces la posición es redundante y debe financiarse desde oro o no existir)* |
| ⚪ **INCONCLUSO** | Menos de 3 episodios con datos · **o** signo dependiente de la moneda · **o** diferencia dentro del error de estimación |

## K.4 Pruebas transversales *(ambos)*

1. **Frente al Motor:** ¿la diferenciación aparece en los trimestres en que el Motor cae?
2. **Frente a bonos:** ¿el −0,51 sobrevive fuera de 2021-2023?
3. **Frente al oro:** ¿oro y commodities se comportan distinto **en los mismos episodios**,
   o el 0,20 medio esconde correlación alta cuando importa?
4. **Contrafactual sin el cambio:** medir la cartera oficial **sin** India y **sin**
   commodities en las mismas ventanas.

---

# L. MAPA DE IMPACTO SOBRE EL INVESTMENT BOOK — **sin ejecutar nada**

| Capítulo | Qué se vería afectado | Gravedad |
|---|---|---|
| **Cap. 4 · PMMA** | **La reclasificación de Robeco por correlación choca con la limitación L3** *(«separación funcional ≠ separación estadística»)* y con el Principio de Función Dominante: la función la fija **la tesis**, no el comportamiento. **Si se aprueba el CAMBIO 1 por correlación, hay que reformular el árbol de clasificación** | 🔴 **Alta** |
| **Cap. 5 · Capas transversales** | **La bolsa del 47% deja de cuadrar con Motor 48%** *(D-4)*. Habría que redefinir si el 47% se calcula sobre Motor ordinario indexado o sobre el módulo completo | 🔴 **Alta** |
| **Cap. 10 · Parametrización** | Motor 44→48 y Aceleración 12→8 **son cambios de peso por módulo**: en la escala de cinco niveles del propio capítulo, es **cambio de exposición**, no de vehículo | 🟠 Media |
| **Cap. 11 · Los siete módulos** | Fichas de **Motor** *(nueva pata)*, **Aceleración** *(India sustituye al multifactor)*, **Freno** *(dos instrumentos)* y **Emergentes** *(clase)*. ⚠️ **La ficha de Aceleración acaba de perder su justificación por régimen (P-1/D99)**: añadir India **sin** argumento de régimen es coherente, pero hay que redactarlo así | 🟠 Media |
| **Cap. 13 · Reserva y aportaciones** | Si se aprueba el CAMBIO 3, **el Freno pasa a tener dos instrumentos**: el árbol mensual debe decir a cuál se aporta | 🟡 Menor |
| **Cap. 14 · Vehículos** | **Cuatro filas nuevas o modificadas** · el **VETO 0** aplica a India *(¿contratable el Franklin?)*, a commodities y a la clase de Emergentes · **el archivo de descartes se enriquece con 29 descartes documentados** — es la mejor aportación del laboratorio a este capítulo | 🟢 **Positiva** |
| **Cap. 19 · Cuatro climas** | 🔴 **Colisión doble.** ① El capítulo 19 acaba de declarar **H4 «no evaluable en su forma original»** por faltar la pata de renta fija con duración — **y el laboratorio propone modificar ese mismo módulo** basándose en un Freno distinto. ② El capítulo 19 **prohíbe** convertir un episodio en evidencia; **el argumento de commodities descansa en 2022** | 🔴 **Alta** |
| **Caps. 16-18** *(no escritos)* | El X-Ray de referencia cambiaría; **la matriz de correlaciones del cap. 18 tendría que rehacerse** con la composición nueva | 🟠 Media |
| **Cap. 20 · Estrés** | **Los shocks de D47a habría que revisarlos**: cambian dos posiciones | 🟠 Media |
| **`CARTERA_V1_0_FUENTE_DE_VERDAD`** | Cuatro filas afectadas + **la discrepancia de tres ISIN de Emergentes** | 🔴 **Alta** |
| **PMMA Universal** | 🔒 **Registrado, no abierto.** El laboratorio genera **dos preguntas legítimas para esa auditoría**: ¿debe existir un módulo «Aceleración» si sus dos patas necesitan justificarse por separado? ¿es el Freno un módulo o **dos módulos con nombres distintos** *(estabilidad nominal y protección real)*? | — |

---

# M. LAS 15 PREGUNTAS MÁS PELIGROSAS

**P1 · «¿Su cartera base del laboratorio es su cartera real?»**
🔴 **La pregunta letal.** **No lo es**: el Freno difiere. **Respuesta correcta:** *«No del
todo, y es una limitación que hemos identificado: la base del laboratorio usa un ETF de
bonos agregados donde la cartera oficial tiene un monetario y un fondo de renta fija
flexible. Por eso la conclusión sobre financiar commodities desde el Freno no la damos por
válida hasta repetirla sobre la composición real.»* **Reconocerlo es la única salida.**

**P2 · «Han probado 33 configuraciones. ¿Cómo sé que la ganadora no es ruido?»**
*«No puede descartarse con lo que tenemos. Por eso citamos a White (2000) y hemos diseñado
una validación independiente con criterios escritos antes de mirar. Lo que sí podemos
defender es que la selección no se hizo por rentabilidad —lo demuestra el control de la
prueba 18— sino por redundancia medida. Y una diferencia de Sharpe de 0,01 no la
presentamos como evidencia.»*

**P3 · «R² más bajo, ¿por qué es eso bueno?»**
*«No es bueno por sí mismo, y nuestro glosario lo formulaba mal. Un R² menor solo indica
menor proporción de varianza explicada por el índice. Lo usamos como **indicio** de
diferenciación, junto con la correlación par a par, no como criterio de calidad.»*

**P4 · «Su alfa es 3,64 con un 23% de la cartera fuera de la renta variable. ¿No es un
artefacto?»**
🔴 **La pregunta técnica más peligrosa.** *«En buena parte sí. El índice de referencia del
X-Ray es de renta variable global, y nuestra cartera tiene bonos, oro, bitcoin y materias
primas. Alfa y beta frente a ese índice reflejan sobre todo la composición, no habilidad.
Por eso no usamos el alfa como criterio de decisión.»*

**P5 · «¿Por qué a India le exigieron cuatro dosis y a las materias primas ninguna?»**
*«Es una asimetría de rigor que no tiene justificación metodológica. La prueba de dosis de
commodities está pendiente y es condición para aprobar el cambio.»*

**P6 · «Un 1% de materias primas, ¿qué puede cambiar?»**
*«En rentabilidad, casi nada: un +28% aporta 0,28 puntos. Su valor sería estructural —
cubrir un escenario sin cobertura—, pero con ese peso el efecto es simbólico. Es una
crítica que aceptamos y que hace obligatoria la prueba de dosis.»*

**P7 · «Dicen que las materias primas protegen de la inflación. ¿Con qué evidencia?»**
*«Con un solo episodio: 2022. Nuestro propio capítulo 19 establece que con uno o dos
episodios se ilustra, no se infiere. Por tanto hoy es una hipótesis, no un resultado.»*

**P8 · «Reclasifican Robeco a Motor por su correlación. ¿No contradice eso su propio
método?»**
🔴 *«Sí, hay tensión con el Principio de Función Dominante y con nuestra limitación L3, que
dice que la separación funcional no es estadística. La reclasificación no puede aprobarse
únicamente por correlaciones y volatilidad: debe justificarse por función económica. Y
además debe reconciliarse con el macrobloque del 47%, que con Motor al 48% dejaría de
cuadrar. Hasta que ambas cosas se resuelvan, el cambio está bloqueado.»*

**P9 · «Su Motor pasa a 48%. ¿Qué ocurre con la bolsa del 47% del capítulo 5?»**
*«Deja de cuadrar. Es una consecuencia que el laboratorio no había detectado y que hay que
resolver antes de aprobar la reclasificación: definir si el 47% se mide sobre el Motor
ordinario indexado o sobre el módulo completo.»*

**P10 · «Su matriz mezcla filas del informe oficial con filas de carteras que no existen.»**
*«Las filas 11 a 13 vienen de tiradas de diagnóstico, y está declarado en la propia ficha.
El fundamento es que la correlación entre dos series no depende de los pesos de cartera, y
lo verificamos empíricamente: nueve pares compartidos entre tiradas devolvieron el mismo
valor sin variar una centésima. Lo que no sabemos es sobre qué ventana calcula Morningstar,
y eso sí es una limitación abierta.»*

**P11 · «India ha sido uno de los mercados más caros del mundo emergente. ¿A qué valoración
compran?»**
🔴 **No tenemos respuesta.** *«No lo hemos analizado, y es un hueco real: todo el argumento
de India es de correlación y ninguno de valoración.»* **Hay que traer el dato antes de la
defensa.**

**P12 · «¿Qué pasa con la rupia?»**
*«Está sin cubrir y no hemos cuantificado su contribución al riesgo. Es la segunda pieza
que falta.»*

**P13 · «Han eliminado su única posición europea dedicada. ¿Es deliberado?»**
*«Sí, y lo declaramos: Europa baja del 8,9% al 5,6%, sostenida por el índice global y por
Robeco. Aceptamos perder la exposición dedicada porque el vehículo que la daba duplicaba
el núcleo con correlación 0,91. Lo que no hemos hecho es buscar un sustituto europeo no
redundante.»*

**P14 · «Si las materias primas protegen, ¿por qué su peor trimestre empeora?»**
*«Porque protegen frente a inflación, no frente a pánico de liquidez. Pero reconocemos el
problema de fondo: si la protección no aparece en el peor trimestre ni en el peor año, no
hay en el X-Ray ninguna métrica capaz de mostrarla. Por eso la validación tiene que ir a
episodios de inflación, no al X-Ray.»*

**P15 · «Todo viene de Morningstar. ¿Qué han contrastado?»**
*«Cotejamos cuatro volatilidades con el buscador de MAPFRE y coinciden a la centésima —
pero MAPFRE también usa Morningstar, así que **no es una fuente independiente**. La
validación con datos de índices, ajena a Morningstar, está diseñada y pendiente de
ejecutar.»*

---

# N. VEREDICTO GLOBAL

> # 🟡 **NECESITA CORRECCIONES ANTES DE VALIDAR**

**Por qué no es 🟢:** tres bloqueos sustantivos, no cosméticos.

1. 🔴 **La base experimental no coincide con la cartera oficial en el Freno** — y el
   CAMBIO 3 se decidió exactamente ahí.
2. 🔴 **El CAMBIO 1 no puede aprobarse solo por correlación y volatilidad**, contiene un
   error factual en su justificación **y es incompatible con el macrobloque del 47%**
   mientras no se resuelva la gobernanza.
3. 🔴 **R² y TE capturan diferenciación, no mejora**, y por sí solos no neutralizan el
   *multiple testing* de 33 configuraciones.
4. 🔴 **La premisa de partida del CAMBIO 3 contradice el capítulo 19** *(D-9)*: la cartera
   **no** carecía de cobertura frente a la inflación.

**Por qué no es 🔴:** la metodología **no** es insuficiente. Tiene control deliberado,
descartes conservados, errores publicados, criterios previos, verificación cruzada de la
matriz y límites declarados. **Los tres bloqueos son corregibles sin rehacer el
laboratorio**: uno exige repetir una prueba, otro reescribir una justificación y el tercero
añadir una validación fuera de muestra que **ya está diseñada en §K**.

## N.1 Qué hay que hacer, en orden

| # | Acción | Bloquea a |
|---|---|---|
| **1** | **Repetir la prueba 31** sobre el Freno oficial *(monetario + PIMCO)* — o declarar explícitamente que la BASE v10 no es la cartera oficial y acotar todas las conclusiones | CAMBIO 3 |
| **2** | **Reescribir la justificación del CAMBIO 1** sobre criterio funcional, corrigiendo el dato de volatilidad | CAMBIO 1 |
| **3** | **Resolver la colisión del 47%** *(cap. 5)* | CAMBIO 1 |
| **4** | **Ejecutar la validación de §K** con criterios ya escritos | CAMBIOS 2 y 3 |
| **5** | **Prueba de dosis de commodities** | CAMBIO 3 |
| **6** | **Traer valoración y divisa de India** | CAMBIO 2 |
| **7** | **VETO 0** de los tres vehículos nuevos y fijar el ISIN correcto de Emergentes | CAMBIO 4 |
| **8** | **Unificar el recuento de pruebas** y corregir la rentabilidad 5a *(11,06)* | Todos |

## N.2 Estado por cambio

| Cambio | Veredicto |
|---|---|
| **1 · Robeco → Motor** | ⚠️ **No aprobar como está** — la conclusión puede ser correcta, la evidencia publicada no |
| **2 · Europa → India** | 🟡 **Aprobable condicionado** a validación fuera de muestra, valoración y divisa |
| **3 · Freno → 8+1** | 🔴 **No aprobar** — base incorrecta, un solo episodio, sin dosis |
| **4 · Clase de Emergentes** | 🟢 **Aprobar sujeto al VETO 0** y a fijar el ISIN |

---

## Nota final del auditor

**El laboratorio no tiene un problema de honestidad: tiene un problema de fuerza
probatoria.** Publica sus errores, conserva sus descartes, se cita a sí mismo la objeción
del *data snooping* y declara sus sacrificios sin maquillarlos. Eso es infrecuente y hay
que decirlo.

Lo que le falta es lo contrario de lo que suele faltar: **no le sobra confianza, le falta
evidencia fuera de la ventana en la que se tomaron las decisiones.** Y las dos piezas más
débiles —el Freno de la base y el episodio único de 2022— son **exactamente las que un
tribunal exigente encontraría primero**.

**Encontrarlas ahora vale más que diez elogios.**
