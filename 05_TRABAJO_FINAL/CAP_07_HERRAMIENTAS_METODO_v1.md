# CAPÍTULO 7 — LAS HERRAMIENTAS DEL MÉTODO: CLASIFICAR, REGISTRAR Y COMPROBAR

## Investment Book · Parte I · Borrador v1 para auditoría · 13 de agosto de 2026

> **Convención tipográfica:** **[MODELO]** = afirmación propia de PMMA.
> **[EVIDENCIA EXTERNA]** = afirmación que requiere cita o fuente primaria.
>
> **Objetivo del capítulo:** demostrar que PMMA transforma una clasificación intuitiva en
> un **procedimiento documentado, repetible y auditable**. Repetible significa que el
> mismo equipo, siguiendo los mismos pasos, deja el mismo rastro; **no** afirmamos que dos
> analistas independientes llegarán necesariamente a la misma clasificación — esa
> comparabilidad sigue siendo una limitación no testada *(§7.7)*.

---

## 7.1 De la intuición al procedimiento

Los capítulos 4 a 6 definieron el lenguaje: funciones, capas y modos de análisis. Un
lenguaje, por sí solo, no impide clasificar mal, olvidar por qué se compró algo o
justificar cualquier posición a posteriori. Para eso hacen falta herramientas — cosas que
se usan, que dejan rastro y que otro puede revisar.

**[MODELO]** PMMA tiene cuatro, y este capítulo enseña **cómo se usan**, no qué son
*(las definiciones están en el capítulo 4 y no se repiten)*:

| Herramienta | Qué hace | Cuándo se usa |
|---|---|---|
| **El árbol de clasificación** | Asigna cada posición a su módulo mediante ocho preguntas en orden fijo | Cada vez que entra una posición nueva |
| **El protocolo para excepciones** *(nombre formal: Protocolo de Extensión)* | Da salida honesta a lo que no encaja | Cuando el árbol termina sin respuesta clara |
| **El modelo de datos** *(35 campos)* | Registra cada posición con todo lo necesario para auditarla después | Siempre — es la ficha de cada posición |
| **El control final de aceptación** *(en inglés, Gate)* | Somete la cartera completa a diez preguntas antes de darla por aceptada | Al cerrar la construcción y en revisiones mayores |

La secuencia natural es la del título: **clasificar** *(árbol y excepciones)*,
**registrar** *(modelo de datos)* y **comprobar** *(control final)*. Lo que sigue es cada
herramienta trabajando sobre casos reales de este proyecto.

---

## 7.2 El árbol en uso: tres clasificaciones reales

El árbol *(capítulo 4, §4.9)* hace ocho preguntas en orden fijo, todas sobre la **función**
de la posición, nunca sobre su mera clase de activo. Verlo funcionar con posiciones reales
enseña más que cualquier definición.

**Caso 1 — El fondo de renta fija flexible del Freno.** Un fondo de renta fija de gestión
activa, con mandato amplio *(puede moverse entre tipos de deuda, plazos y niveles de
riesgo)*. La tentación es clasificarlo automáticamente «porque es renta fija». El árbol no
lo permite: la pregunta 2 no dice *«¿es renta fija?»* sino *«¿su función dominante es
estabilizar la cartera o responder a escenarios distintos de los activos productivos?»*.
La respuesta exige mirar la **tesis**: este fondo se incorporó para dar al Freno una
fuente de renta y comportamiento distinta del monetario, dentro de la función
estabilizadora del módulo. Respuesta: sí → **Freno**, con forma de gestión *activa
delegada* y una anotación en la ficha: su mandato es más amplio que el del vehículo al
que sustituyó, y esa amplitud es un riesgo que se vigila *(capítulo 11)*.

**Caso 2 — La calidad, el caso ambiguo por excelencia.** Un fondo de empresas de
«calidad» *(beneficios estables, poca deuda)* puede comprarse por dos razones distintas:
por resiliencia *(pregunta 5: Defensivos)* o como fuente de rentabilidad extra
*(pregunta 6: Aceleración)*. El árbol resuelve el empate por orden —la pregunta defensiva
llega antes— pero la respuesta depende de **por qué** se compró, y eso solo lo sabe la
tesis registrada. En este proyecto el caso no es teórico: un fondo de calidad global se
probó y se descartó al comprobarse, mirando dentro, que su comportamiento apenas se
distinguía del núcleo de la cartera *(el análisis, con sus cifras y fuente, en el
capítulo 14)*. La clasificación habría sido posible; la posición, redundante. **Clasificar
bien no sustituye a preguntarse si la posición aporta algo.**

**Caso 3 — El cobre.** Un producto cotizado sobre futuros de cobre. Pregunta 3: *¿su
función dominante es aportar un comportamiento ligado a activos reales o a la inflación,
distinto de acciones y bonos?* Sí → **Activos Reales**. Pero la ficha registra un matiz
que la etiqueta no cuenta: el vehículo no posee cobre físico, sino contratos de futuros
con estructura de deuda — un funcionamiento distinto del oro físico del mismo módulo.
Mismo módulo, distinta mecánica interna: **el árbol asigna la función; la ficha conserva
la letra pequeña.**

Los tres casos comparten el patrón: **el árbol no ahorra el juicio — lo ordena y lo deja
escrito.** La pregunta correcta queda registrada junto a la respuesta, y cualquiera puede
revisar después si la respuesta sigue siendo válida.

---

## 7.3 El protocolo para excepciones

¿Qué pasa cuando el árbol termina y ninguna pregunta ha capturado la función de un
instrumento con honestidad? Gestión alternativa, capital privado, estrategias de
volatilidad, productos estructurados: cosas cuya función dominante no es clara ni forzada.

**[MODELO]** La regla del método es contracultural en un sector que lo etiqueta todo:

> **Es preferible reconocer una excepción que falsear la arquitectura.**

La posición se clasifica temporalmente como **Extensión / Estrategia Alternativa** y queda
en un estado explícito de «pendiente de función»: o su tesis madura hasta justificar un
módulo, o se concluye que no pertenece a la cartera. Lo que nunca ocurre es el encaje a
martillazos — un producto complejo disfrazado de Freno porque «lleva bonos», o de
Asimetría porque «puede subir mucho».

En la implementación actual el protocolo no ha hecho falta: las trece posiciones tienen
función dominante clara. Ese dato también informa — la cartera se construyó con
instrumentos simples a propósito, y la puerta de las excepciones está para el futuro, no
para maquillar el presente. Si algún día entra un instrumento de los listados arriba, su
camino está escrito de antemano.

---

## 7.4 El modelo de datos: la ficha de cada posición

**[MODELO]** Cada posición se registra con una ficha de **35 campos**: los 26 del modelo
original *(identificación, pesos, módulo, marcas de capa, benchmark, exposiciones, coste,
riesgo, tesis y regla de revisión)* más **nueve añadidos durante la propia construcción**.
Esos nueve no salieron de un manual: **cada uno existe porque su ausencia causó un
problema real en este proyecto.** Los seis principales:

| Campo añadido | El caso que lo exigió |
|---|---|
| **ISIN** | El mismo producto cotiza en varias bolsas con distintos códigos de pizarra. En este proyecto, más de un vehículo aparece en dos o tres mercados: solo el ISIN identifica sin ambigüedad **qué** se posee |
| **Clase de participación** | Dos posiciones de la cartera se contrataron en una clase que las herramientas de análisis no reconocían; el análisis se hizo con otra clase del **mismo fondo**. Misma cartera interna, distinto coste. Sin este campo, la diferencia se vuelve invisible y el coste publicado sale mal |
| **Proxy analítico** *(sí/no y cuál)* | El bloque de pequeñas compañías se analiza con un producto sustituto del mismo índice *(decisión D77)*. El campo registra que hay proxy y cuál es — sin él, la regla *«del proxy solo se toma aquello para lo que es realmente equivalente»* no se puede aplicar ni auditar |
| **Cobertura de divisa** | El cobre analizado estaba cubierto a euro; el contratado, no. Es la única discrepancia del análisis que **cambia el comportamiento** del activo, y se detectó precisamente comparando este campo |
| **Fuente y fecha del dato** | El coste de un fondo del Freno procede de una plataforma de análisis y está pendiente de confirmarse en su documento oficial. El campo distingue «verificado en documento del fondo» de «tomado de plataforma» — sin esa distinción, todos los datos parecen igual de firmes y no lo son |
| **Confianza de clasificación** *(alta / media / ambigua)* | El caso de la calidad *(§7.2)*: cuando una posición admite dos módulos razonables, este campo lo declara y exige justificación y segunda revisión. **Convierte la subjetividad en un dato auditable** en lugar de esconderla |

Los otros tres — acumulación o reparto, atributos fiscales del vehículo *(cuya
documentación formal corresponde al capítulo 22)* y contribución al riesgo — completan la
ficha; el modelo íntegro figura en el anexo H.

La lección de fondo: **un modelo de datos no se diseña en abstracto — se gana a base de
errores encontrados.** Cuatro de los nueve campos existen porque el análisis de esta misma
cartera falló sin ellos.

---

## 7.5 El control final de aceptación

**[MODELO]** Ninguna cartera se da por aceptada por acumulación de entusiasmo. Antes de
cerrarse, pasa un **control final de aceptación**: diez preguntas, cada una respondida
**con evidencia, no con adjetivos** — un documento, una cifra con fuente, una regla
escrita. Las diez preguntas están definidas en el capítulo 4 *(§4.12)*; aquí importa cómo
se usan:

- **Cada respuesta señala su evidencia.** «¿Existen reglas de aportación y rebalanceo?» no
  se responde «sí»: se responde «sí — protocolo operativo, secciones tal y tal», con el
  documento delante.
- **Una pregunta puede suspender, y decirlo es parte del método.** Si la respuesta honesta
  a «¿conocemos el riesgo?» es «parcialmente — el análisis de escenarios extremos sigue
  pendiente», eso se escribe. Una cartera con un suspenso declarado y su plan de cierre es
  más sólida que una con diez aprobados retóricos.
- **El control se repite.** No es un trámite de inauguración: cada revisión mayor vuelve a
  pasarlo, porque las respuestas caducan — los datos envejecen, los vehículos cambian, las
  reglas se completan.

La implementación de este trabajo pasa explícitamente por el control en el **capítulo 26**,
con la evidencia acumulada en las Partes III a V — incluidas las preguntas cuya respuesta
honesta, a fecha de hoy, es incompleta.

⚠️ Y la advertencia que evita idolatrar la herramienta: **el control final examina el
proceso, no adivina el futuro.** Una cartera puede responder las diez preguntas con
evidencia impecable y aun así obtener malos resultados — el control garantiza que se sabe
lo que se tiene y por qué, no que vaya a ganar dinero.

---

## 7.6 Cómo encajan las cuatro herramientas

Las cuatro forman un circuito, y el registro de decisiones lo cose todo:

```
posición nueva
     │
     ▼
ÁRBOL DE CLASIFICACIÓN  ──sin función clara──►  PROTOCOLO PARA EXCEPCIONES
     │                                                │
     ▼                                                ▼
MODELO DE DATOS  ◄────────────────────  (estado: Extensión, pendiente)
  (ficha de 35 campos: módulo, tesis,
   confianza, fuente y fecha…)
     │
     ▼
CONTROL FINAL DE ACEPTACIÓN
  (10 preguntas con evidencia, sobre la cartera completa)
     │
     ▼
REGISTRO DE DECISIONES
  (cada paso, fechado y con motivo)
```

**[MODELO]** El resultado es la propiedad que da título al capítulo: cualquier tercero
puede tomar una posición cualquiera y reconstruir su historia — con qué pregunta se
clasificó, con qué confianza, qué dice su tesis, de dónde salió cada dato y cuándo, y qué
respondió la cartera entera en su último control. Eso es lo que significa **auditable**: no
que las decisiones sean infalibles, sino que **están todas a la vista con su rastro**.

---

## 7.7 Limitaciones

Las herramientas mejoran el proceso; no lo vuelven infalible. Cuatro límites reales:

1. **El árbol reduce la subjetividad, no la elimina.** Las preguntas ordenan el juicio,
   pero el juicio sigue siendo humano: la función dominante la decide quien responde. Y la
   comparabilidad entre analistas independientes —¿clasificarían igual dos personas que no
   se conocen?— **no ha sido testada** y queda declarada como extensión futura.
2. **Treinta y cinco campos aumentan el control… y la carga de mantenimiento.** Cada campo
   es algo que puede quedarse desactualizado. Una ficha incompleta o vieja da apariencia
   de rigor sin su sustancia — el coste de mantener el sistema es real y permanente.
3. **El control final no garantiza resultados.** Examina si la cartera está bien
   construida y documentada; el mercado no lee nuestros documentos. Proceso impecable y
   mal resultado pueden convivir — y el método debe juzgarse por lo primero sin usar lo
   primero para excusar eternamente lo segundo.
4. **Una clasificación bien documentada puede seguir siendo una decisión equivocada.**
   Documentar no es acertar: el registro perfecto de una mala tesis produce una mala
   inversión perfectamente trazable. El valor del rastro no es evitar el error, sino
   poder encontrarlo, entenderlo y no repetirlo.

---

## 7.8 Síntesis

> **Clasificar con preguntas ordenadas. Reconocer lo que no encaja en lugar de forzarlo.
> Registrar cada posición con todo lo necesario para auditarla. Y someter la cartera
> entera a un examen con evidencia antes de darla por buena. Ninguna de estas herramientas
> acierta por nosotros — pero todas juntas hacen imposible equivocarse sin dejar rastro.**

El capítulo 8 somete el lenguaje del método a la prueba de describir ocho carteras ajenas;
el capítulo 9 reúne todas las limitaciones del marco; y la Parte II muestra las
herramientas aplicadas posición a posición en *Peaky Minders Global 10Y*.

---

## CIERRE DEL CAPÍTULO — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes | Remisiones |
|---|---|---|---|---|---|
| D75 *(arquitectura modular y modelo de datos)* · D77 *(proxy y regla de atribución — origen del campo proxy)* · D78-D79 *(campo de confianza de clasificación; formas de gestión usadas en los casos del árbol)* · D68 *(el fondo flexible del Freno y su mandato amplio)* | Los tres casos del árbol proceden del registro del proyecto: fondo flexible del Freno *(D68, D67-④)* · calidad probada y descartada *(X-Ray histórico del proyecto; cifras en el cap. 14)* · cobre y su mecánica de futuros *(fichas del proyecto)* · los seis campos añadidos con su caso real cada uno *(auditoría A.4)* | El árbol reduce, no elimina, la subjetividad · comparabilidad inter-analista **no testada** · carga de mantenimiento de 35 campos · el control final no garantiza resultados · documentar ≠ acertar *(§7.7)* | ① El circuito de las cuatro herramientas *(§7.6)* ② El árbol con los tres casos reales recorridos ③ La ficha de 35 campos con los 9 añadidos destacados ④ Tablero del control final *(10 preguntas · evidencia · estado)* | 🟡 Cifras del caso calidad *(correlación con el núcleo, con fuente y fecha)* — cap. 14 · 🟡 Documentación fiscal comparada de vehículos *(campo fiscal de la ficha)* — cap. 22 | **Cap. 8** *(validación sobre carteras ajenas)* · **Cap. 9** *(limitaciones reunidas)* · **Cap. 11** *(la vigilancia del mandato amplio del fondo flexible)* · **Cap. 14** *(vehículos y el caso calidad con cifras)* · **Cap. 26** *(el control final aplicado a Global 10Y)* · **Anexo H** *(modelo de datos íntegro)* |

### Prueba anti-redundancia — respecto al capítulo 4

| Contenido compartido con el cap. 4 | Tratamiento en el cap. 7 |
|---|---|
| Las ocho preguntas del árbol *(§4.9)* | **No se reproducen**: se recorren con tres posiciones reales, mostrando cómo la tesis decide los casos ambiguos |
| El Protocolo de Extensión *(§4.10)* | La regla se cita en una línea; lo nuevo es su **uso** — incluido el dato de que aún no ha hecho falta y por qué eso también informa |
| El modelo de datos y los 9 campos *(§4.11)* | El cap. 4 los lista; el cap. 7 cuenta **el caso real que exigió cada campo** |
| Las diez preguntas del control final *(§4.12)* | **No se repiten**: se explica cómo se responde con evidencia, que puede suspenderse honestamente y que se repite en el tiempo |

**Confirmación:** ninguna definición del capítulo 4 se reproduce íntegra; el capítulo
enseña el uso de las herramientas con casos del propio proyecto.

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Borrador v1 completo del capítulo 7** — 8 secciones. Título en llano *(«las herramientas del método»)*; Gate → control final de aceptación; Protocolo de Extensión citado una vez como nombre formal. Tres casos reales del árbol *(fondo flexible del Freno, calidad, cobre)*, seis campos del modelo de datos con el problema real que los originó, y las cuatro limitaciones exigidas — incluida la comparabilidad inter-analista como no testada. **Ninguna cifra exacta publicada**; las del caso calidad remitidas al cap. 14. Pendiente de auditoría |
