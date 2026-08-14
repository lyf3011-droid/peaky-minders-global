# CAPÍTULO 8 — VALIDACIÓN DESCRIPTIVA: OCHO CARTERAS HISTÓRICAS BAJO EL MISMO LENGUAJE

## Investment Book · Parte I · Borrador v1 para auditoría · 13 de agosto de 2026

> **Convención tipográfica:** **[MODELO]** = afirmación propia de PMMA.
> **[EVIDENCIA EXTERNA]** = afirmación con fuente primaria; su estado de verificación se
> declara caso a caso y se resume en la tabla final.
>
> **Regla central de este capítulo:** aquí **no** se demuestra que PMMA sea universal,
> superior ni capaz de predecir nada. Se demuestra una sola cosa, más modesta y más útil:
> **capacidad descriptiva sobre arquitecturas heterogéneas** — que carteras diseñadas por
> personas distintas, en épocas distintas y con filosofías distintas pueden describirse
> con el mismo lenguaje funcional sin deformarlas… y que, cuando algo se pierde en la
> traducción, se dice.

---

## 8.1 Por qué este ejercicio importa

Un lenguaje inventado para describir una sola cartera no vale mucho: siempre encajará con
aquello para lo que fue diseñado. La prueba honesta es aplicarlo a carteras ajenas —
conocidas, publicadas y anteriores a este trabajo — y ver dos cosas: **qué describe bien**
y **qué se le escapa**.

Por eso cada uno de los ocho casos siguientes usa exactamente la misma estructura:

> **qué intenta hacer → composición original → traducción PMMA → qué enseña al método →
> qué se pierde o simplifica al traducirla**

La última columna es obligatoria. Ocho ejemplos donde el método siempre quedara perfecto
no serían una validación: serían publicidad.

⚠️ **Advertencia previa:** las traducciones son nuestras, no de los autores. Ninguno de
ellos usó nuestros módulos ni pensó en ellos. Describir su cartera con nuestro lenguaje no
significa que lo aprobaran, ni que el lenguaje capture todo lo que quisieron decir.

---

## 8.2 La cartera 60/40

**Qué intenta hacer.** Es el equilibrio clásico entre crecimiento y estabilidad: una parte
mayoritaria en acciones para crecer, una parte en bonos para amortiguar. Durante décadas
ha sido la referencia por defecto de la inversión equilibrada.

**Composición original.** Aproximadamente 60% acciones y 40% bonos. **[EVIDENCIA EXTERNA
— verificada]** Como implementación institucional de referencia se cita el *Vanguard
Balanced Index Fund*, estructurado aproximadamente con esa distribución. ⚠️ Se cita como
**implementación institucional, no como origen histórico** de la proporción — el 60/40 es
anterior y de autoría difusa.

**Traducción PMMA.**

| Módulo | Peso |
|---|---|
| 🚀 Motor | 60% |
| ⚓ Freno | 40% |
| Resto de módulos | 0% |

**Qué enseña al método.** Que dos módulos bastan para describir la cartera equilibrada más
famosa del mundo — y que un 0% en cinco módulos también es información: esas funciones no
fueron incorporadas.

**Qué se pierde o simplifica.** El «40% bonos» del 60/40 real puede contener cosas
radicalmente distintas — deuda pública o privada, plazos cortos o larguísimos — que se
comportan de manera muy diferente. La etiqueta *Freno 40%* agrupa todo eso en una sola
casilla; sin los submódulos *(duración, crédito)*, la traducción pierde la textura que
distingue un 60/40 conservador de uno agresivo por el lado de los bonos.

---

## 8.3 Buffett 90/10

**Qué intenta hacer.** Máxima simplicidad para un heredero no experto: casi todo en el
índice americano de grandes empresas, un resto en deuda pública corta para liquidez.

**Composición original.** 90% en un fondo indexado al S&P 500 de muy bajo coste y 10% en
bonos gubernamentales de corto plazo. **[EVIDENCIA EXTERNA — verificada]** Carta de
Warren Buffett a los accionistas de Berkshire Hathaway, ejercicio 2013, **página 18 del
documento**: instrucciones para el patrimonio destinado a su esposa.

**Traducción PMMA.**

| Módulo | Peso |
|---|---|
| 🚀 Motor | 90% |
| ⚓ Freno | 10% |

**Qué enseña al método.** El extremo minimalista: una cartera válida con dos módulos y una
concentración funcional enorme en el Motor. El método no la corrige — la describe, y la
describe en dos líneas.

**Qué se pierde o simplifica.** El contexto del mandato. Esa instrucción es para un caso
concreto: un fideicomiso, una beneficiaria determinada, un horizonte y unas necesidades
particulares. Traducida a dos casillas, parece una receta general — y Buffett no la
formuló como tal. PMMA empieza siempre por el mandato *(capítulo 3)*; la tabla de
traducción, sola, no lo muestra, y eso es una pérdida real de significado.

---

## 8.4 Bogleheads Three-Fund

**Qué intenta hacer.** La filosofía de John Bogle llevada a la práctica por su comunidad:
tres fondos indexados baratos —mercado doméstico completo, acciones internacionales, bonos—
y nada más.

**Composición original.** Tres componentes **sin pesos obligatorios**: cada inversor los
ajusta a su situación. **[EVIDENCIA EXTERNA — verificada]** Bogleheads Wiki; la propia
fuente subraya que no existe una proporción única correcta.

**Traducción PMMA.**

| Módulo | Contenido |
|---|---|
| 🚀 Motor | Renta variable doméstica + internacional desarrollada |
| 🌍 Emergentes | Solo si el vehículo internacional los separa deliberadamente |
| ⚓ Freno | Bonos |

**Qué enseña al método.** Dos cosas. Primera: el método puede describir **familias** de
carteras, no solo carteras con pesos fijos — la estructura funcional es la misma aunque
los porcentajes varíen. Segunda: la regla de no duplicidad en acción — los emergentes solo
son módulo propio si existe una decisión separada sobre ellos.

**Qué se pierde o simplifica.** La distinción doméstico/internacional, que para la
comunidad Bogleheads es una decisión central *(cuánto sesgo hacia el propio país)*, no
tiene módulo propio en PMMA: ambos caen en Motor y la distinción queda relegada al
análisis de exposiciones. Para un inversor cuya gran pregunta es precisamente esa, la
traducción pierde el eje del debate.

---

## 8.5 Harry Browne — Permanent Portfolio

**Qué intenta hacer.** Una cartera preparada para cualquier clima económico, sin
predicciones: cuatro activos a partes iguales, cada uno pensado para un escenario
—prosperidad, deflación, recesión, inflación.

**Composición original.** 25% acciones · 25% bonos del tesoro de larga duración · 25%
letras del tesoro · 25% oro. **[EVIDENCIA EXTERNA — composición validada; cita primaria
pendiente]** Harry Browne, *Fail-Safe Investing* — ⚠️ **edición y página exacta
pendientes de localizar; no se inventan.**

**Traducción PMMA.**

| Módulo | Peso | Detalle |
|---|---|---|
| 🚀 Motor | 25% | |
| ⚓ Freno | 50% | 25% duración larga + 25% liquidez estratégica |
| 🥇 Activos Reales | 25% | Oro |

**Qué enseña al método.** La distinción más útil del capítulo 5 en acción: **las letras
del tesoro permanentes son Freno, no Reserva** — son una asignación estratégica con
función propia, no caja operativa. Y la necesidad de submódulos: el Freno de Browne
contiene dos papeles opuestos *(duración larga para la deflación, liquidez para la
recesión)* que la cifra agregada del 50% no distingue.

**Qué se pierde o simplifica.** La elegancia del diseño original. Browne construyó una
**simetría uno-a-uno**: cada activo defiende un régimen económico, con pesos iguales
porque ningún régimen se considera más probable. Al traducir a funciones, esa
correspondencia activo-régimen —que es el alma de la cartera— se difumina en tres casillas
de tamaños distintos. La traducción es correcta; el porqué profundo queda fuera del
cuadro y hay que contarlo aparte, como aquí.

---

## 8.6 Golden Butterfly

**Qué intenta hacer.** Una evolución de la Permanent Portfolio con una inclinación
adicional hacia la prosperidad: mantiene la protección de todos los climas pero añade
peso a las acciones pequeñas y baratas.

**Composición original.** Cinco bloques del 20%: grandes compañías · pequeñas compañías de
valor · bonos del tesoro largos · bonos del tesoro cortos · oro. **[EVIDENCIA EXTERNA —
verificada]** Portfolio Charts *(su creador, Tyler)*, artículo original.

**Traducción PMMA.**

| Módulo | Peso | Detalle |
|---|---|---|
| 🚀 Motor | 20% | Grandes compañías |
| ⚡ Aceleración | 20% | Pequeñas compañías de valor |
| ⚓ Freno | 40% | 20% largo + 20% corto |
| 🥇 Activos Reales | 20% | Oro |

**Qué enseña al método.** El ejemplo más limpio de la diferencia entre **Motor y
Aceleración**: las grandes compañías capturan el mercado; las pequeñas de valor se añaden
buscando algo más que el mercado. Misma clase de activo *(acciones)*, dos funciones
distintas — exactamente la distinción que da sentido al módulo Aceleración.

**Qué se pierde o simplifica.** El doble motivo de la pieza clave. En el diseño original,
las pequeñas compañías de valor no están solo «por la prima»: completan el mapa de
regímenes inclinándolo hacia la prosperidad. La etiqueta *Aceleración* captura el motivo
de rentabilidad y deja fuera el motivo de régimen — media verdad bien clasificada.

---

## 8.7 All Seasons

**Qué intenta hacer.** Una cartera para particulares inspirada en la idea de equilibrio
entre escenarios económicos: que ningún clima —crecimiento, recesión, inflación,
deflación— la dañe de forma desproporcionada.

**Composición original.** 30% acciones · 40% bonos del tesoro de larga duración · 15%
bonos intermedios · 7,5% oro · 7,5% materias primas. **[EVIDENCIA EXTERNA — verificada]**
Tony Robbins, a partir de sus conversaciones con Ray Dalio, **para los pesos de la versión
divulgada**. ⚠️ **Distinción obligatoria:** esta versión *retail* no es el *All Weather*
institucional de Bridgewater — aquél se construye por **equilibrio de riesgo**, con
técnicas que una cartera de pesos fijos no replica. Bridgewater se cita únicamente para
explicar esa diferencia, no como fuente de estos pesos.

**Traducción PMMA.**

| Módulo | Peso | Detalle |
|---|---|---|
| 🚀 Motor | 30% | |
| ⚓ Freno | 55% | 40% duración larga + 15% intermedia |
| 🥇 Activos Reales | 15% | 7,5% oro + 7,5% materias primas |

**Qué enseña al método.** Que una filosofía muy distinta de la nuestra cabe en el mismo
lenguaje sin forzarla — y una lección de fondo: **el peso en dinero no es el peso en
riesgo**. El 55% de bonos existe porque los bonos «pesan» menos en riesgo que las
acciones; una lectura solo por capital no lo explica.

**Qué se pierde o simplifica.** Precisamente eso: **la lógica que genera los pesos**.
La idea madre del diseño es equilibrar riesgo entre escenarios, y PMMA clasifica capital
por función — puede describir el resultado, pero no contiene el principio de equilibrio de
riesgo que lo produjo. De las ocho traducciones, ésta es donde el lenguaje funcional deja
fuera la mayor parte del pensamiento original.

---

## 8.8 Swensen — la cartera para particulares

**Qué intenta hacer.** David Swensen, gestor del patrimonio de Yale, propuso para
particulares una cartera diversificada por funciones económicas: crecimiento, protección
frente a crisis y protección frente a inflación, con vehículos indexados.

**Composición original.** 30% renta variable doméstica · 15% desarrollados
internacionales · 5% emergentes · 20% inmobiliario cotizado (REIT) · 15% bonos del
tesoro · 15% bonos ligados a la inflación (TIPS). **[EVIDENCIA EXTERNA — composición
validada; cita primaria pendiente]** David Swensen, *Unconventional Success* —
⚠️ **página exacta pendiente de localizar; no se inventa.**

**Traducción PMMA.**

| Módulo | Peso | Detalle |
|---|---|---|
| 🚀 Motor | 45% | Doméstica + internacional desarrollada |
| 🌍 Emergentes | 5% | Asignación separada y deliberada |
| 🥇 Activos Reales | 20% | REIT como asignación inmobiliaria específica |
| ⚓ Freno | 30% | 15% tesoro nominal + 15% ligado a inflación |

**Qué enseña al método.** Tres reglas de clasificación en un solo caso: los emergentes
como módulo propio *(hay decisión separada)*, el REIT como Activos Reales *(es una
asignación inmobiliaria específica, no parte de un índice global)* y los TIPS como Freno
*(siguen siendo renta fija, aunque protejan de la inflación)*. Es la cartera ajena que más
se parece estructuralmente al lenguaje del método — cinco módulos activos.

**Qué se pierde o simplifica.** Una restricción normativa central del autor: Swensen
defiende que la renta fija del particular sea **exclusivamente gubernamental**, por
desconfianza del crédito privado en los momentos de crisis. El módulo Freno de PMMA admite
más cosas; la traducción conserva los pesos pero pierde esa prohibición — que en el diseño
original no es un detalle, es una convicción.

---

## 8.9 Meb Faber — GTAA

**Qué intenta hacer.** Un modelo con dos ideas: una estructura diversificada en cinco
grandes grupos y, encima, una **regla táctica** que puede sacar cada grupo a liquidez
cuando su tendencia se vuelve negativa.

**Composición original.** Cinco grupos a partes iguales *(20%)*: acciones estadounidenses ·
acciones extranjeras · bonos · inmobiliario cotizado · materias primas. La versión táctica
aplica una media móvil de diez meses: cada grupo permanece invertido o pasa a liquidez
según la señal. **[EVIDENCIA EXTERNA — verificada]** Fuentes del propio Meb Faber /
paper GTAA.

**Traducción PMMA** *(estructura de compra y mantenimiento)*:

| Módulo | Peso | Detalle |
|---|---|---|
| 🚀 Motor | 40% | EEUU + extranjero |
| ⚓ Freno | 20% | Bonos |
| 🥇 Activos Reales | 40% | REIT + materias primas |

Y la regla táctica **no es un módulo**: es una **forma de gestión sistemática aplicada
sobre la estructura** — una capa de decisión activa regulada, descrita con las dimensiones
del capítulo 5.

**Qué enseña al método.** La separación estructura/gestión en su versión más exigente: un
sistema táctico completo puede describirse **sin romper la arquitectura**, como regla
superpuesta a módulos estables. Es la demostración de que las capas del capítulo 5 no son
decorativas.

**Qué se pierde o simplifica.** Dos cosas, y la segunda es seria. Primera: en GTAA **la
esencia es la regla, no la estructura** — describir primero los módulos invierte la
jerarquía del autor, para quien la señal táctica es el corazón del modelo. Segunda: la
liquidez táctica de GTAA no encaja limpiamente en nuestras casillas — no es Reserva *(no
es caja de ejecución)* ni Freno estratégico *(no es permanente)*: es un estado temporal
dictado por una señal. El método la describe como efecto de la regla, pero la casilla
exacta de ese efectivo táctico es una **tensión clasificatoria real** que declaramos en
lugar de esconder.

---

## 8.10 La tabla comparativa

| Cartera | Motor | Defensivos | Aceleración | Emergentes | Freno | Activos Reales | Asimetría |
|---|---|---|---|---|---|---|---|
| 60/40 | 60 | — | — | — | 40 | — | — |
| Buffett 90/10 | 90 | — | — | — | 10 | — | — |
| Bogleheads 3-Fund | variable | — | — | opcional | variable | — | — |
| Permanent Portfolio | 25 | — | — | — | 50 | 25 | — |
| Golden Butterfly | 20 | — | 20 | — | 40 | 20 | — |
| All Seasons | 30 | — | — | — | 55 | 15 | — |
| Swensen | 45 | — | — | 5 | 30 | 20 | — |
| Faber GTAA *(estructura)* | 40 | — | — | — | 20 | 40 | — |

La tabla no pretende decir qué cartera es mejor. Dice otra cosa: **filosofías de inversión
profundamente distintas pueden leerse con las mismas siete columnas** — y las columnas
vacías hablan tanto como las llenas.

---

## 8.11 Qué demuestra el conjunto — y qué no

**[MODELO]** Cinco lecciones salen del ejercicio:

1. **No hacen falta los siete módulos.** Dos carteras funcionan con dos; ninguna de las
   ocho usa Defensivos ni Asimetría — funciones que sí usa nuestra implementación, y esa
   diferencia también describe algo.
2. **El método no prescribe pesos.** El Motor va del 20% al 90% entre casos igualmente
   describibles.
3. **El Freno adopta estructuras muy distintas** — de la liquidez pura de Buffett a los
   dos tramos opuestos de Browne — y por eso necesita submódulos.
4. **Motor y Aceleración son funciones distintas de la misma clase de activo** — Golden
   Butterfly lo muestra mejor que cualquier definición.
5. **La gestión activa puede describirse sin romper la estructura** — GTAA lo demuestra,
   con la tensión declarada de su liquidez táctica.

Y lo que el ejercicio **no** demuestra, dicho sin rodeos:

- **No demuestra universalidad.** Ocho carteras conocidas, todas de largo plazo y de
  espíritu mayoritariamente indexado, elegidas por nosotros. Fuera quedan las estrategias
  que más incomodarían al lenguaje *(gestión alternativa, derivados, apalancamiento)* —
  para ésas existe el protocolo para excepciones, no esta galería.
- **No demuestra superioridad.** Describir bien una cartera no la mejora ni la empeora.
- **No es un aval de los autores.** Las traducciones son nuestras; los autores ni las
  conocieron ni las aprobaron.
- **Y en dos casos la traducción pierde el corazón del diseño** *(el equilibrio de riesgo
  de All Seasons, la jerarquía táctica de GTAA)* — el lenguaje describe el resultado, no
  siempre el porqué.

---

## 8.12 Síntesis

> **Ocho carteras de autores, épocas y filosofías distintas caben en el mismo lenguaje de
> funciones — con sus pesos, sus ceros y sus reglas. Eso es capacidad descriptiva, y es
> todo lo que este capítulo reclama. Donde la traducción simplifica o pierde algo, queda
> dicho caso por caso: un lenguaje que no admite sus límites no describe — etiqueta.**

El capítulo 9 reúne las limitaciones del marco, incluidas las que este ejercicio ha
sacado a la luz; la Parte II aplica el lenguaje completo a *Peaky Minders Global 10Y*.

---

## CIERRE DEL CAPÍTULO — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes | Remisiones |
|---|---|---|---|---|---|
| D75 *(los siete módulos y su carácter no prescriptivo)* · D78-D79 *(formas de gestión — usadas en el caso GTAA)* | **Matriz documental del capítulo:** 6 casos con fuente verificada *(Vanguard Balanced como implementación, carta Berkshire 2013 p. 18, Bogleheads Wiki, Portfolio Charts/Tyler, Robbins para los pesos retail con Bridgewater solo como contraste, Faber/paper GTAA)* · 2 casos con composición validada y cita primaria pendiente *(Browne y Swensen)* | Selección hecha por nosotros *(sesgo de muestra hacia carteras indexadas de largo plazo)* · traducciones propias, sin aval de los autores · dos casos pierden el principio generador *(All Seasons, GTAA)* · la liquidez táctica de GTAA como tensión clasificatoria declarada | ① Tabla comparativa 8×7 *(§8.10)* ② Ficha visual por cartera con las cinco filas de la estructura ③ El contraste All Seasons retail vs All Weather institucional ④ GTAA: estructura + regla como capas | 🟠 **Browne, *Fail-Safe Investing*: edición y página exacta** — pendiente, no se inventa · 🟠 **Swensen, *Unconventional Success*: página exacta** — pendiente, no se inventa | **Cap. 5** *(capas usadas en GTAA)* · **Cap. 9** *(limitaciones que este ejercicio aporta)* · **Anexo E** *(fichas bibliográficas completas cuando se cierren las dos citas)* |

### Prueba anti-redundancia — respecto al capítulo 4

El capítulo 4 **anuncia** la validación descriptiva en una frase *(§4.13)* y remite aquí;
no desarrolla ningún caso. Este capítulo no repite ninguna definición de módulos: los usa.
La única superposición es la tabla comparativa, que existe solo aquí.

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Borrador v1 completo del capítulo 8** — 12 secciones. Los ocho casos con la estructura obligatoria de cinco pasos, **incluida la columna «qué se pierde o simplifica» en los ocho** *(las dos pérdidas mayores: el equilibrio de riesgo de All Seasons y la jerarquía táctica de GTAA; más la tensión clasificatoria de la liquidez táctica)*. Matriz documental aplicada: 6 fuentes verificadas, 2 composiciones validadas con **página pendiente y no inventada** *(Browne, Swensen)*. Sección explícita de qué NO demuestra el ejercicio. Pendiente de auditoría |
