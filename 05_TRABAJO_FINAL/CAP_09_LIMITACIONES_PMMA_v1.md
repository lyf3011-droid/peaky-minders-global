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
