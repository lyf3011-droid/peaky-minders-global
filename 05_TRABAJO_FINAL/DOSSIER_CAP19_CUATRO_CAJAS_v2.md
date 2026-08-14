# 📦 DOSSIER PREPARATORIO — CAPÍTULO 19 · **v2**

## Marco de cuatro cajas: crecimiento × inflación · auditoría aplicada · 14 de agosto de 2026

> **Esto no es el capítulo 19.** Es el trabajo previo que fija definiciones, criterios,
> fuentes y episodios **antes** de mirar ningún resultado. **Regla fundamental: primero
> datos y episodios; después narrativa. Si los datos contradicen el mapa del capítulo 4,
> se corrige el mapa — nunca al revés.**
>
> ⚠️ **Ninguna cifra de este documento está calculada todavía.**

---

# 1. Naturaleza del marco — qué es y qué NO es

**[EVIDENCIA EXTERNA]** El marco original de cuatro cuadrantes que popularizó Bridgewater
*(y del que derivan las carteras de «todo clima»)* **se formula en términos de cambios y
sorpresas de crecimiento e inflación respecto de lo que el mercado ya descontaba** — no en
términos de niveles absolutos. La intuición es que los precios de los activos ya
incorporan las expectativas: lo que mueve un mercado no es que la inflación sea del 4%,
sino que sea del 4% cuando se esperaba el 2%.

**[MODELO]** Nuestro clasificador **no reproduce ese sistema.** Lo que construimos aquí es:

> ### **Una aproximación histórica operativa y reproducible** basada en **niveles**
> ### observados de crecimiento e inflación frente a su propia historia reciente.

| | Marco original *(Bridgewater)* | Nuestro clasificador |
|---|---|---|
| Variable | **Sorpresa** frente a expectativa descontada | **Nivel** frente a su mediana histórica reciente |
| Requiere | Series de expectativas *(encuestas, breakevens)* | Solo PIB e IPC públicos |
| Reproducible por un tercero | Difícil; imposible antes de ~1990 | ✅ Sí, con dos series gratuitas |
| Qué explica | Por qué se mueven los precios | En qué clima económico ocurrió cada periodo |

**Por qué elegimos niveles:** porque el criterio debe poder **repetirlo cualquiera** con
fuentes públicas para todo el periodo, incluidos los años setenta. Un método elegante que
nadie puede comprobar vale menos, para este trabajo, que uno simple y verificable.

**Consecuencia que el capítulo debe declarar:** nuestras cajas describen **el clima
económico observado**, no el **shock** que movió los mercados. Son cosas relacionadas pero
distintas, y confundirlas sería un error de método.

---

# 2. Definiciones — crecimiento e inflación

**Crecimiento** es cuánto más produce y vende una economía que el año anterior. Si las
empresas venden más, contratan más y sus beneficios suben. **Variable: variación
interanual del PIB real.**

**Inflación** es cuánto suben los precios de lo que compramos: si el carro de la compra
costaba 100 € y ahora 103 €, la inflación es del 3%. **Variable: variación interanual del
IPC.**

Las dos importan a la vez porque afectan a cosas distintas: **el crecimiento mueve los
beneficios de las empresas; la inflación mueve el valor del dinero y el tipo de interés al
que se descuentan esos beneficios.** Una empresa puede ir bien y la inversión ir mal, si
la inflación obliga a subir los tipos.

---

# 3. Definición operacional de las cuatro cajas

**[MODELO]** Dos variables con dos estados dan cuatro combinaciones. No hay más — y ésa es
la fuerza del marco: **es exhaustivo**. Toda situación cae en una de las cuatro.

```
                    INFLACIÓN BAJA          INFLACIÓN ALTA
                 ┌──────────────────────┬──────────────────────┐
 CRECIMIENTO     │   CAJA 1             │   CAJA 2             │
 ALTO            │   Expansión          │   Recalentamiento    │
                 │   desinflacionaria   │   (crecimiento caro) │
                 ├──────────────────────┼──────────────────────┤
 CRECIMIENTO     │   CAJA 3             │   CAJA 4             │
 BAJO            │   Recesión           │   Estanflación       │
                 │   desinflacionaria   │                      │
                 └──────────────────────┴──────────────────────┘
```

| Caja | Definición formal | Qué se vive en la calle |
|---|---|---|
| **1 · Expansión desinflacionaria** | Crecimiento > umbral **y** inflación < umbral | Las empresas ganan más y el dinero no pierde valor |
| **2 · Recalentamiento** | Crecimiento > umbral **e** inflación > umbral | Va rápido pero caro; el banco central suele subir tipos |
| **3 · Recesión desinflacionaria** | Crecimiento < umbral **e** inflación < umbral | Se vende menos y los precios se moderan; bajan tipos |
| **4 · Estanflación** | Crecimiento < umbral **e** inflación > umbral | No se crece y encima todo sube. **El escenario que rompe la lógica del 60/40** |

**Nota obligatoria del capítulo:** las cajas son una **simplificación deliberada**. La
economía es continua y nosotros la partimos en cuatro cuadrantes con dos variables. Es un
instrumento de **análisis de robustez ante entornos económicos diferentes** — no una teoría
de cómo funciona la economía, y **en ningún caso una herramienta de predicción**.

---

# 4. Criterio de clasificación R1-R8 — congelado antes de calcular

## 4.1 Las reglas

| # | Regla | Motivo |
|---|---|---|
| **R1** | **Unidad de análisis: el trimestre** | El PIB es trimestral; usar meses obligaría a interpolar |
| **R2** | **Crecimiento = variación interanual del PIB real** | Interanual elimina estacionalidad |
| **R3** | **Inflación = variación interanual del IPC** | Homogéneo con R2 |
| **R4** | **Umbral principal = MEDIANA MÓVIL de los 40 trimestres anteriores** *(10 años), **excluyendo el trimestre que se clasifica*** | La mediana resiste valores extremos mejor que la media; excluir el trimestre clasificado evita que el dato se compare consigo mismo. **Solo usa información pasada** |
| **R5** | **Un episodio requiere ≥2 trimestres consecutivos** en la misma caja | Evita cambios de caja por ruido de un trimestre |
| **R6** | **Sin zona frontera en la clasificación.** Todo trimestre con datos recibe caja por comparación estricta con la mediana. **Ninguna observación se excluye ni se ajusta a mano** | Ver §4.2 |
| **R7** | **Umbrales, código y series se publican en anexo** con proveedor, identificador, fecha de descarga y transformación | Reproducibilidad: un tercero debe poder repetirlo |
| **R8** | 🔒 **Todas las reglas de clasificación quedan CONGELADAS antes de analizar las rentabilidades de los activos.** Cualquier cambio posterior de R1-R7 se registra como decisión fechada, con su motivo, y **obliga a repetir y republicar la clasificación completa** | Impide el ajuste retroactivo del método a resultados que no gustan |

## 4.2 La zona frontera: **eliminada de la clasificación**

La v1 proponía excluir los trimestres «cercanos al umbral». **Se elimina**, porque un
criterio de exclusión sin fórmula fijada de antemano introduce exactamente la
discrecionalidad que este capítulo intenta evitar.

**En su lugar, un indicador puramente informativo con fórmula fija, que NO altera ninguna
clasificación:**

> **Marca de proximidad:** un trimestre se señala como «cercano al umbral» si
> `|valor − mediana móvil| < 0,20 × desviación típica de la misma ventana de 40 trimestres`.

Los trimestres marcados **conservan su caja** y **entran en todos los cálculos**; la marca
solo se publica en una tabla informativa que responde a «¿cuántas asignaciones penden de
un hilo?». No hay decisión manual en ningún punto del proceso.

## 4.3 Robustez obligatoria — se publican las dos clasificaciones

| Publicación | Contenido |
|---|---|
| **1 · Clasificación principal** | Mediana móvil de 40 trimestres *(R4)* |
| **2 · Clasificación alternativa** | **Media móvil de 10 años** *(el criterio de la v1)* |
| **3 · Tabla de desacuerdo** | **Número y porcentaje de trimestres que cambian de caja** entre ambas, con el detalle de cuáles |

**Los desacuerdos se publican, no se esconden.** Si las dos clasificaciones difieren mucho,
ése es un resultado del capítulo: significaría que la frontera entre climas es más difusa
de lo que el marco sugiere.

---

# 5. Limitación por revisiones macro — el sistema es descriptivo, no invertible

> **[MODELO — texto que va literal al capítulo]** La clasificación utiliza series
> históricas **actualmente revisadas**. Los umbrales no utilizan observaciones futuras
> *(R4 solo mira hacia atrás)*, pero las cifras históricas pueden incorporar **revisiones
> que un inversor no conocía en tiempo real**. Por eso el sistema es **descriptivo ex post
> y no una señal invertible de market timing**.

Dicho en corto para la defensa: **sabemos hoy en qué caja estuvo 1974; nadie podía saberlo
en 1974 con estos números.** Este capítulo analiza robustez, no genera señales.

---

# 6. Fuentes macro primarias

| Dato | Fuente primaria | Cobertura | Estado |
|---|---|---|---|
| PIB real EEUU trimestral | **BEA** *(Bureau of Economic Analysis)*, vía FRED | 1947→ | 📚 Por descargar |
| IPC EEUU mensual | **BLS** *(Bureau of Labor Statistics)*, vía FRED | 1913→ | 📚 Por descargar |
| Tipo oficial | **Reserva Federal** | 1954→ | 📚 Contexto |
| Retornos por clase de activo | **Damodaran** *(NYU, anual 1928→)* · **Shiller** *(S&P y CPI)* | 1928→ | 📚 **Clave también para el cap. 20** |
| Factores tamaño y valor | **Biblioteca de datos Fama-French** *(pública)* | 1926→ | 📚 Por descargar |
| Oro | **LBMA / World Gold Council** | 1968→ útil | 📚 ⚠️ precio fijado hasta 1971 |
| PIB e IPC zona euro / España | **Eurostat · INE** | ~1995→ | 📚 Solo periodo reciente |

**Regla de fuentes:** cada serie se cita con proveedor, identificador, fecha de descarga y
transformación aplicada. Sin eso, no entra en el capítulo.

---

# 7. Episodios históricos — 🔬 candidatos, y su papel exacto

⚠️ **Ninguno está clasificado todavía.** La clasificación sale de aplicar R1-R8 a las
series descargadas.

| Episodio candidato | Caja esperada *(descripción histórica habitual)* | Por qué interesa |
|---|---|---|
| **1973-1975** *(crisis del petróleo)* | 4 · Estanflación | Ver §7.1 — prueba externa de sentido económico |
| **1979-1982** *(Volcker)* | 4 → 3 | Inflación alta combatida con tipos hasta provocar recesión |
| **1990-1991** | 3 | Recesión corta |
| **1995-1999** | 1 | Expansión con inflación contenida |
| **2000-2002** *(puntocom)* | 3 | Caída bursátil severa **sin** inflación |
| **2007-2009** | 3 | El estrés de referencia del proyecto *(D47a)* |
| **2010-2019** | 1 | La década que formó las expectativas actuales |
| **2020** *(covid)* | ? | ⚠️ Caso límite: caída y recuperación en meses; el criterio trimestral puede no capturarlo |
| **2021-2023** | 2 → 4 según trimestre | **El más valioso**: 2022 rompió el 60/40 y es el único que el equipo ha vivido invirtiendo |

## 7.1 El papel de 1973-75 — **prueba externa, no condición de validez**

> **[MODELO — texto literal al capítulo]** El episodio 1973-75 funciona como **prueba
> externa de sentido económico**. Si la clasificación difiere de la descripción histórica
> habitual, **la discrepancia se investiga y se publica; no se modifica automáticamente el
> algoritmo para forzar el resultado.**

Una discrepancia puede deberse a varias causas legítimas — el retardo entre el shock y la
caída medida del PIB, el efecto de la ventana móvil en una década de inflación creciente,
o el propio criterio de niveles frente al de sorpresas *(§1)*. **Investigarlas es parte del
resultado del capítulo; reescribir el criterio hasta que dé lo esperado, no.**

---

# 8. Series, activos y proxies por módulo

| Módulo | Proxy histórico | Cobertura | Límite declarado |
|---|---|---|---|
| 🚀 Motor | Índice amplio de acciones EEUU | 1928→ | El All-World no existía; el proxy sobre-representa EEUU *(igual que nuestra cartera)* |
| 🌿 Defensivos | Sectores consumo básico y salud | ⚠️ Series largas escasas | 🔴 **El proxy más débil.** Si no hay serie fiable y gratuita, se declara «no analizable con datos largos» |
| ⚡ Aceleración | Factores tamaño y valor *(Fama-French)* | 1926→ | Los factores académicos **no son productos comprables**: miden la prima, sin costes ni implementación |
| 🌍 Emergentes | Índice de emergentes | 1988→ | **No cubre 1973 ni 1979** |
| ⚓ Freno | Letras y bonos del Tesoro | 1928→ | Nuestro vehículo real es otro; el proxy mide **el tipo de exposición**, no nuestros fondos |
| 🥇 Activos Reales | Oro y materias primas | 1968→ útil | **Oro con precio fijo hasta 1971**: nada anterior es interpretable |
| 💥 Asimetría | Bitcoin | 2010→ | 🔴 **No analizable en ninguna caja histórica relevante.** Se dice — no se sustituye por otra cosa |

> **Regla dura:** los proxies miden **cómo se comporta ese tipo de exposición en cada
> clima**, no cómo se habría comportado nuestra cartera — que no existía, igual que la
> mitad de sus productos. Cualquier frase del tipo «nuestra cartera habría rendido X en
> 1973» queda **prohibida** salvo etiquetada como simulación con todos sus supuestos.

---

# 9. «Proteger» — definición operativa obligatoria

**[MODELO]** La palabra «proteger» **no se usa sin definir**. Para cada módulo o activo, en
cada caja, se calculan y publican **cuatro cosas**:

| # | Medida | Qué responde |
|---|---|---|
| **M1** | **Rentabilidad nominal** anualizada en esa caja | ¿Ganó o perdió dinero? |
| **M2** | **Rentabilidad real** *(descontada la inflación del propio periodo)* | ¿Conservó poder de compra? **Es la medida decisiva en las cajas 2 y 4** |
| **M3** | **Comportamiento relativo al Motor** *(diferencia de rentabilidad real frente al proxy del Motor en la misma caja)* | ¿Aportó algo que el Motor no daba ya? |
| **M4** | **Consistencia entre episodios** de la misma caja | ¿Fue una vez o siempre? |

## 9.1 Definición cuantitativa de «relativamente favorable» y de «consistente»

> **Relativamente favorable en una caja** = **M3 > 0** *(rentabilidad real superior a la
> del Motor en esa caja)*. Se publica siempre junto a M1 y M2, porque un activo puede ser
> relativamente favorable **perdiendo dinero**, y eso hay que decirlo con esas palabras.

> **Consistencia (M4), regla fija:**
> · **≥3 episodios con datos** → consistente si es relativamente favorable en **la mayoría**
> *(≥2 de 3, ≥3 de 4…)*.
> · **2 episodios** → se publican ambos y el veredicto es **«evidencia insuficiente»**.
> · **1 episodio** → se publica como **«ilustración, no evidencia»**. **Un solo episodio no
> confirma ni invalida ningún módulo.**

Esta regla se congela aquí, con R8, **antes de ver ningún resultado**.

---

# 10. Hipótesis del mapa PMMA — reformuladas

**[MODELO]** El capítulo 4 publicó un mapa módulo→régimen etiquetado como **hipótesis de
diseño sin validar**. Aquí queda enumerado qué se somete a prueba y **cómo puede fallar**,
ya con la regla de consistencia del §9.1 incorporada.

| # | Hipótesis reformulada | 🔴 Se pone en cuestión si… |
|---|---|---|
| **H1 · Motor** | Las acciones muestran rentabilidad real mayor en la caja 1 que en la 3, de forma consistente | El orden se invierte de forma consistente → se corrige el mapa; el Motor sigue justificado por crecimiento a largo plazo, pero pierde su lectura por regímenes |
| **H2 · Defensivos** | En las cajas 3 y 4, los defensivos son **relativamente favorables** *(M3 > 0)* de forma consistente | No lo son de forma consistente → **golpe a la razón de ser del módulo**: habría que replantear el 12% o redefinir su función como «menor volatilidad» sin promesa de caídas menores |
| **H3 · Activos Reales** *(reformulada)* | **En los episodios de caja 4 con datos utilizables, el oro y las materias primas son relativamente favorables frente al Motor (M3 > 0) de forma consistente según §9.1.** Con menos de 3 episodios, el resultado es ilustración y **no puede confirmar ni refutar la hipótesis por sí solo** | La mayoría de los episodios disponibles muestra M3 ≤ 0 → **se publica y se revisa la función del módulo** *(de «cobertura de inflación» a «diversificador»)*. ⚠️ **Un único episodio desfavorable NO invalida el módulo** |
| **H4 · Freno** | Los bonos son relativamente favorables en la caja 3 y **desfavorables** en la 4 | Si también ayudan en la caja 4, el módulo **mejora** respecto a lo previsto — y también se publica |
| **H5 · Aceleración** | Los factores muestran comportamiento diferenciado por caja | Sin diferencia apreciable → Aceleración pierde el argumento de régimen; le queda el de prima a largo plazo, ya declarado como discutido |
| **H6 · Emergentes** | Se comporta distinto del Motor según la caja | Datos desde 1988: **como mucho, evidencia insuficiente** |
| **H7 · Cobertura** *(reformulada)* | **Cada caja tiene al menos un módulo relativamente favorable de forma consistente.** Si en alguna caja **ningún** módulo lo es de forma consistente, se declara **«posible hueco de robustez»** — no «la cartera falla» | Un hueco declarado es **el resultado más valioso del capítulo aunque sea el peor**: se publica como limitación estructural, con su nivel de evidencia |
| **H8 · Reserva** | ⚪ No comprobable con datos históricos: es una propiedad operativa, no de retorno | Se declara como tal |

> **Compromiso registrado:** si H3 o H7 quedan en cuestión **según la regla de consistencia
> del §9.1** *(no por un episodio suelto)*, se publica en el capítulo 19 y **se propaga la
> corrección al capítulo 4 y al 11**. El capítulo 4 **no se toca antes** de tener
> resultados, ni para adelantarse a ellos.

---

# 11. Problemas de datos — declarados por adelantado

| # | Problema | Gravedad | Tratamiento |
|---|---|---|---|
| **P1** | **Módulos casi sin historia**: Asimetría *(2010→)*, Emergentes *(1988→)* | 🔴 | No analizables en cajas antiguas. **No se inventa sustituto** |
| **P2** | **Defensivos sin serie sectorial larga y gratuita** | 🔴 | Si no aparece fuente, se analiza solo desde donde haya datos |
| **P3** | **Oro con precio fijo hasta 1971** | 🟠 | Todo análisis de oro empieza en 1971-73 |
| **P4** | **Revisiones del PIB** | 🟠 | Ver §5: descriptivo ex post, no invertible |
| **P5** | **Sesgo EEUU** | 🟠 | Ver §12 |
| **P6** | **Divisa**: retornos históricos en dólares ≠ lo que cobraría un inversor en euros | 🟠 | Declarado; la conversión es trabajo del cap. 18 |
| **P7** | **Pocos episodios por caja** — la caja 4 tiene esencialmente uno y medio | 🔴 | **Con 1-2 episodios no hay inferencia, hay ilustración.** Regla §9.1 |
| **P8** | **Covid (2020) tensiona el criterio trimestral** | 🟡 | Se muestra aparte como caso límite del método |

---

# 12. Limitación geográfica — declarada

> **[MODELO — texto literal al capítulo]** La clasificación histórica utiliza
> principalmente **macro de Estados Unidos**. Por tanto, **clasifica el entorno
> macroeconómico estadounidense, no un régimen global perfectamente sincronizado.** Otras
> economías pueden haber estado en una caja distinta en el mismo trimestre.

**Por qué se acepta:** EEUU es el mercado dominante de la cartera *(≈2/3 de la renta
variable)* y el único con series homogéneas desde 1947. **Qué se hará si hay tiempo:**
repetir la clasificación con datos de la zona euro desde ~1995 y publicar **cuánto
coinciden** — un desacuerdo alto sería, otra vez, un resultado y no un defecto que tapar.

---

# ✅ SIGUIENTE PASO

1. Auditoría de R1-R8 → ver [`AUDITORIA_CRITERIO_R1_R8.md`](AUDITORIA_CRITERIO_R1_R8.md).
2. Preparación de series y cálculo → ver [`PREPARACION_SERIES_CAP19.md`](PREPARACION_SERIES_CAP19.md).
3. **El capítulo 19 no se redacta hasta tener resultados.** El capítulo 4 **no se modifica
   para hacerlo coincidir con ellos.**

**Este dossier no contiene un solo resultado.**
