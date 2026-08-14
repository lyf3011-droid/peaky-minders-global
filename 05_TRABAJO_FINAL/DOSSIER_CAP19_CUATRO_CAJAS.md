# 📦 DOSSIER PREPARATORIO — CAPÍTULO 19

## Marco de cuatro cajas: crecimiento × inflación · 14 de agosto de 2026

> **Esto no es el capítulo 19.** Es el trabajo previo que fija definiciones, criterios,
> fuentes y episodios **antes** de mirar ningún resultado — para que la conclusión no pueda
> acomodarse a la hipótesis. **Regla fundamental de este dossier: primero datos y
> episodios; después narrativa. Si los datos contradicen el mapa del capítulo 4, se corrige
> el mapa.**
>
> ⚠️ **Ninguna cifra de este documento está calculada todavía.** Todo lo que aparece como
> episodio o expectativa es **candidato a verificar**, y así está marcado.

---

# 1. Definición sencilla: crecimiento e inflación

**Crecimiento** es cuánto más produce y vende una economía que el año anterior. Si las
empresas venden más, contratan más y sus beneficios suben. La medida habitual es el
**PIB real** *(producto interior bruto descontando la subida de precios)*.

**Inflación** es cuánto suben los precios de lo que compramos. Si un carro de la compra
costaba 100 € y ahora cuesta 103 €, la inflación es del 3%. La medida habitual es el
**IPC** *(índice de precios al consumo)*.

Las dos importan a la vez porque afectan a cosas distintas de una inversión: **el
crecimiento mueve los beneficios de las empresas; la inflación mueve el valor del dinero
y el tipo de interés al que se descuentan esos beneficios.** Una empresa puede ir bien y
la inversión ir mal, si la inflación obliga a subir los tipos.

## 1.1 La decisión metodológica más importante: nivel o sorpresa

**[MODELO — decisión a tomar y justificar en el capítulo]** Hay dos formas de definir
«alto» y «bajo», y **dan resultados distintos**:

| Enfoque | Qué mide | Ventaja | Problema |
|---|---|---|---|
| **A · Nivel absoluto** | ¿El crecimiento supera un umbral fijo? *(p. ej. media histórica)* | Simple, reproducible, verificable por un tercero | Un 2% de inflación es «bajo» hoy y era «bajísimo» en 1975: los umbrales fijos envejecen |
| **B · Sorpresa vs expectativa** | ¿Salió por encima o por debajo de lo que el mercado descontaba? | Es lo que mueve los precios de verdad | **Requiere series de expectativas** *(encuestas, breakevens)* que no existen para 1973 y son difíciles de obtener |

> **Propuesta para auditar:** usar el **enfoque A (nivel vs media móvil larga)** como
> criterio principal —porque es el único **reproducible con fuentes públicas y gratuitas
> para todo el periodo**— y **declarar explícitamente** que el marco teórico original de
> las carteras de todo clima razona en términos de sorpresa. Es una **simplificación
> declarada**, no un descuido. La alternativa —usar sorpresas— haría el análisis
> irreproducible antes de 1990, y este trabajo prefiere un método verificable a uno
> elegante que nadie puede comprobar.

---

# 2. Definición operacional de las cuatro cajas

**[MODELO]** Con dos variables y dos estados cada una salen cuatro combinaciones. No hay
más, y ésa es la fuerza del marco: **es exhaustivo**. Toda situación económica cae en una
de las cuatro.

```
                    INFLACIÓN BAJA          INFLACIÓN ALTA
                 ┌──────────────────────┬──────────────────────┐
 CRECIMIENTO     │   CAJA 1             │   CAJA 2             │
 ALTO            │   Expansión          │   Recalentamiento    │
                 │   desinflacionaria   │   (crecimiento caro) │
                 ├──────────────────────┼──────────────────────┤
 CRECIMIENTO     │   CAJA 3             │   CAJA 4             │
 BAJO            │   Recesión           │   Estanflación       │
                 │   deflacionaria      │                      │
                 └──────────────────────┴──────────────────────┘
```

| Caja | Nombre operativo | Definición | Qué se vive en la calle |
|---|---|---|---|
| **1** | **Expansión desinflacionaria** | Crecimiento > umbral **y** inflación < umbral | Las empresas ganan más y el dinero no pierde valor. El escenario más cómodo para una cartera de acciones |
| **2** | **Recalentamiento** | Crecimiento > umbral **e** inflación > umbral | La economía va rápido pero los precios suben; el banco central suele subir tipos para frenarla |
| **3** | **Recesión desinflacionaria** | Crecimiento < umbral **e** inflación < umbral | Se vende menos y los precios se moderan o caen; el banco central baja tipos |
| **4** | **Estanflación** | Crecimiento < umbral **e** inflación > umbral | Lo peor de ambos: no se crece y encima todo sube. **El escenario que rompe la lógica del 60/40**, porque acciones y bonos pueden caer a la vez |

**Nota metodológica obligatoria del capítulo:** las cajas son **una simplificación
deliberada**. La economía es continua; nosotros la partimos en cuatro cuadrantes con dos
variables. Es un instrumento de análisis de robustez — **no una teoría de cómo funciona
la economía, y no una herramienta de predicción**.

---

# 3. Criterio para asignar un periodo a una caja

**[MODELO — el criterio se escribe ANTES de mirar los resultados. Ésa es toda la
disciplina de este capítulo.]**

## 3.1 Reglas propuestas

| # | Regla | Motivo |
|---|---|---|
| **R1** | **Unidad de análisis: el trimestre** | El PIB es trimestral; usar meses obligaría a interpolar |
| **R2** | **Crecimiento = PIB real interanual** *(EEUU como economía de referencia, por ser el mercado dominante de la cartera — declarado como sesgo)* | Interanual elimina estacionalidad |
| **R3** | **Inflación = IPC interanual** de la misma economía | Homogéneo con R2 |
| **R4** | **Umbral = media móvil de los 10 años anteriores** de cada serie *(no un número fijo)* | Evita que «inflación alta» signifique lo mismo en 1975 y en 2015. **Usa solo información pasada: no mira al futuro** |
| **R5** | **Un episodio necesita ≥2 trimestres consecutivos** en la misma caja | Evita cambios de caja por ruido de un trimestre |
| **R6** | **Los trimestres en el borde** *(a menos de ±0,5 pp del umbral)* **se marcan «frontera»** y se excluyen del cálculo principal, mostrándose aparte | Honestidad: la clasificación binaria tiene zonas grises y hay que enseñarlas |
| **R7** | **Los umbrales y el código se publican en anexo** | Reproducibilidad: un tercero debe poder repetirlo |

## 3.2 Prueba de robustez obligatoria

**El capítulo debe repetir la clasificación con al menos una variante** *(p. ej. umbral =
mediana de 20 años, o inflación subyacente en vez de general)* **y enseñar cuántos
trimestres cambian de caja.** Si la asignación es muy sensible al umbral, eso es un
resultado del capítulo — no algo que ocultar.

---

# 4. Fuentes macro primarias necesarias

| Dato | Fuente primaria propuesta | Cobertura | Estado |
|---|---|---|---|
| PIB real EEUU trimestral | **BEA** *(Bureau of Economic Analysis)*, vía FRED serie de PIB real | 1947→ | 📚 **Por descargar** |
| IPC EEUU mensual | **BLS** *(Bureau of Labor Statistics)*, vía FRED | 1913→ | 📚 Por descargar |
| PIB real e IPC zona euro/España | **Eurostat · INE** | ~1995→ *(limitado)* | 📚 Por descargar — **solo sirve para el periodo reciente** |
| Tipo de interés oficial | **Reserva Federal** *(fed funds)* | 1954→ | 📚 Contexto |
| Retornos históricos por clase de activo | **Damodaran** *(NYU, serie anual acciones/bonos/letras 1928→)* · **Shiller** *(datos S&P y CPI)* | 1928→ | 📚 **La fuente clave del cap. 20** |
| Oro | Precio histórico *(LBMA / World Gold Council)* — ⚠️ **oro fijado hasta 1971** | 1968→ útil | 📚 Con salvedad |

**Regla de fuentes del capítulo:** cada serie se cita con **proveedor, identificador de
serie, fecha de descarga y transformación aplicada**. Sin eso, no entra.

---

# 5. Propuesta de episodios históricos — 🔬 **CANDIDATOS A VERIFICAR, NO RESULTADOS**

⚠️ **Estos periodos son hipótesis de trabajo basadas en el consenso histórico general.
NINGUNO está clasificado todavía por nuestro criterio.** La clasificación definitiva sale
de aplicar R1-R7 a las series descargadas — **y puede desmentir a esta lista**. Se publican
aquí precisamente para poder comprobar después si nuestro criterio los reproduce: si un
episodio universalmente reconocido como estanflación no cae en la caja 4, **el defectuoso
es nuestro criterio, y hay que decirlo.**

| Episodio candidato | Caja esperada | Por qué es interesante | Verificación |
|---|---|---|---|
| **1973-1975** *(crisis del petróleo)* | 4 · Estanflación | El caso de manual: shock de oferta con recesión | 🔬 Pendiente |
| **1979-1982** *(Volcker)* | 4 → 3 | Transición: inflación alta combatida con tipos altos hasta provocar recesión | 🔬 Pendiente |
| **1990-1991** | 3 | Recesión corta | 🔬 Pendiente |
| **1995-1999** | 1 | Expansión con inflación contenida | 🔬 Pendiente |
| **2000-2002** *(puntocom)* | 3 | Caída bursátil severa **sin** inflación | 🔬 Pendiente |
| **2007-2009** *(crisis financiera)* | 3 | El estrés de referencia del proyecto *(D47a)* | 🔬 Pendiente |
| **2010-2019** | 1 | La década que formó las expectativas actuales | 🔬 Pendiente |
| **2020** *(covid)* | 3 → ? | ⚠️ **Caso problemático**: caída y recuperación en meses; el criterio trimestral puede no capturarlo | 🔬 Pendiente |
| **2021-2023** *(inflación post-covid)* | 2 → 4 según el trimestre | **El caso más valioso**: 2022 rompió el 60/40 *(acciones y bonos cayeron juntos)*. Y es el único episodio que la mayoría del equipo ha vivido invirtiendo | 🔬 Pendiente |

**Cobertura buscada: las cuatro cajas con al menos un episodio cada una.** Si alguna caja
se queda sin episodios en el periodo con datos fiables, **se dice** — y el capítulo declara
esa caja como analizable solo teóricamente.

---

# 6. Series necesarias — lista de la compra

| # | Serie | Para qué | Prioridad |
|---|---|---|---|
| 1 | PIB real EEUU trimestral | Eje vertical de las cajas | 🔴 Imprescindible |
| 2 | IPC EEUU mensual→trimestral | Eje horizontal | 🔴 Imprescindible |
| 3 | Retorno anual de acciones EEUU | Comportamiento del Motor por caja | 🔴 |
| 4 | Retorno anual de bonos del Tesoro *(largo y corto)* | Comportamiento del Freno | 🔴 |
| 5 | Precio del oro | Activos Reales | 🟠 *(con la salvedad pre-1971)* |
| 6 | Índice de materias primas / cobre | Activos Reales | 🟠 |
| 7 | Acciones defensivas *(consumo básico, salud)* vs mercado | Módulo Defensivos | 🟠 **Serie larga difícil de conseguir gratis** |
| 8 | Small caps y value *(factores Fama-French)* | Aceleración | 🟠 *(la biblioteca de datos de Fama-French es pública)* |
| 9 | Emergentes | Módulo Emergentes | 🟡 **Solo desde ~1988** |
| 10 | Bitcoin | Asimetría | 🟡 **Solo desde ~2010: no cubre ninguna estanflación. Se declarará como no analizable históricamente** |

---

# 7. Activos y proxies por módulo — y su límite

| Módulo | Proxy histórico propuesto | Cobertura | Problema declarado |
|---|---|---|---|
| 🚀 Motor | Índice amplio de acciones EEUU | 1928→ | El All-World no existe hasta mucho después: el proxy sobre-representa EEUU *(aunque nuestra cartera también lo hace, así que el sesgo va a favor de la comparación)* |
| 🌿 Defensivos | Sectores consumo básico y salud | ⚠️ Series sectoriales largas escasas | 🔴 **El proxy más débil.** Si no hay serie fiable, se declara «no analizable con datos largos» |
| ⚡ Aceleración | Factores tamaño y valor *(Fama-French)* | 1926→ | Los factores académicos **no son productos comprables**: miden la prima, no un fondo con costes |
| 🌍 Emergentes | Índice de emergentes | 1988→ | **No cubre 1973 ni 1979** |
| ⚓ Freno | Letras y bonos del Tesoro | 1928→ | Nuestro vehículo real es otra cosa *(monetario euro + renta fija flexible)*: el proxy mide el **tipo de exposición**, no nuestros fondos |
| 🥇 Activos Reales | Oro y materias primas | 1968→ útil | **El oro tuvo precio fijo hasta 1971**: cualquier análisis anterior es artificial |
| 💥 Asimetría | Bitcoin | 2010→ | 🔴 **No analizable en ninguna caja histórica relevante.** Se dice y no se sustituye por otra cosa |

> **Regla dura del capítulo:** los proxies miden **cómo se comporta ese tipo de exposición
> en cada clima**, no cómo se habría comportado nuestra cartera. La cartera actual no
> existía. Cualquier frase del tipo «nuestra cartera habría rendido X en 1973» está
> **prohibida** salvo etiquetada como simulación con todos sus supuestos.

---

# 8. Problemas de datos — declarados por adelantado

| # | Problema | Gravedad | Cómo se trata |
|---|---|---|---|
| **P1** | **Dos módulos casi sin historia**: Asimetría *(2010→)* y Emergentes *(1988→)* | 🔴 | Se declaran no analizables en las cajas antiguas. **No se inventa un sustituto** |
| **P2** | **Defensivos sin serie sectorial larga y gratuita** | 🔴 | Si no aparece fuente, el módulo se analiza solo desde donde haya datos |
| **P3** | **El oro estuvo fijado hasta 1971** | 🟠 | Todo análisis de oro empieza en 1971-73 |
| **P4** | **Revisiones del PIB**: el dato de hoy sobre 1974 no es el que se conocía entonces | 🟠 | Se usan datos revisados y **se declara**: la clasificación es retrospectiva, no lo que un inversor sabía en tiempo real |
| **P5** | **Sesgo EEUU** en toda la clasificación | 🟠 | Declarado. Justificación: es el mercado dominante de la cartera. Se comprueba con Europa desde 1995 si da tiempo |
| **P6** | **Divisa**: los retornos históricos en dólares no son lo que habría cobrado un inversor en euros | 🟠 | Se declara; la conversión completa es trabajo del cap. 18 |
| **P7** | **Pocos episodios por caja** — la estanflación tiene esencialmente uno y medio | 🔴 | **Límite estadístico fundamental: con 1-2 episodios no hay inferencia, hay ilustración.** El capítulo debe decirlo en sus propias palabras |
| **P8** | **Covid (2020) rompe el criterio trimestral** | 🟡 | Se muestra aparte como caso límite del método |

---

# 9. Qué del mapa PMMA inicial sigue siendo **hipótesis**

**[MODELO]** El capítulo 4 publicó un mapa módulo→régimen etiquetado explícitamente como
**hipótesis de diseño sin validar**. Aquí queda enumerado qué se somete a prueba:

| # | Hipótesis del mapa inicial | Estado | Cómo se pone a prueba |
|---|---|---|---|
| **H1** | El **Motor** rinde bien en la caja 1 y mal en la 3 | 🔬 Hipótesis | Retorno de acciones por caja |
| **H2** | Los **Defensivos** caen menos que el mercado en las cajas 3 y 4 | 🔬 Hipótesis **débil** *(problema P2)* | Sectorial vs mercado, si hay datos |
| **H3** | Los **Activos Reales** protegen en la caja 4 *(estanflación)* | 🔬 **La hipótesis más importante del marco** — es la razón de ser del módulo | Oro y materias primas en 1973-75 y 1979-82 |
| **H4** | El **Freno** ayuda en la caja 3 y **estorba** en la 4 | 🔬 Hipótesis | Bonos por caja — **2022 es el test moderno** |
| **H5** | **Aceleración** amplifica en ambos sentidos | 🔬 Hipótesis | Factores por caja |
| **H6** | **Emergentes** se comporta distinto del Motor según el clima | 🔬 Hipótesis · datos insuficientes | Solo desde 1988 |
| **H7** | **Ninguna caja queda huérfana** en la cartera | 🔬 **Hipótesis de cobertura — la que el tribunal atacará** | Suma de las anteriores |
| **H8** | La **Reserva** aporta capacidad de actuar en cualquier caja | ⚪ No comprobable con datos históricos — es una propiedad operativa, no de retorno | Se declara como tal |

---

# 10. Qué resultados **refutarían** cada hipótesis

**[MODELO]** Se escribe antes de calcular. Si un resultado de esta columna aparece, **se
publica y se corrige el mapa del capítulo 4** — no al revés.

| Hipótesis | 🔴 **Se refuta si…** | Consecuencia si se refuta |
|---|---|---|
| **H1 · Motor** | Las acciones rinden igual o mejor en la caja 3 que en la 1 | El mapa se corrige; el Motor sigue justificado por otras razones *(crecimiento a largo plazo)*, pero el mapa por regímenes deja de sostenerse |
| **H2 · Defensivos** | Los defensivos **no** caen menos que el mercado en las cajas 3 y 4 | 🔴 **Golpe directo a la razón de ser del módulo.** Habría que replantear el 12% o redefinir su función como «menor volatilidad» sin promesa de caídas |
| **H3 · Reales** | El oro **no** protege en los episodios de estanflación identificados | 🔴 **El golpe más grave de todos**: el 9% de Activos Reales existe principalmente por esta hipótesis. Obligaría a revisar el módulo o a reformular su función *(«diversificador» en vez de «cobertura de inflación»)* |
| **H4 · Freno** | Los bonos protegen en la caja 4 tanto como en la 3 | El módulo mejora respecto a lo previsto — **también hay que publicarlo** |
| **H5 · Aceleración** | Los factores no muestran comportamiento diferenciado por caja | Aceleración pierde su argumento de régimen; queda solo el argumento de prima a largo plazo *(ya declarado como discutido)* |
| **H7 · Cobertura** | **Una caja queda sin ningún módulo que la defienda** | 🔴 **El resultado más valioso del capítulo, aunque sea el peor**: identificaría un hueco real de la cartera. Se publicaría como limitación estructural, no se taparía |

> **Compromiso registrado:** si H3 o H7 se refutan, **se publican en el capítulo 19 y se
> propaga la corrección al capítulo 4 y al 11.** Un marco que solo puede confirmar lo que
> ya creíamos no sirve para nada.

---

# ✅ SIGUIENTE PASO TRAS AUDITAR ESTE DOSSIER

1. Auditar y aprobar *(o corregir)* definiciones, criterio R1-R7 y lista de refutación.
2. **Solo entonces**: descargar series → clasificar trimestres → calcular por caja.
3. **Solo entonces**: redactar el capítulo 19 con los resultados que salgan.

**Nada de lo anterior está hecho. Este dossier no contiene un solo resultado.**
