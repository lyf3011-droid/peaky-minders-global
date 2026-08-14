# 📦 PACK ÚNICO DE AUDITORÍA — CAPÍTULOS 9 A 14

## Peaky Minders Global 10Y · Investment Book · 13 de agosto de 2026

> **Naturaleza de este archivo:** paquete de solo lectura para auditoría externa.
> Contiene **íntegros y sin modificar** los capítulos 9-14, las dos auditorías internas
> y los pendientes en tres categorías separadas. **No sustituye a los archivos fuente**,
> que siguen siendo la referencia en `05_TRABAJO_FINAL/`.
>
> Estado: caps. 4-8 CERRADOS *(el 8 provisional)* · caps. 9-14 en borrador v1, objeto de
> esta auditoría · ningún peso, vehículo, X-Ray ni decisión Dxx modificados.



<!-- ══════════════════════════════════════════════════════════ -->

# ▓▓▓ BLOQUE 1 · CAPÍTULO 9 ▓▓▓

---

# CAPÍTULO 9 — LIMITACIONES DE PEAKY MINDERS MODULAR ARCHITECTURE

## Investment Book · Parte I · Borrador v1 · 13 de agosto de 2026

> **Convención tipográfica:** **[MODELO]** = afirmación propia de PMMA.
> **[EVIDENCIA EXTERNA]** = afirmación que requiere fuente.
>
> **Pregunta que responde este capítulo:** *¿dónde funciona PMMA, dónde empieza a perder
> información y en qué casos podría no aportar suficiente valor?*
>
> Este no es el capítulo decorativo de «debilidades». Es **el capítulo más crítico del
> marco**, y cierra la Parte I a propósito: quien llegue hasta aquí debe salir sabiendo
> los bordes del método mejor que sus virtudes.

---

## 9.1 Por qué este capítulo existe

Un método que solo cuenta lo que hace bien no es un método: es un folleto. Los capítulos
4 a 8 han ido dejando limitaciones declaradas por el camino; este capítulo las reúne,
las ordena y añade las que faltaban. La ordenación es la aportación:

| Tipo | Qué significa | Qué se hace con ellas |
|---|---|---|
| **Limitaciones reducibles** | Pueden mitigarse con datos, procedimientos o controles | Se mitigan, y se dice cómo |
| **Limitaciones inherentes** | Forman parte de la naturaleza del método | Se aceptan, y se dice por qué |

Confundir unas con otras produce dos errores simétricos: prometer que se arreglará lo que
no tiene arreglo, o resignarse ante lo que sí lo tiene.

---

## 9.2 Limitaciones reducibles

**R1 — Dependencia de la calidad de los datos.** Todo el análisis mirando dentro
*(capítulo 6)* vale lo que valgan los datos publicados: carteras internas con retraso,
desgloses parciales, clasificaciones que cambian según el proveedor. **[EVIDENCIA
EXTERNA — plazos y diferencias concretas pendientes de documentar.]**
*Mitigación:* el campo «fuente y fecha» en cada dato, la regla de denominador comparable
y fechas compatibles antes de sumar, y declarar la antigüedad de cada foto.

**R2 — Proxies.** Cuando la herramienta de análisis no reconoce el vehículo exacto, se
analiza un sustituto del mismo índice. Útil, pero nunca idéntico.
*Mitigación:* la regla de atribución *(«del proxy solo se toma aquello para lo que es
realmente equivalente»)*, el campo de proxy en la ficha y la tabla de conciliación
vehículo real ↔ vehículo analizado.

**R3 — Falsa precisión.** Un porcentaje con dos decimales calculado sobre datos atrasados
sigue siendo una estimación; los decimales no lo convierten en verdad.
*Mitigación:* declarar método y fecha junto a cada cifra, y usar rangos u órdenes de
magnitud cuando la precisión aparente supere a la real.

**R4 — Carga de mantenimiento.** Treinta y cinco campos por posición, tres vistas del
capital, un registro de decisiones: todo eso hay que mantenerlo, y una ficha
desactualizada da apariencia de control sin su sustancia.
*Mitigación:* calendario de revisión *(Parte V)*, y la regla de que ninguna cifra se
publica sin su fecha — lo viejo se ve viejo.

**R5 — Fichas que caducan.** Los fondos cambian por dentro; las tesis envejecen; los
costes se revisan. La ficha perfecta de hoy describe mal la posición de dentro de dos
años.
*Mitigación:* el campo «regla de revisión» de cada posición, que fija cuándo se
reconsidera — la caducidad se programa en lugar de descubrirse.

**R6 — Concordancia entre analistas no testada.** No se ha probado que dos analistas
independientes clasifiquen igual con el árbol. Es reducible porque el test existe y puede
hacerse *(clasificaciones a ciegas y comparación)*; hasta entonces, la mitigación es el
campo de confianza de clasificación y la segunda revisión en casos ambiguos.

**R7 — Activos que exigen el protocolo para excepciones.** Gestión alternativa, capital
privado, estructurados: instrumentos sin función dominante honesta. El protocolo los
acoge como «Extensión», pero cada excepción es capacidad descriptiva que el marco admite
no tener.
*Mitigación:* parcial — el protocolo convierte el hueco en categoría declarada, pero no
lo elimina: si una cartera estuviera dominada por estos activos, PMMA describiría poco.

---

## 9.3 Limitaciones inherentes

**I1 — La subjetividad de la función dominante.** La función la decide quien clasifica,
mirando la tesis. El árbol ordena el juicio; no lo sustituye. Esto no es un defecto a
reparar: **es el precio de clasificar por intención en lugar de por etiqueta** — la
intención no es observable desde fuera. Se acota *(árbol, tesis escrita, confianza,
segunda revisión)*; no se elimina.

**I2 — El riesgo de racionalización a posteriori.** PMMA se desarrolló en paralelo a la
cartera que lo implementa. El registro de decisiones fechado y la validación sobre
carteras ajenas *(capítulo 8)* mitigan la sospecha; **ninguna defensa la elimina del
todo**, porque el orden real de las ideas en la cabeza de un equipo no es auditable.
Se declara y se convive con ella.

**I3 — El riesgo de ser solo etiquetas nuevas.** Con otros siete nombres, el método
funcionaría igual. Si el valor estuviera en la taxonomía, no habría valor. La defensa
—que el valor está en las separaciones y en el rastro documental— es razonable, pero es
**nuestra defensa de nuestro método**: el lector debe juzgarla, no aceptarla.

**I4 — Función distinta no implica comportamiento estadístico distinto.** Dos posiciones
con funciones diferentes pueden moverse casi igual — la propia implementación lo muestra
*(las cifras, en el capítulo 18)*. El método obliga a medirlo y a declararlo; **no puede
impedirlo**, porque la función es una intención y la correlación es un hecho del mercado.

**I5 — Traducir pierde información.** El capítulo 8 lo documentó caso por caso: la
simetría de regímenes de Browne, el equilibrio de riesgo de All Seasons, la jerarquía
táctica de Faber. Un lenguaje común **compacta**; compactar **pierde**. La pérdida se
declara, no se evita.

**I6 — PMMA no predice.** Nada en el método estima rentabilidades futuras, detecta techos
ni anticipa crisis. No es una carencia por inmadurez: **el método no contiene ningún
mecanismo predictivo, por diseño.**

**I7 — PMMA no selecciona pesos automáticamente.** Del mandato no se deduce
mecánicamente «44% Motor». Los pesos son juicio parametrizado del equipo — el método
exige justificarlos y registrarlos; no los calcula.

**I8 — PMMA no garantiza rentabilidad.** Una cartera impecablemente clasificada,
registrada y verificada puede perder dinero durante años. El control final examina el
proceso; el mercado no lee nuestros documentos.

**I9 — PMMA no sustituye el análisis de riesgo.** Clasificar por funciones no mide
volatilidades, correlaciones, caídas ni concentraciones. El método **exige** ese análisis
*(Parte III y IV)* y le da estructura; no lo reemplaza.

**I10 — La escalabilidad amplia está declarada, no demostrada.** Que el marco sirva para
una estructura patrimonial compleja multi-cuenta es una extensión razonada; lo demostrado
es su aplicación a un mandato concreto y su capacidad descriptiva sobre ocho carteras
conocidas. La diferencia entre «declarado» y «demostrado» se mantiene siempre visible.

---

## 9.4 Dónde funciona, dónde pierde, dónde puede no compensar

**[MODELO]** El resumen honesto del alcance:

| Zona | Situación | Ejemplos |
|---|---|---|
| ✅ **Funciona bien** | Carteras de largo plazo con instrumentos convencionales *(fondos, ETF, acciones, bonos)* donde la pregunta central es *para qué está cada cosa* | Las ocho del capítulo 8 · la implementación de este trabajo |
| 🟡 **Empieza a perder información** | Diseños cuya lógica generadora no es funcional: equilibrio de riesgo, sistemas tácticos, simetrías de régimen | All Seasons *(pierde el principio)* · GTAA *(pierde la jerarquía)* |
| 🔴 **Puede no aportar suficiente valor** | Carteras dominadas por instrumentos sin función dominante honesta, o inversores que no van a mantener el registro | Carteras centradas en gestión alternativa · uso ocasional sin decision log |

La tercera fila merece subrayarse: **PMMA es un método de documentación continua. Quien no
vaya a mantener las fichas y el registro obtiene el coste del sistema sin su beneficio —
y estaría mejor con algo más simple.**

---

## 9.5 Qué tendría que ocurrir para retirar PMMA

El capítulo 4 fijó el criterio de falsación organizativo. Aquí se convierte en una lista
operativa: **consideraríamos que PMMA no añade suficiente valor frente a un sistema
convencional más sencillo si se diera cualquiera de estas situaciones de forma
sostenida:**

1. **Las clasificaciones resultan irreproducibles** — el test entre analistas *(R6)*,
   cuando se haga, muestra desacuerdos frecuentes incluso con tesis escritas delante.
2. **El registro deja de usarse** — las decisiones reales se toman fuera del sistema y
   se documentan después, con lo que el rastro ya no refleja el proceso *(I2 realizada)*.
3. **Las vistas y fichas no detectan nada** — tras un periodo razonable, ninguna
   duplicidad, ningún solapamiento, ninguna incoherencia intención/realidad ha sido
   descubierta por el método que no fuera evidente sin él.
4. **El mantenimiento devora el beneficio** — el tiempo de administrar fichas y vistas
   supera de forma estable al valor de las decisiones que mejora.
5. **La cartera deriva hacia instrumentos de Extensión** — si la mayoría del capital
   acabara en activos sin función dominante clara, el lenguaje describiría una minoría
   del patrimonio.

Ninguna de las cinco se da hoy. Pero el compromiso queda escrito: **si se dan, la
conclusión correcta no será defender el método — será simplificarlo o retirarlo.**

---

## 9.6 Síntesis — y cierre de la Parte I

> **PMMA ordena, registra y comprueba. No predice, no elige pesos, no garantiza
> resultados y no sustituye al análisis de riesgo. Parte de sus límites se reducen con
> procedimiento; otra parte es inherente y se acepta con los ojos abiertos. Y si algún
> día el método cuesta más de lo que aporta, lo dicho en este capítulo obliga a
> simplificarlo o retirarlo — no a defenderlo.**

Con esto queda cerrada la Parte I: el problema *(cap. 2)*, el mandato *(cap. 3)*, el
método *(cap. 4)*, sus capas *(cap. 5)*, sus dos modos de análisis *(cap. 6)*, sus
herramientas *(cap. 7)*, su validación descriptiva *(cap. 8)* y sus límites *(cap. 9)*.
La Parte II aplica todo lo anterior a la construcción de *Peaky Minders Global 10Y*.

---

## CIERRE DEL CAPÍTULO — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes | Remisiones |
|---|---|---|---|---|---|
| D75 · D77 *(proxy)* · D78-D82 *(los cierres que fueron dejando limitaciones declaradas)* | Las limitaciones R1-R7 e I1-I10 proceden de los cierres de los caps. 4-8 y de la auditoría de integración *(C.2)*; ninguna es nueva sin origen | Este capítulo ES la lista — y declara la suya propia: la clasificación reducible/inherente también es un juicio | ① Tabla reducibles vs inherentes ② El mapa de tres zonas *(§9.4)* ③ Las cinco condiciones de retirada *(§9.5)* | 🟠 R1: plazos de publicación y diferencias entre proveedores *(heredado del cap. 6)* · 🟡 el test inter-analista como extensión futura | **Cap. 18** *(cifras de I4)* · **Cap. 22** *(fiscalidad del caso proxy)* · **Cap. 26** *(el control final y las respuestas incompletas honestas)* · **Parte V** *(calendario de mantenimiento)* |

### Prueba anti-redundancia

Las limitaciones L1-L4 del capítulo 4 **no se repiten como definiciones**: se reparten en
I1, I2, I4 y I6-I9 con desarrollo nuevo *(mitigaciones, ejemplos, condiciones de
retirada)*. Lo nuevo de este capítulo: la partición reducible/inherente, el mapa de tres
zonas y las cinco condiciones operativas de retirada.

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Borrador v1 del capítulo 9** — las 17 limitaciones exigidas cubiertas y ordenadas en 7 reducibles *(con mitigación cada una)* + 10 inherentes *(con su porqué)*, mapa de tres zonas de alcance y **las cinco condiciones bajo las que PMMA debería simplificarse o retirarse**. Cierra la Parte I |



<!-- ══════════════════════════════════════════════════════════ -->

# ▓▓▓ BLOQUE 2 · CAPÍTULO 10 ▓▓▓

---

# CAPÍTULO 10 — DEL MANDATO A LA PARAMETRIZACIÓN: LOS PESOS DE GLOBAL 10Y

## Investment Book · Parte II · Borrador v1 · 13 de agosto de 2026

> **Convención:** **[MODELO]** = decisión propia del proyecto · **[EVIDENCIA EXTERNA]** =
> requiere fuente. Datos de producto: ✅ fuente primaria · 🟡 secundaria, pendiente de
> primaria · 🔴 no usar todavía.
>
> **La Parte I respondió: ¿cuál es el método? La Parte II responde: ¿cómo lo aplicamos
> para construir *Peaky Minders Global 10Y*?** Este capítulo muestra el primer tramo de la
> cadena: mandato → necesidades → funciones → pesos.

---

## 10.1 La cadena, visible

**[MODELO]** Todo lo que sigue en la Parte II recorre esta cadena, y cada eslabón tiene su
capítulo:

```
MANDATO (cap. 10)  →  NECESIDADES (cap. 10)  →  FUNCIONES (cap. 10-11)
→  PESOS (cap. 10)  →  EXPOSICIONES (cap. 11)  →  VEHÍCULOS (cap. 14)
→  REGLAS (caps. 12-13)
```

El orden importa porque es la prueba de que el método no se inventó después para
justificar la cartera: el registro de decisiones fechado *(anexo B)* documenta que las
funciones se discutieron antes que los productos, y que más de un producto cambió sin que
cambiara ninguna función.

---

## 10.2 El mandato

| Parámetro | Valor |
|---|---|
| 💰 Capital inicial | **100.000 €** |
| 📅 Aportación | **1.000 € al mes** |
| ⏳ Horizonte | **10 años** |
| 🎯 Perfil | **Agresivo** |

Tres consecuencias del mandato que condicionan todo lo demás:

1. **Las aportaciones son grandes en términos relativos.** En diez años entran 120.000 €
   nuevos sobre 100.000 iniciales — más que la cartera de partida. Eso convierte el flujo
   mensual en una herramienta de primera magnitud: puede corregir desviaciones sin vender
   *(capítulo 13)*.
2. **El horizonte tolera volatilidad, no la ignora.** Diez años permiten asumir una
   mayoría amplia de renta variable; no eliminan la posibilidad de una década mediocre,
   que se examina en la Parte IV.
3. **«Agresivo» describe la tolerancia, no un objetivo de emociones fuertes.** El perfil
   habilita la asignación; las reglas *(caps. 12-13)* existen precisamente para que la
   agresividad del diseño no se convierta en impulsividad de la gestión.

---

## 10.3 De las necesidades a las funciones

**[MODELO]** El mandato genera necesidades; cada necesidad se cubre con una función; cada
función es un módulo. Ésta es la traducción completa:

| Necesidad del mandato | Función que la cubre | Módulo |
|---|---|---|
| Crecer durante una década | Capturar el crecimiento empresarial global | 🚀 Motor |
| No depender solo del ciclo alcista | Exposición productiva menos cíclica | 🌿 Defensivos |
| Aspirar a algo más que el mercado | Fuentes adicionales de rentabilidad esperada | ⚡ Aceleración |
| Crecimiento fuera del mundo desarrollado | Exposición dedicada a emergentes | 🌍 Emergentes |
| Estabilidad y munición en caídas | Estabilizar y financiar compras | ⚓ Freno |
| Protección frente a inflación | Comportamiento ligado a activos reales | 🥇 Activos Reales |
| Potencial extraordinario acotado | Opcionalidad con pérdida limitada por tamaño | 💥 Asimetría |
| Poder ejecutar sin vender | Capacidad operativa | 💧 Reserva *(capa de ejecución)* |
| Comprar empresas concretas solo a precio | Selección directa condicional | 🎯 Convicción *(capa, 0-14%)* |

Nótese qué **no** aparece: ningún producto. Los vehículos llegan en el capítulo 14,
al final de la cadena — que es exactamente el orden que la Parte I prometió.

---

## 10.4 La parametrización v1.0

**[MODELO]** Los pesos elegidos para este mandato, en la Fecha Cero:

**Vista A — dónde está todo el dinero** *(módulos + Reserva = 100%)*:

| Módulo | Peso |
|---|---|
| 🚀 Motor | **44%** |
| 🌿 Defensivos | **12%** |
| ⚡ Aceleración | **12%** |
| 🌍 Emergentes | **7%** |
| ⚓ Freno | **9%** |
| 🥇 Activos Reales | **9%** |
| 💥 Asimetría | **4%** |
| *Subtotal módulos* | **97%** |
| 💧 Reserva Operativa | **3%** |
| **Total** | **100%** |

**Vista C — cómo se gobierna:** la bolsa del 47% *(44 Motor ordinario + 3 Reserva + 0
Convicción)*, con el techo de Convicción del 14% como presupuesto, no cuota.

Tres advertencias que evitan leer esta tabla como lo que no es:

- ⚠️ **Ningún peso es «perfecto».** Son **la parametrización escogida para este mandato
  con la información disponible en la Fecha Cero** — juicio razonado y registrado, no
  optimización matemática ni porcentajes universales.
- ⚠️ **La lógica de cada peso se defiende módulo a módulo en el capítulo 11**, no aquí en
  bloque: cada uno tiene su porqué, su riesgo y su alternativa estudiada.
- ⚠️ **Convicción no es una fila de esta tabla** — es una etiqueta de gobernanza *(Parte
  I, caps. 4-5)*. Cuando se despliegue, su capital seguirá contado una sola vez en su
  módulo estructural.

---

## 10.5 Versionado: la implementación evoluciona sin rehacer el libro

**[MODELO]** Esta implementación se denomina formalmente:

> ## **Peaky Minders Global 10Y — v1.0**

Si el grupo modifica algo después *(un vehículo, un peso)*, la versión avanza — v1.1,
v1.2… — con su entrada en el registro de decisiones. **No se rehace el libro**; se anota
qué cambió, por qué y con qué evidencia.

El principio que lo gobierna:

> **La arquitectura puede permanecer estable mientras pesos, exposiciones o vehículos
> mejoran, si nueva evidencia demuestra que existe una implementación mejor de la misma
> función.**

**Cambiar no es sinónimo de error.** Pero no todos los cambios son iguales, y confundir
sus niveles sí lo sería:

| Tipo de cambio | Qué toca | Ejemplo | Gravedad |
|---|---|---|---|
| **De vehículo** | El producto que implementa una función | Sustituir un fondo por otro del mismo índice | Menor — versión nueva y ficha |
| **De peso** | La parametrización | Motor 44 → 42 | Media — exige justificación registrada |
| **De exposición** | Qué busca un módulo por dentro | Añadir un factor a Aceleración | Media-alta — reabre la tesis del módulo |
| **De función** | La arquitectura misma | Eliminar o crear un módulo | Mayor — decisión de arquitectura |
| **De mandato** | El encargo entero | Cambiar horizonte o perfil | La mayor — todo lo demás se revisa |

Y la tabla maestra que resume qué es estable y qué es sustituible:

| Elemento | Estado |
|---|---|
| **Función** | 🔒 Estable |
| **Peso** | 🔧 Parametrizable |
| **Exposición** | 🔧 Parametrizable |
| **Vehículo** | 🔁 Sustituible |
| **X-Ray** | 🔄 Regenerable |
| **Regla de gobernanza** | 🔒 Estable salvo decisión registrada *(Dxx)* |
| **Mandato** | 🔐 Solo cambia mediante decisión mayor |

**Por eso, cambiar más adelante un ETF o mover un 2% no invalida este libro:** el libro
documenta funciones y método; los productos y los decimales son la capa sustituible, y
su historial vive en el registro.

---

## 10.6 Síntesis

> **Un mandato concreto generó nueve necesidades; las necesidades se tradujeron a
> funciones; las funciones recibieron pesos razonados y registrados. Eso es la
> parametrización v1.0: la mejor respuesta del equipo en la Fecha Cero — revisable con
> evidencia, versionable sin rehacer nada, y nunca presentada como perfecta.**

El capítulo 11 defiende cada módulo uno a uno; el 12 y el 13, las dos capas; el 14, los
vehículos que lo implementan todo.

---

## CIERRE — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes | Remisiones |
|---|---|---|---|---|---|
| D54 *(mandato)* · D75 *(funciones)* · D73 *(Motor 44 con su composición)* · D48-D50 *(bolsa del 47%, Reserva)* · D78-D79 *(vistas y terminología)* | La cadena mandato→funciones→pesos con el registro fechado como prueba de orden · la suma 97+3=100 verificada | Los pesos son juicio, no optimización *(declarado)* · la tensión «10 años + agresivo» del mandato se examina en el cap. 3 y la Parte IV | ① La cadena con sus capítulos ② Tabla necesidad→función→módulo ③ La parametrización en vista A ④ La tabla maestra estable/sustituible | — *(este capítulo no usa datos de producto)* | **Cap. 3** *(mandato en detalle)* · **Cap. 11** *(defensa de cada peso)* · **Caps. 12-13** *(reglas)* · **Cap. 14** *(vehículos)* · **Anexo B** *(registro)* |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Borrador v1** — cadena mandato→necesidades→funciones→pesos, parametrización v1.0 en vista A *(97+3)*, versionado con los cinco niveles de cambio y la tabla maestra estable/sustituible |



<!-- ══════════════════════════════════════════════════════════ -->

# ▓▓▓ BLOQUE 3 · CAPÍTULO 11 ▓▓▓

---

# CAPÍTULO 11 — LOS SIETE MÓDULOS IMPLEMENTADOS

## Investment Book · Parte II · Borrador v1 · 13 de agosto de 2026

> **Convención:** **[MODELO]** = decisión propia · **[EVIDENCIA EXTERNA]** = requiere
> fuente. Datos de producto: ✅ verificado en fuente primaria *(documento oficial del
> fondo)* · 🟡 verificado en fuente secundaria *(catálogo del distribuidor o plataforma de
> análisis)*, pendiente de primaria · 🔴 no usar todavía.
>
> ⚠️ **Estado de verificación general:** a fecha de este borrador, **los datos de producto
> proceden de fuentes secundarias consultadas el 13-ago-2026** *(catálogo MyInvestor y
> fichas Morningstar)*. **Los documentos oficiales (KID) de los vehículos están pendientes:
> por eso ningún dato de producto lleva ✅ todavía.** Cuando se verifiquen, este capítulo
> actualizará las etiquetas sin cambiar su estructura.

Cada módulo responde las mismas diez preguntas: para qué existe, qué problema resuelve,
por qué ese peso, qué exposición busca, qué vehículo la implementa, qué aporta, qué
riesgos introduce, qué solapa, qué alternativa se estudió y qué nos haría cambiarlo.

---

## 11.1 🚀 Motor — 44%

**Para qué existe y qué problema resuelve.** Es la fuente principal de crecimiento: captura
el beneficio agregado de las empresas cotizadas del mundo. Sin él, la cartera no tendría
motor de largo plazo — de ahí el nombre.

**Por qué el 44%.** Es el peso mayor porque es la función que menos habilidad exige y más
evidencia acumula a su favor **[EVIDENCIA EXTERNA — SPIVA; Bessembinder, pendientes de
cita formal]**. La cifra exacta es parametrización *(cap. 10)*: suficiente para dominar el
crecimiento de la cartera, sin ahogar al resto de funciones.

**Qué exposición busca — y cómo hay que contarla.** [MODELO]

> ### **Motor global con mayor peso estructural de Estados Unidos.**

Dos piezas: el **ancla global** *(un fondo del mercado mundial, emergentes incluidos)* y la
**sobreponderación deliberada de EEUU** *(un fondo del índice S&P 500)*. ❌ **No son dos
fuentes independientes de diversificación y nunca se presentan así**: comparten muchas de
las mayores compañías y su comportamiento está estrechamente ligado. **El solapamiento es
la tesis, no un descuido** — si no lo hubiera, no habría sobreponderación. Es un riesgo
declarado aquí y cuantificado en la Parte III *(caps. 16 y 18)*.

**Vehículos** *(versión de referencia v1.0)*:

| Pieza | Vehículo | ISIN | Coste | Estado |
|---|---|---|---|---|
| Tilt EEUU · 22% | iShares Core S&P 500 UCITS ETF | `IE00B5BMR087` | 0,07% | 🟡 catálogo 13-ago |
| Ancla global · 22% | Vanguard FTSE All-World UCITS ETF Acc | `IE00BK5BQT80` | 0,14% | 🟡 catálogo 13-ago |

**Qué aporta.** La beta del mercado mundial más una convicción estratégica sobre el
ecosistema empresarial estadounidense — cuya defensa completa *(escala, productividad,
mercados de capitales, beneficios)* exige el dossier de evidencia registrado como
pendiente **[EVIDENCIA EXTERNA — dossier macro del tilt, por construir]**.

**Riesgos que introduce.** Concentración geográfica en EEUU y sectorial en tecnología por
encima de un índice mundial estándar; sensibilidad plena a las caídas de mercado; y el
compromiso de gobernanza más duro de la cartera: **mantener el tilt aunque EEUU lo haga
peor durante años** — compromiso registrado *(D73)* con su criterio de revisión.

**Solapamientos.** Entre sus dos piezas *(deliberado)*; con Emergentes a través del ancla
global *(deliberado y medido — cap. 16)*; con Defensivos y Aceleración en las mayores
compañías *(medido en el X-Ray)*.

**Alternativa estudiada.** Un vehículo único de mercados desarrollados *(Motor «A»)*: menor
concentración y menor coste de gobernanza, sin tilt y sin emergentes. **Se estudió a fondo,
con su propio análisis completo, y se descartó por decisión del equipo** — el expediente
íntegro se conserva *(anexo C)* y sus ventajas medidas quedan reconocidas en la decisión
que lo descartó *(D73)*.

**Qué nos haría cambiarlo.** Lo fija D73: un cambio del objetivo del mandato *(de
sobreponderar EEUU a ampliar cobertura global — en cuyo caso el instrumento correcto sería
el ancla global sola)*, o la invalidación de la evidencia metodológica pendiente.
**Expresamente excluido como motivo: la rentabilidad relativa reciente.**

---

## 11.2 🌿 Defensivos — 12%

**Para qué existe y qué problema resuelve.** Mantener exposición a empresas cuyos
beneficios dependen menos del ciclo: lo que la gente sigue comprando —alimentación,
higiene, medicinas— cuando la economía se tuerce. Reduce la sensibilidad del conjunto sin
salir de la renta variable.

**Por qué el 12%.** Suficiente para notarse en un año malo; no tanto como para lastrar una
década buena. Parametrización razonada, no cifra mágica.

**Qué exposición busca.** Dos mitades: consumo básico global y salud.

**Vehículos** *(versión de referencia)*:

| Pieza | Vehículo | ISIN | Coste | Estado |
|---|---|---|---|---|
| Consumo básico · 6% | Xtrackers MSCI World Consumer Staples | `IE00BM67HN09` | 0,25% | 🟡 catálogo |
| Salud · 6% | iShares S&P 500 Health Care | `IE00B43HR379` | 0,15% | 🟡 catálogo |

**Qué aporta.** Beneficios más estables y, históricamente, mejores caídas relativas en
recesiones — sin garantía de que ocurra en todas *(regla del cap. 5)*.

**Riesgos que introduce.** ⚠️ El vehículo de salud replica un índice **exclusivamente
estadounidense**: un 6% de la cartera queda en un solo sector de un solo país. Es el
bloque más concentrado geográficamente y se declara como tal — y se suma al tilt del Motor
en la cuenta total de EEUU *(cap. 16)*.

**Solapamientos.** Sus empresas también están en el Motor *(el módulo las sobrepondera, no
las descubre)*.

**Alternativa estudiada.** Un fondo de salud de gestión activa se comparó con el vehículo
indexado; la comparación —coste frente a resultado— favoreció al indexado y quedó
registrada. También se evaluó un fondo activo de salud global como candidato *(registro
del proyecto)*.

**Qué nos haría cambiarlo.** Un vehículo de salud global comparable en coste *(eliminaría
la concentración EEUU del bloque)*; o evidencia de que la mitad de salud duplica riesgos
que el mandato no quiere.

---

## 11.3 ⚡ Aceleración — 12%

**Para qué existe y qué problema resuelve.** Buscar fuentes adicionales de rentabilidad
esperada sobre el mercado neutral: primas documentadas por la investigación académica
**[EVIDENCIA EXTERNA — Fama-French; Asness et al., pendientes de cita formal]** — tamaño
pequeño, valoración baja, combinación de factores.

**Por qué el 12%.** Las primas son inciertas y pasan años sin aparecer: peso suficiente
para que importen si llegan, acotado para que su ausencia no hunda el plan.

**Qué exposición busca.** Tres vías: pequeñas compañías globales *(4%)*, valor global de
gestión activa *(4%)* y multifactor europeo *(4%)*.

**Vehículos** *(versión de referencia)*:

| Pieza | Vehículo | ISIN | Coste | Estado |
|---|---|---|---|---|
| Tamaño · 4% | Vanguard Global Small-Cap Index EUR Acc | `IE00B42W4L06` | 0,30% | 🟡 catálogo |
| Valor · 4% | Robeco BP Global Premium Eq D Acc EUR | `LU0203975437` | 1,46% | 🟡 catálogo |
| Multifactor · 4% | iShares STOXX Europe Equity Multifactor | `IE00BZ0PKV06` | 0,25% | 🟡 catálogo |

**La lección de las pequeñas compañías — la función sobrevivió a los vehículos.** Esta
casilla cambió de forma durante la construcción *(composición del bloque, candidatos,
clases)* y su análisis se realiza con un producto sustituto del mismo índice **(proxy:
SPDR MSCI World Small Cap, `IE00BCBJG560` — regla D77: del proxy se toman geografía,
sectores y estilo; nunca coste, fiscalidad ni condiciones contractuales, que son las del
Vanguard)**. A pesar de todos esos cambios, **la función —capturar la prima de tamaño—
no se movió**. Es la demostración práctica de la tabla maestra del cap. 10: vehículo
sustituible, función estable.

**Qué aporta.** Exposición a primas distintas de la beta — y el multifactor europeo, de
paso, el único contrapeso geográfico material al peso de EEUU.

**Riesgos que introduce.** Las primas pueden no pagar durante períodos larguísimos; el
vehículo de valor es caro *(1,46%)* y de gestión delegada — su justificación frente a
alternativas indexadas es una pregunta de investigación abierta y registrada *(D67)* que
este libro responde en este capítulo o declara pendiente; y los tres vehículos pueden
moverse muy juntos — medido en el cap. 18.

**Solapamientos.** Con el Motor *(son renta variable global)*: **el bloque diversifica el
origen de la prima, no el riesgo** — formulación registrada tras medirlo.

**Alternativa estudiada.** Un fondo de calidad global: se probó y se descartó porque el
análisis cuestionó que aportara suficiente diferenciación respecto al núcleo *(cifras en
el cap. 14)*. También se evaluaron vehículos alternativos de valor indexado.

**Qué nos haría cambiarlo.** Respuesta negativa a las preguntas D67 sobre el vehículo de
valor *(¿justifica su coste?)*; o evidencia de que alguna pieza no captura la prima que
dice capturar.

---

## 11.4 🌍 Emergentes — 7%

**Para qué existe y qué problema resuelve.** Exposición dedicada al crecimiento de las
economías emergentes, con peso propio y modificable con independencia del Motor.

**Por qué el 7%.** Peso deliberadamente moderado: relevante para participar, acotado
frente a la volatilidad y los riesgos institucionales de esos mercados.

**⚠️ La cifra que hay que leer bien.** **El 7% es el peso de la decisión dedicada — no la
exposición económica total.** El ancla global del Motor también contiene emergentes; la
exposición total es mayor que el 7% y se cuantifica mirando dentro *(cap. 16)*. **Es una
sobreponderación deliberada y declarada**, no un descuido *(D73)*.

**Vehículo** *(versión de referencia)*:

| Vehículo | ISIN | Coste | Estado |
|---|---|---|---|
| iShares Emerging Markets Index **clase S** | `IE000QAZP7L2` | 0,16% | 🟡 catálogo 13-ago · ⚠️ **identidad de clase pendiente de confirmar contra documentación contractual vigente antes de imprimirse como definitiva**; el análisis X-Ray usó la clase D del mismo fondo como proxy declarado |

**Qué aporta.** Crecimiento demográfico y económico no recogido por los índices
desarrollados; diversificación geográfica parcial.

**Riesgos que introduce.** Volatilidad superior; riesgo político y de gobernanza;
concentración asiática *(los mayores países del índice)*.

**Solapamientos.** Con el Motor vía ancla global — el deliberado del punto anterior.

**Alternativa estudiada.** Incluir Japón como pieza separada: se descartó al comprobar que
la exposición deseada ya quedaba razonablemente cubierta, y su peso se reasignó
*(registro del proyecto)*.

**Qué nos haría cambiarlo.** Que la exposición total medida *(bloque + Motor)* superara de
forma sostenida lo que el mandato tolera; se revisa con el X-Ray periódico.

---

## 11.5 ⚓ Freno — 9%

**Para qué existe y qué problema resuelve.** Estabilizar: la parte de la cartera que no
depende de que la bolsa suba, aporta liquidez estratégica y amortigua — busca amortiguar
determinadas caídas, sin garantía de lograrlo en todas *(regla del cap. 5)*.

**Por qué el 9%.** En un mandato agresivo a diez años, el estabilizador es deliberadamente
pequeño: suficiente para dar estabilidad y financiar oportunidades, sin renunciar al
crecimiento que el mandato pide.

**Qué exposición busca.** Dos pisos: liquidez remunerada de máxima estabilidad *(6%)* y
renta fija con algo más de recorrido *(3%)*.

**Vehículos** *(versión de referencia)*:

| Pieza | Vehículo | ISIN | Coste | Estado |
|---|---|---|---|---|
| Monetario · 6% | AXA Trésor Court Terme C | `FR0000447823` | 0,06% | 🟡 catálogo |
| Renta fija · 3% | PIMCO GIS Income E EUR (H) Acc | `IE00B84J9L26` | 1,45% | 🟡 ficha Morningstar · 🔴 **KID pendiente** |

⚠️ **Sobre la segunda pieza, con total claridad:** el PIMCO es **el vehículo vigente de la
versión analizada, sujeto a revisión de implementación** — el equipo está revisando si
sigue siendo la mejor opción para ese 3% **por su coste**. **La función del Freno no
depende de que el PIMCO permanezca**: si se sustituye, cambiará la fila de esta tabla y la
versión *(v1.x)*, no el módulo. Además, su mandato es amplio *(renta fija flexible)*: esa
amplitud es el riesgo específico que se vigila, y aporta a la cartera una duración y un
perfil de crédito que se miden en la Parte III.

**Qué aporta.** Estabilidad, rentas y la materia prima del rebalanceo.

**Riesgos que introduce.** El monetario no es una cuenta corriente *(es un fondo, con su
naturaleza)*; la pieza de renta fija introduce sensibilidad a tipos y crédito, y su coste
es alto para el módulo.

**Solapamientos.** Funcionales con la Reserva **solo en apariencia**: la tabla del cap. 5
los separa — el Freno es asignación estratégica; la Reserva, capacidad operativa.

**Alternativa estudiada.** Renta fija global indexada de corto plazo y bajo coste — fue la
pieza de referencia anterior y es candidata natural si la revisión del vehículo vigente
concluye que el coste no se justifica *(registro del proyecto)*.

**Qué nos haría cambiarlo.** La revisión en curso del coste de la segunda pieza; o que la
duración/crédito medidos *(Parte III)* excedan lo que la función estabilizadora tolera.

---

## 11.6 🥇 Activos Reales — 9%

**Para qué existe y qué problema resuelve.** Comportamiento ligado a activos reales e
inflación, distinto de acciones y bonos nominales: la parte pensada para los escenarios
donde el dinero pierde valor o la confianza monetaria se resiente.

**Por qué el 9%.** Peso de seguro: material si el escenario llega, asumible si no llega.

**Qué exposición busca.** Oro físico *(7%)* como reserva de valor; cobre *(2%)* como metal
industrial ligado al ciclo real.

**Vehículos** *(versión de referencia)*:

| Pieza | Vehículo | ISIN | Coste | Estado |
|---|---|---|---|---|
| Oro · 7% | WisdomTree **Core** Physical Gold | `JE00BN2CJ301` | 0,12% | 🟡 catálogo |
| Cobre · 2% | WisdomTree Copper | `GB00B15KXQ89` | 0,49% | 🟡 catálogo |

⚠️ Dos matices honestos: el oro es físico asignado; **el cobre no** — es un producto sobre
futuros con estructura de deuda, mecánica distinta que se declara *(y su análisis X-Ray
usó una clase con cobertura de divisa distinta: limitación registrada, cap. 14)*.

**Qué aporta.** El oro, la descorrelación histórica más citada de la cartera — medida en la
Parte III con su fuente y ventana. El cobre, exposición al ciclo industrial real.

**Riesgos que introduce.** El oro no produce rentas y puede pasar décadas planas; el cobre
es volátil y cíclico; ninguno de los dos «garantiza» protección.

**Solapamientos.** Mínimos por construcción — es el módulo más distinto del resto.

**Alternativa estudiada.** Mineras de oro *(descartadas por diseño: son renta variable,
con volatilidad muy superior al metal)*; cestas amplias de materias primas *(descartadas:
mezclan exposiciones no buscadas)*; y clases más caras del mismo oro *(descartadas por
coste)* — todo en el registro.

**Qué nos haría cambiarlo.** Un vehículo de cobre físico o de mejor estructura a coste
comparable; o que el papel del oro deje de sostenerse en la evidencia medida.

---

## 11.7 💥 Asimetría — 4%

**Para qué existe y qué problema resuelve.** Opcionalidad: una posición cuyo potencial
alcista es muy alto en relación con el daño máximo que su tamaño puede causar. La
asimetría está **en el tamaño**, no en el activo.

**Por qué el 4%.** Es la respuesta a la pregunta de control del módulo: *¿aceptaríamos su
pérdida prácticamente total sin comprometer el plan?* Con un 4%, sí. Con un 15%, no —
dejaría de ser Asimetría y sería concentración.

**Qué exposición busca.** Bitcoin, con custodia institucional y formato cotizado.

**Vehículo** *(versión de referencia)*:

| Vehículo | ISIN | Coste | Estado |
|---|---|---|---|
| 21Shares Bitcoin Core ETP | `CH1199067674` | 0,10% | 🟡 catálogo |

**Qué aporta.** Un recorrido posible no ligado a los beneficios empresariales ni a los
tipos — y la disciplina de tener la posición especulativa **regulada y acotada** en lugar
de negada o improvisada.

**Riesgos que introduce.** Volatilidad extrema y caídas históricas superiores al 70%
**[EVIDENCIA EXTERNA — episodios concretos pendientes de cita con fuente]**; riesgo
regulatorio; correlación no nula con el mercado en momentos de tensión *(medida, cap. 18)*.

**Solapamientos.** Ninguno estructural.

**Alternativa estudiada.** Cestas de criptoactivos diversificadas — descartadas tras
comparar su histórico de caídas con el del activo principal *(registro del proyecto)*; y
la alternativa de no tener el módulo, descartada por el mandato agresivo con pérdida
acotada.

**Qué nos haría cambiarlo.** Que el tamaño creciera hasta romper la pregunta de control
*(la política de sobreponderaciones, pendiente, lo regulará — D47b)*; o un cambio
regulatorio que altere la custodia o el vehículo.

---

## 11.8 Síntesis

> **Siete módulos, siete porqués, siete «qué nos haría cambiarlo». Ningún peso se presenta
> como perfecto y ningún vehículo como eterno: las funciones son estables; casi todo lo
> demás es parametrizable o sustituible, con registro. La defensa detallada de los números
> —cuánto EEUU, cuánta tecnología, cuánto solapamiento— pertenece a la Parte III, donde se
> mide en lugar de afirmarse.**

---

## CIERRE — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes | Remisiones |
|---|---|---|---|---|---|
| D73 *(Motor y su criterio de revisión)* · D77 *(proxy small caps)* · D67 *(preguntas Robeco/PIMCO — abiertas)* · D68 *(identificación del PIMCO)* · D75-D79 *(funciones y capas)* | Cada módulo con sus diez respuestas; alternativas estudiadas trazadas al registro; suma de piezas = 97% + Reserva | **Todos los datos de producto en 🟡** *(KID pendientes)* · PIMCO expresamente **sujeto a revisión de implementación** · clase exacta de Emergentes pendiente de confirmación contractual · dossier macro del tilt sin construir · D67 sin responder | ① Ficha visual por módulo *(10 preguntas)* ② El Motor como ancla+tilt ③ El mapa de solapamientos declarados | 🔴 **13 KID** *(todos los costes e identidades)* · 🟠 dossier macro del Motor · 🟠 episodios de caídas de bitcoin con fuente · 🟠 SPIVA/Bessembinder/Fama-French/Asness *(citas formales)* · 🟡 confirmación de clase de Emergentes | **Cap. 14** *(vehículos, proxies y descartados con detalle)* · **Caps. 16-18** *(las cifras: EEUU total, emergentes total, correlaciones)* · **Cap. 12** *(la capa que puede sobreponerse al Motor)* · **D47b** *(sobreponderaciones — pendiente)* |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Borrador v1** — los siete módulos con estructura homogénea de diez respuestas. Motor presentado como *global con mayor peso estructural de EEUU* *(ancla + tilt, solapamiento declarado)* · PIMCO como **vehículo vigente sujeto a revisión de implementación** · Emergentes con el 7% como decisión dedicada, no exposición total, y clase pendiente de confirmación · small caps con la lección *«la función sobrevivió a los vehículos»* y D77 · **todos los datos de producto etiquetados 🟡 con los KID en 🔴 pendiente** |



<!-- ══════════════════════════════════════════════════════════ -->

# ▓▓▓ BLOQUE 4 · CAPÍTULO 12 ▓▓▓

---

# CAPÍTULO 12 — LA CAPA DE CONVICCIÓN: EL PROTOCOLO COMPLETO

## Investment Book · Parte II · Borrador v1 · 13 de agosto de 2026

> **Convención:** **[MODELO]** = decisión propia · **[EVIDENCIA EXTERNA]** = requiere
> fuente.
>
> El capítulo 5 presentó el principio de la capa de Convicción. Este capítulo la convierte
> en protocolo operativo — y una advertencia preside todo lo demás: **nada de lo que sigue
> es una invitación a usar la capa. Hoy está al 0%, y podría estarlo siempre. El 14% es
> techo, no cuota.**

---

## 12.1 Qué es y qué no es — recordatorio en tres líneas

**[MODELO]** La capa de Convicción es el derecho —no la obligación— de comprar empresas
concretas bajo un protocolo escrito de antemano. No es una clase de activo *(cada compra
recibe su módulo estructural)*, no tiene objetivo de peso *(solo techo del 14%)* y no se
activa por calendario ni por aburrimiento: **solo por precio y tesis.**

---

## 12.2 El universo: quién puede entrar

**[MODELO]** Ninguna empresa puede comprarse si antes no está en el **universo de
Convicción**, y para entrar necesita **siete documentos completos**:

```
1. Análisis fundamental          5. Riesgos principales
2. Tesis de inversión escrita    6. Horizonte fundamental
3. Valoración                    7. Criterios de invalidación
4. IDC (precio de entrada)
```

Sin los siete, la empresa no existe para la capa — **aunque su precio parezca
atractivo**. El universo admite **hasta siete compañías**; no siete obligatorias: si solo
tres merecen los siete documentos, el universo tiene tres.

---

## 12.3 El IDC: el precio de entrada, bien formulado

**[MODELO]** El IDC es el precio de entrada derivado de nuestra valoración. Está
construido de modo que, **si las hipótesis del análisis se cumplen**, la rentabilidad
anualizada esperada desde ese precio ronde el 15% a cinco años.

La formulación importa tanto como el número:

| ❌ Prohibido decir | ✅ Se dice |
|---|---|
| «la acción dará como mínimo un 15%» | «el precio ofrece aproximadamente un 15% anual **implícito según el modelo, condicionado al cumplimiento de las hipótesis**» |
| «rentabilidad garantizada» | «rentabilidad esperada bajo un modelo» |

Y la regla fundacional: **el margen de seguridad ya está dentro del IDC.** No se aplican
descuentos adicionales sobre él — exigir «un 15% por debajo del IDC» sería duplicar el
margen y bloquear entradas válidas.

---

## 12.4 La regla de compra: dos tramos y se acabó

**[MODELO]**

```
TRAMO 1 · hasta el 1% del valor total de la cartera
  CONDICIÓN:  precio ≤ IDC  +  tesis intacta
  (el 1% se mide sobre el valor de la cartera INMEDIATAMENTE ANTES de ejecutar)

TRAMO 2 · hasta otro 1%
  CONDICIÓN:  precio ≤ 0,90 × IDC  +  NUEVA revisión completa de la tesis
  LÍMITE:     la posición directa no supera ≈2% del valor de la cartera al ejecutar

DESPUÉS DEL TRAMO 2 NO SE COMPRA MÁS EN ESA EMPRESA, AUNQUE SIGA CAYENDO.
```

Tres consecuencias del diseño:

- **Elimina el promedio infinito a la baja** — el error clásico de «comprar más porque ha
  caído más» tiene un tope estructural de dos decisiones.
- **Una caída con tesis deteriorada no habilita nada.** El precio es condición necesaria,
  nunca suficiente.
- **Los importes son proporcionales, no fijos**: como la cartera crece, dos tramos
  ejecutados en momentos distintos difieren en euros. Es deliberado.

**Límites agregados:** hasta 7 empresas · máximo ≈2% de capital asignado por empresa ·
máximo 14% del conjunto por nuevas decisiones de compra. Si el mercado revaloriza una
posición por encima de esos pesos, **no hay venta automática** — el tratamiento de las
sobreponderaciones pertenece a la política de ventas, pendiente y registrada como tal.

---

## 12.5 Si hay varias oportunidades y poco capital

**[MODELO]** La financiación de cada mes es la aportación más la Reserva disponible
*(cap. 13)*. Si las oportunidades válidas superan el capital:

1. **Todas deben cumplirlo todo** — tesis intacta, IDC formal, precio habilitado.
2. **Se ordenan por mayor descuento porcentual sobre su IDC** y se ejecutan en ese orden
   hasta agotar el capital. Un solo criterio, verificable, sin discrecionalidad añadida.
3. **Lo no ejecutado no genera derecho acumulado.** El mes siguiente se reevalúa desde
   cero: si sigue en precio, vuelve a competir; si subió, salió.

Y el compromiso de los dos relojes *(cap. 5)*: el despliegue es **gradual por diseño**.
Preferimos comprar menos compañías al precio previamente definido que forzar liquidez
para capturar un mínimo de mercado.

---

## 12.6 La Fecha Cero y la cohorte real: el antídoto del autoengaño

**[MODELO]** La trampa clásica de la selección de empresas es retrospectiva: calcular el
precio de entrada *después* de ver el gráfico y presentarlo como disciplina. El protocolo
la bloquea con dos piezas:

**La Fecha Cero.** Una tabla fechada con la cohorte inicial de candidatas: compañía,
mercado, divisa, IDC, precio de referencia, distancia al IDC, fecha de valoración y
estado *(en precio / cerca / en espera)*. 🔴 **Prohibido aplicar retrospectivamente un IDC
calculado después y presentarlo como decisión previa.** Todo estudio hacia atrás se
etiqueta «simulación retrospectiva» — sin esa etiqueta no vale nada.

**La cohorte real.** De cada operación real se registra: fecha, precio, IDC vigente,
valor de la cartera, importe, tramo, tesis y motivo. Con eso, dentro de cinco años el
resultado podrá evaluarse **sin reescribir la historia**.

⚠️ Estado a fecha de este borrador: **la tabla de la Fecha Cero está pendiente de
construcción** *(exige las valoraciones con IDC de las candidatas — hueco declarado, no
relleno)*.

---

## 12.7 Cómo se mide el éxito: contra el Motor, no contra cero

**[MODELO]** Cada posición de la capa se evalúa a su horizonte fundamental contra **la
alternativa real que sustituyó: el Motor.**

```
exceso = rentabilidad anualizada de la acción − rentabilidad anualizada del Motor
```

**Ganar dinero no basta.** Si una selección renta un 9% mientras el Motor rentaba un 11%,
la capa destruyó valor aunque el saldo sea positivo — y el compromiso registrado es
decirlo así. El presupuesto de impacto es simétrico y se publica con sus dos caras: con un
diferencial favorable de 5 puntos, la capa completa añadiría en torno a 0,7 puntos anuales
a la cartera; con el mismo diferencial en contra, los restaría.

**Años 1-4 se evalúa la tesis, no la cotización:** crecimiento, márgenes, caja, balance,
ventaja competitiva. Una caída no demuestra que la tesis falle; **una subida tampoco
demuestra que fuera correcta** — la segunda mitad de esa frase es la difícil.

---

## 12.8 Síntesis

> **Siete documentos para entrar, un precio escrito para comprar, dos tramos como máximo,
> prioridad por descuento cuando falte capital, Fecha Cero contra el autoengaño y el Motor
> como vara de medir. Y sobre todo: una capa que puede quedarse en cero para siempre sin
> que nada falle — porque el 14% es un límite de riesgo, no una promesa de actividad.**

---

## CIERRE — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes | Remisiones |
|---|---|---|---|---|---|
| D45-D46 *(límite, no orden)* · D49 *(dos tramos)* · D55 *(formulación del IDC)* · D57 *(1% medido antes de ejecutar)* · D58 *(priorización y no acumulación)* · D59 *(despliegue gradual)* · D60 *(benchmark Motor y simetría)* · D61 *(Fecha Cero)* | El protocolo completo consolidado en el documento operativo del proyecto; el árbol de decisión verificable sin interpretación añadida | 🔴 **Fecha Cero sin construir** *(exige valoraciones con IDC — hueco declarado)* · política de ventas por sobreponderación **pendiente** *(D47b)* · cero fichas de empresa a fecha del borrador | ① El embudo: universo→precio→tramos ② Los dos tramos con el tope ③ Tabla de la Fecha Cero *(plantilla)* ④ El presupuesto simétrico de impacto | 🟠 Las valoraciones con IDC de las candidatas *(mínimo tres para el estándar del trabajo)* | **Cap. 5** *(el principio de la capa)* · **Cap. 13** *(la financiación)* · **Cap. 24** *(seguimiento y cohorte)* · **D47b** *(ventas — pendiente)* |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Borrador v1** — protocolo completo en 8 secciones: universo de siete documentos, IDC con formulación obligatoria, dos tramos con fin del promedio infinito, priorización por descuento, Fecha Cero contra el sesgo retrospectivo y evaluación contra el Motor con presupuesto simétrico. **Sin invitación a desplegar: 0% inicial, 14% techo.** Huecos declarados: Fecha Cero y fichas con IDC |



<!-- ══════════════════════════════════════════════════════════ -->

# ▓▓▓ BLOQUE 5 · CAPÍTULO 13 ▓▓▓

---

# CAPÍTULO 13 — RESERVA OPERATIVA Y FLUJO DE APORTACIONES

## Investment Book · Parte II · Borrador v1 · 13 de agosto de 2026

> **Convención:** **[MODELO]** = decisión propia · **[EVIDENCIA EXTERNA]** = requiere
> fuente.
>
> **La frase que gobierna este capítulo:**
>
> ### **«La aportación mensual no replica la cartera: la rebalancea.»**

---

## 13.1 El problema que resuelve el flujo

Cada mes entran 1.000 € nuevos. La reacción instintiva sería repartirlos como está
repartida la cartera: 440 al Motor, 120 a Defensivos… **[MODELO]** Ese reparto
proporcional es exactamente lo que **no** se hace, por una razón simple: perpetúa las
desviaciones en lugar de corregirlas — mete dinero en lo que ya está sobre su objetivo y
no repone lo que se quedó atrás.

En este mandato el flujo es una herramienta enorme: 12.000 € al año sobre una cartera
inicial de 100.000 permiten corregir las desviaciones típicas de todos los módulos
**sin vender nada** — con lo que el rebalanceo casi no genera coste ni fricción.

---

## 13.2 El árbol de decisión mensual

**[MODELO]** Cada mes, los 1.000 € siguen este camino y no otro:

```
ENTRAN 1.000 €
   │
   ├─ PASO 1 · ¿Hay alguna empresa del universo de Convicción
   │           con precio ≤ IDC y tesis intacta?
   │
   │     SÍ → CONVICCIÓN TIENE PRIORIDAD.
   │          La aportación puede ir íntegra a esa compra
   │          (más la Reserva disponible si hace falta).
   │
   └─ NO → PASO 2 · ¿Hay algún módulo por debajo de su objetivo?
              │
              ├─ SÍ → los 1.000 € van AL MÓDULO CON MAYOR DESVIACIÓN
              │        NEGATIVA (uno solo; no se reparte).
              │
              └─ NO → PASO 3 · los 1.000 € van AL MOTOR
                       (destino indexado por defecto).
```

Tres reglas cierran el árbol para que no admita interpretación:

1. **La Reserva participa en el ranking de infraponderación como un bloque más.** Si se
   consumió ejecutando una compra, compite por las aportaciones siguientes y se
   reconstruye sola — sin regla especial.
2. **La capa de Convicción NUNCA aparece en ese ranking.** Su objetivo es 0%; no tiene
   hueco que rellenar. Su única puerta es el paso 1: precio y tesis.
3. **Lo no ejecutado caduca.** Si un mes hubo cinco oportunidades y capital para dos, las
   tres restantes no quedan «pendientes»: el mes siguiente se reevalúa todo desde cero.

---

## 13.3 La Reserva en operación

**[MODELO]** La fórmula del capítulo 5 — *la política es permanente; el capital es
transitorio* — se traduce operativamente así:

- **Capacidad objetivo/máxima: 3%** del patrimonio, en efectivo remunerado.
- **Se consume** cuando una compra de Convicción necesita más que la aportación del mes.
- **Se reconstruye** por el árbol del §13.2: al quedar por debajo de su capacidad, entra
  en el ranking y las aportaciones la reponen.
- **No se recarga por miedo** — su tamaño no sube porque el mercado «parezca caro», ni
  baja porque parezca barato. No expresa opiniones.

Ejemplo completo con números redondos: en un mes aparecen tres empresas en precio.
Financiación disponible: 1.000 € de aportación + 3.000 € de Reserva = 4.000 €. Se ejecutan
las compras por orden de descuento *(cap. 12)*; la Reserva queda en 1.000 €. Los meses
siguientes, sin nuevas oportunidades, el árbol la detecta infraponderada y la reconstruye
hacia el 3%. **Ninguna venta en todo el proceso.**

---

## 13.4 Lo que las aportaciones no pueden hacer

**[MODELO]** El mecanismo tiene un límite estructural que hay que decir en voz alta:

> ### **Las aportaciones solo suman. Nunca restan.**

Pueden corregir un módulo que se quedó **corto**; no pueden reducir uno que creció
**demasiado**. Si una posición muy volátil se multiplica y desborda sus límites, el flujo
mensual tardaría años en diluirla — la única herramienta real para eso son las ventas, y
**la política de ventas por sobreponderación está pendiente y registrada como tal**
*(D47b)*. Este libro no la improvisa: declara el hueco y remite a su cierre.

Mientras tanto, la vigilancia existe: los pesos se comparan con sus objetivos en cada
revisión, y una sobreponderación material dispara la elaboración de esa política, no una
venta impulsiva.

---

## 13.5 Los dos relojes, versión operativa

El principio del capítulo 5 *(el mercado es continuo; el capital, periódico)* se concreta
aquí en tres consecuencias prácticas:

1. **Entre revisiones no hay cambios rutinarios por ruido de mercado.** Las subidas y
   bajadas normales no disparan órdenes.
2. **Las reglas predefinidas sí actúan en cualquier momento**: una empresa que alcanza su
   IDC, la invalidación de una tesis, un problema sobrevenido en un vehículo. Toda
   actuación fuera de calendario ejecuta una regla escrita — nunca improvisa.
3. **El despliegue de oportunidades es gradual por diseño.** La capacidad de un mes es la
   aportación más la Reserva; si las oportunidades exceden eso, se ejecutan las de mayor
   descuento y el resto caduca. Se prefiere comprar menos al precio correcto que forzar
   liquidez para comprarlo todo.

---

## 13.6 Síntesis

> **Mil euros al mes con un árbol de tres pasos: primero la oportunidad con precio y
> tesis; si no la hay, el módulo más rezagado; si no lo hay, el Motor. La Reserva se
> consume ejecutando y se reconstruye sola. Y el límite queda declarado: las aportaciones
> corrigen lo que falta, nunca lo que sobra — para eso hará falta la política de ventas,
> que está pendiente y no se improvisa aquí.**

---

## CIERRE — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes | Remisiones |
|---|---|---|---|---|---|
| D56 *(árbol de asignación dinámica y sus tres reglas)* · D57-D58 *(importes y priorización)* · D59 *(dos relojes y despliegue gradual)* · D50 *(Reserva)* · D5 *(bandas evaluadas en revisión, no en continuo)* | El árbol es ejecutable sin interpretación *(verificado en el protocolo operativo del proyecto con las ocho preguntas que antes exigían criterio)* · el ejemplo del §13.3 con la aritmética completa | 🔴 **Política de ventas por sobreponderación PENDIENTE** *(D47b)* — el límite del §13.4 queda sin su segunda mitad · el rendimiento del efectivo remunerado de la Reserva, pendiente de cifra con fuente *(cap. 22)* | ① El árbol mensual ② El ciclo consumo→reconstrucción de la Reserva ③ La asimetría «suman/no restan» | 🟡 remuneración del efectivo operativo *(cap. 22)* | **Cap. 12** *(qué es una oportunidad válida)* · **Cap. 5** *(el principio de la capa de ejecución)* · **D47b** *(ventas — pendiente)* · **Cap. 23** *(rebalanceo completo y bandas)* |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Borrador v1** — el árbol mensual con sus tres reglas de cierre *(la Reserva compite, Convicción nunca, lo no ejecutado caduca)*, la Reserva en operación con ejemplo numérico completo, el límite estructural declarado *(las aportaciones no restan — D47b pendiente)* y los dos relojes en versión operativa |



<!-- ══════════════════════════════════════════════════════════ -->

# ▓▓▓ BLOQUE 6 · CAPÍTULO 14 ▓▓▓

---

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



<!-- ══════════════════════════════════════════════════════════ -->

# ▓▓▓ A · AUDITORÍA PARTE I — CAPS. 4-9 ▓▓▓

---

# 🔍 AUDITORÍA DE LA PARTE I — CAPÍTULOS 4 A 9

## 13 de agosto de 2026 · previa a la redacción de la Parte II

> **Regla aplicada:** los capítulos 4-7 están CERRADOS y no se modifican silenciosamente.
> Toda incidencia se registra aquí; ninguna se corrige sin aprobación.

---

## 1. Contradicciones

| # | Incidencia | Gravedad | Veredicto |
|---|---|---|---|
| C1 | **Ninguna contradicción de fondo detectada** entre los seis capítulos: pesos, techos, definiciones de capas, regla anti-doble-conteo y terminología de D78-D79 son consistentes | — | ✅ **No bloqueante — la Parte II puede empezar** |
| C2 | **Deriva terminológica cosmética entre caps. 4 y 5-8:** el cap. 4 *(cerrado antes de la regla de lenguaje reforzada)* usa los nombres ingleses de las tres vistas como primarios *(Total Capital View…)*; los caps. 5-8 usan español primero. No es contradicción de contenido — el cap. 5 introduce las traducciones — pero un lector muy fino notará el cambio de convención | 🟡 | **Registrada, NO corregida** *(cap. 4 cerrado)*. Opcional: nota de convención en la maquetación final |
| C3 | **Mapa módulo→régimen del cap. 4 §4.4:** Emergentes marcado «adverso» en dos cajas es hipótesis discutible que el cap. 19 puede contradecir con datos. Ya está etiquetado «hipótesis de diseño, no evidencia validada» | 🟡 | Cubierto por la etiqueta; se revisará al construir el cap. 19 |
| C4 | El cap. 4 §4.6 dice que el capital del overlay «cuenta una sola vez, en su módulo estructural» y el cap. 5 §5.7 lo desarrolla con la bolsa del 47% — coherentes entre sí y con D78/D79 | — | ✅ |

## 2. Repeticiones

| # | Incidencia | Veredicto |
|---|---|---|
| R1 | La frase *«la arquitectura expresa la intención; el X-Ray verifica/comprueba el resultado»* aparece en caps. 4, 6 y de refilón en 5 | ✅ **Deliberada** — es el eslogan del método; la repetición es retórica, no redundancia de contenido |
| R2 | La regla del proxy *(«del proxy solo se toma…»)* aparece en caps. 6 y 7 | ✅ Aceptable: en 6 como caso, en 7 como campo de la ficha. Ambas remiten a D77 |
| R3 | «La política es permanente; el capital transitorio» en caps. 4, 5 y 9 | ✅ Fórmula canónica; una aparición por contexto |
| R4 | Las pruebas anti-redundancia de cada cierre confirman que ninguna definición se reprodujo íntegra | ✅ |

## 3. Conceptos usados sin explicar

| # | Incidencia | Veredicto |
|---|---|---|
| X1 | **«IDC»** se nombra en caps. 4, 5 y 7 con remisión al cap. 12 pero sin glosa mínima en su primera aparición *(cap. 4 §4.5: «con IDC y protocolo propio»)* | 🟠 **Registrada.** Mitigada porque el cap. 5 §5.3 lo glosa como «precio de entrada»; para la maquetación final conviene una glosa de tres palabras en la primera mención del cap. 4. **No se toca ahora** *(capítulo cerrado)* |
| X2 | «Benchmark» aparece en fichas y tablas sin glosa en la Parte I | 🟡 Va al glosario *(anexo G)*; primera glosa natural en el cap. 12 *(benchmark del bloque = el Motor)* |
| X3 | «UCITS» aparece una vez en el cap. 7 *(tabla ISIN)* sin explicar | 🟡 Glosario |

## 4. Exceso de jerga

| # | Incidencia | Veredicto |
|---|---|---|
| J1 | Cap. 4 es el más denso *(escrito antes del refuerzo de la regla de lenguaje)*: «beta», «idiosincrásico» no aparecen pero «primas factoriales sistemáticas» sí, sin glosa | 🟠 Registrada; el cap. 11 *(Aceleración)* la glosará en llano. Cap. 4 no se toca |
| J2 | Caps. 5-9 cumplen la regla: inglés una vez entre paréntesis, explicación→ejemplo→detalle | ✅ |

## 5. Referencias cruzadas

Verificadas todas las remisiones de los cierres 4→(5-27), 5→(6,12,13,14,15,22), 6→(7,11,15-18), 7→(8,9,11,14,26,H), 8→(5,9,E), 9→(18,22,26,V): **ninguna apunta a un capítulo inexistente ni contradice el índice de 27**. ✅

## 6. Afirmaciones demasiado fuertes / claims sin evidencia

| # | Incidencia | Veredicto |
|---|---|---|
| A1 | Cap. 4 §4.1: «el error más común en carteras» *(cap. 5 §5.1 lo repite)* — afirmación empírica sin fuente | 🟠 **Registrada.** Defendible como observación cualitativa, pero un tribunal exigente puede pedir fuente. Propuesta *(no aplicada)*: suavizar a «un error frecuente» si los capítulos se reabren por otro motivo |
| A2 | Cap. 4 §4.15 marca como [EVIDENCIA EXTERNA] todo lo citado *(SPIVA, Kahneman, Fama-French, Bridgewater, Swensen)* — pendientes de cita formal, correctamente etiquetadas | ✅ etiquetado correcto; pendencia en la lista de fuentes |
| A3 | Cap. 8 v2: las negaciones explícitas *(no universal, no superior…)* cierran los flancos | ✅ |
| A4 | Cap. 9: las 17 limitaciones tienen origen trazado en cierres anteriores; ninguna afirmación nueva sin base | ✅ |

## 7. Veredicto

> ### ✅ **NINGUNA CONTRADICCIÓN BLOQUEANTE. La Parte II puede redactarse.**
>
> Incidencias registradas: **2 🟠** *(X1 glosa de IDC en cap. 4 · A1 «error más común»)* y
> **5 🟡** cosméticas — todas en capítulos cerrados, ninguna corregida silenciosamente,
> todas resolubles en la pasada de maquetación final si se aprueba reabrir.



<!-- ══════════════════════════════════════════════════════════ -->

# ▓▓▓ B · AUDITORÍA PARTE II — CAPS. 10-14 ▓▓▓

---

# 🔍 AUDITORÍA CONJUNTA DE LA PARTE II — CAPÍTULOS 10 A 14

## 13 de agosto de 2026 · cierre del sprint 8-14

> **Regla aplicada:** ninguna incidencia corregida silenciosamente; X-Ray, pesos,
> vehículos, capítulos cerrados y decisiones Dxx intactos.

---

## 1. Consistencia interna de la Parte II

| Comprobación | Resultado |
|---|---|
| **Pesos idénticos en 10, 11 y 14** *(44 · 12 · 12 · 7 · 9 · 9 · 4 = 97 + Reserva 3)* | ✅ |
| **Convicción nunca como fila estructural** — solo etiqueta de gobernanza *(B3/D78)* | ✅ en los cinco capítulos |
| **PIMCO señalado como «vigente sujeto a revisión por coste»** en 11 y 14; la función del Freno independiente del vehículo | ✅ *(regla 9 del sprint)* |
| **Motor presentado como ancla + tilt, nunca como diversificación** | ✅ en 10, 11 y 14 |
| **Emergentes: 7% = decisión dedicada ≠ exposición total** | ✅ en 11 y 14, remitido al cap. 16 |
| **D77 respetada** *(proxy small caps con regla de atribución)* | ✅ en 11 y 14 |
| **«La política es permanente; el capital transitorio»** | ✅ en 13, coherente con 5 |
| **0% inicial / 14% techo; sin invitación a rellenar** | ✅ en 12 |
| **Etiquetas de fuente ✅/🟡/🔴 en todos los datos de producto** | ✅ — decisión honesta: **todo en 🟡** porque los KID no están; ningún dato inventado |
| **Versionado v1.0 y tabla estable/sustituible** | ✅ en 10 |
| **Cadena mandato→…→reglas visible** | ✅ — 10 la abre, cada capítulo declara su eslabón |

## 2. Incidencias registradas *(ninguna bloqueante)*

| # | Incidencia | Gravedad |
|---|---|---|
| P1 | **La clase de Emergentes** *(S, `IE000QAZP7L2`)* viene de catálogo; la confirmación contra documentación contractual está pendiente y así se marca en 11 y 14 — **no imprimir como definitiva hasta esa confirmación** | 🟠 |
| P2 | **La correlación 0,96 del caso calidad** *(cap. 14)* es medición propia del 12-ago sin ventana documentada; etiquetada 🟡 con re-verificación pendiente. Si la re-verificación falla, el cap. 14 rebaja la cifra a cualitativa | 🟡 |
| P3 | El coste **≈0,23% estimado** aparece en 14 remitido al cap. 22; coherente con el estado del proyecto *(estimado hasta fuentes primarias)* | 🟡 |
| P4 | Cap. 11 usa «primas documentadas por la investigación académica» con [EVIDENCIA EXTERNA] pendiente — correctamente etiquetado, pero **el cap. 11 no debe cerrarse sin esas citas** | 🟠 |
| P5 | La Fecha Cero de Convicción **no existe** *(cap. 12 lo declara)* — hueco estructural conocido, no de redacción | 🟠 *(ya en rúbrica)* |

## 3. Contraste con capítulos cerrados y decisiones

- Sin contradicción con caps. 4-9 *(terminología de capas y vistas, D78-D79)*. ✅
- Sin contradicción con D45-D61 *(protocolo)*, D73 *(Motor)*, D75-D77. ✅
- El tratamiento del PIMCO **no contradice D63/D68**: sigue siendo Freno + activa
  delegada; solo se añade el estado «en revisión por coste», que refleja la instrucción
  vigente del equipo. ✅

## 4. Veredicto

> ### ✅ **Parte II coherente y sin contradicciones bloqueantes. Lista para auditoría del director.**

---

# 📋 LISTA CONSOLIDADA DE DATOS Y FUENTES PENDIENTES *(caps. 8-14)*

## 🔴 Bloqueantes para cerrar capítulos

| # | Pendencia | Bloquea |
|---|---|---|
| 1 | **13 KID/documentos oficiales de los vehículos** *(coste, clase, réplica, política de distribución)* | Cap. 14 → ✅ · cap. 22 |
| 2 | **Revisión por coste del vehículo de renta fija del Freno** *(PIMCO vs alternativa indexada)* | Cierre definitivo de 11 y 14 |
| 3 | **Valoraciones con IDC de las candidatas** *(mínimo 3)* + **tabla Fecha Cero** | Cap. 12 cerrado de verdad · rúbrica dim. 6 |

## 🟠 Importantes

| # | Pendencia | Para |
|---|---|---|
| 4 | Citas formales: **SPIVA · Bessembinder · Fama-French · Asness · Kahneman/Montier · Bridgewater · Swensen · goals-based** | Caps. 4, 11 *(anexo E)* |
| 5 | **Browne, *Fail-Safe Investing*** — edición y página · **Swensen, *Unconventional Success*** — página | Cap. 8 *(cierre definitivo)* |
| 6 | **Dossier de evidencia macro del tilt EEUU** *(escala, productividad, I+D, mercados de capitales, beneficios, dólar — con fuentes primarias: FMI, OCDE, NSF, SIFMA, BEA)* | Cap. 11 · D73 |
| 7 | **Confirmación contractual de la clase de Emergentes** | Caps. 11, 14 |
| 8 | Episodios de caídas históricas de bitcoin **con fuente** | Cap. 11 |
| 9 | Frecuencias/retrasos de publicación de carteras y diferencias entre proveedores *(marcados [EVIDENCIA EXTERNA] en el cap. 6)* | Caps. 6*, 9 *(anexo)* |

## 🟡 Menores

| # | Pendencia | Para |
|---|---|---|
| 10 | Remuneración del efectivo operativo *(cifra con fuente)* | Caps. 13, 22 |
| 11 | Re-verificación formal de la correlación del caso calidad *(ventana, frecuencia)* | Cap. 14 |
| 12 | Glosas pendientes registradas en la auditoría de la Parte I *(IDC en cap. 4, «error más común»)* | Pasada de maquetación, si se aprueba reabrir |

*\*el cap. 6 está cerrado: su pendencia se documenta en anexo, no reabriendo el capítulo.*



<!-- ══════════════════════════════════════════════════════════ -->

# ▓▓▓ C · PENDIENTES EN TRES CATEGORÍAS ▓▓▓

---

## C.1 — FUENTES Y DOCUMENTOS PENDIENTES

*(Cosas que existen fuera del proyecto y hay que traer: documentos oficiales, papers,
páginas de libros. No exigen decidir nada ni calcular nada — solo localizar y citar.)*

| # | Pendencia | Prioridad | Afecta a |
|---|---|---|---|
| F1 | **13 KID/documentos oficiales de los vehículos** — coste, clase exacta, réplica, política de distribución | 🔴 | Caps. 11, 14, 22 · el coste ≈0,23% deja de ser «estimado» |
| F2 | **Browne, *Fail-Safe Investing*** — edición y página exacta de la composición 4×25 | 🟠 | Cap. 8 *(cierre definitivo)* |
| F3 | **Swensen, *Unconventional Success*** — página exacta de la cartera 30/15/5/20/15/15 y formulación de sus restricciones sobre renta fija | 🟠 | Caps. 8 y 11 |
| F4 | **Citas académicas formales**: SPIVA *(Persistence Scorecard)* · Bessembinder · Fama-French · Asness et al. · Kahneman / Montier · Bridgewater *(The All Weather Story)* · literatura goals-based | 🟠 | Caps. 4, 11 · anexo E |
| F5 | **Dossier de evidencia macro del tilt EEUU** con fuentes primarias *(FMI, OCDE, NSF, SIFMA, BEA, composición de reservas del FMI, desglose de ingresos del S&P 500)* | 🟠 | Cap. 11 · compromiso de D73 |
| F6 | **Confirmación contractual de la clase del vehículo de Emergentes** *(clase S `IE000QAZP7L2` contra documentación vigente)* | 🟠 | Caps. 11, 14 |
| F7 | **Episodios de caídas históricas de bitcoin** con fuente citable | 🟠 | Cap. 11 |
| F8 | **Frecuencias y retrasos de publicación de carteras** y **diferencias metodológicas entre proveedores** *(marcados [EVIDENCIA EXTERNA] en el cap. 6)* | 🟡 | Anexo del cap. 6 · cap. 9 |
| F9 | **Remuneración del efectivo operativo** *(cifra con fuente y fecha)* | 🟡 | Caps. 13, 22 |
| F10 | **CNMV — plazos de reembolso**, solo con vehículo y proceso concretos identificados | 🟡 | Cap. 14 *(nota del cap. 5)* |

## C.2 — DECISIONES PENDIENTES

*(Cosas que el equipo debe decidir. Ningún documento ni cálculo las sustituye.)*

| # | Decisión | Prioridad | Contexto |
|---|---|---|---|
| D-a | **Mantener o sustituir el PIMCO GIS Income** en el 3% del Freno, por coste *(1,45% 🟡)* | 🔴 | Revisión en curso declarada. Candidata natural identificada: renta fija global indexada de corto plazo *(pieza de referencia anterior)*. La función Freno no depende del resultado |
| D-b | **Resolver la tensión del mandato: ¿el año 10 es fecha de retirada o mínimo de permanencia?** *(riesgo del objetivo vs perfil; con o sin glidepath)* | 🔴 | Bloquea el cierre del cap. 3 y la coherencia de la dimensión 1 de la rúbrica |
| D-c | **Aprobar o revisar las 7 incidencias no-bloqueantes** de las auditorías I y II *(reabrir o no los caps. cerrados en la pasada de maquetación)* | 🟠 | Glosa de IDC en cap. 4 · «error más común» · deriva terminológica cosmética |
| D-d | **D47b — política de ventas por sobreponderación** *(las aportaciones no restan; falta la regla de venta)* | 🔴 | Bloquea el cap. 23 y cierra el hueco declarado en el cap. 13 |
| D-e | **Selección definitiva de las compañías candidatas de Convicción** *(cuáles entran al universo con los 7 documentos)* | 🟠 | Precede al trabajo analítico A-a |

## C.3 — TRABAJO ANALÍTICO PENDIENTE

*(Cosas que hay que calcular o construir dentro del proyecto.)*

| # | Trabajo | Prioridad | Afecta a |
|---|---|---|---|
| A-a | **Valoraciones completas con IDC de al menos 3 candidatas** + **tabla de la Fecha Cero** | 🔴 | Cap. 12 · dimensión 6 de la rúbrica *(hoy la nota más baja)* |
| A-b | **D47a — auditoría de los shocks del estrés** *(tres shocks heredados de bloques que cambiaron)* + **estrés por regímenes** *(1973-74 · 2000-02 · 2008-09 · 2022)* | 🔴 | Caps. 19-20 · el −43,45% sigue provisional |
| A-c | **Marco de cuatro cajas crecimiento × inflación** con datación histórica y cobertura por módulos | 🔴 | Cap. 19 · dimensión 11 de la rúbrica *(hoy 0/5)* |
| A-d | **D53 — escenarios de despliegue de Convicción** | 🟠 | Cap. 21 |
| A-e | **X-Ray bruto vs neto** *(coste + fiscalidad del rebalanceo + fricción)* | 🟠 | Cap. 22 · dimensión 12 de la rúbrica |
| A-f | **Cuantificación del riesgo de divisa** *(¿qué pasa con la rentabilidad en euros si el dólar cae?)* | 🟠 | Cap. 18 |
| A-g | **Correlaciones con ventana, frecuencia, fuente y fecha** *(las cifras remitidas por los caps. 4, 6, 11)* + exposición emergente total y EEUU total medidos | 🟠 | Caps. 16, 18 |
| A-h | **Re-verificación formal de la correlación del caso calidad** *(el 0,96 interno, sin ventana documentada)* | 🟡 | Cap. 14 |
| A-i | **Test de concordancia inter-analista** del árbol de clasificación *(extensión declarada)* | 🟡 | Caps. 7, 9 — mejora, no bloquea |
| A-j | **Sortino y métricas complementarias** para cartera agresiva | 🟡 | Cap. 17 |

---

# FIN DEL PACK

*Generado el 13-ago-2026 · archivos fuente en `05_TRABAJO_FINAL/` · nada modificado.*
