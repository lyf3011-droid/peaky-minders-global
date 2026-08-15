# 🧪 PMMA UNIVERSAL — PROTOCOLO DE FALSACIÓN PREESPECIFICADO

## FASE 0 · Congelado el 15 de agosto de 2026 · **antes de examinar ninguna cartera externa**

> ## 🔒 **Este documento se fija ANTES de mirar resultados.**
> Ninguna regla, criterio, umbral ni predicción de este protocolo se ha escrito conociendo
> el resultado del estudio. **Toda regla añadida después llevará la etiqueta
> `POST HOC / surgida durante auditoría`**, como se hizo con C8 en el capítulo 19.
>
> **Nada ejecutado:** ni análisis de carteras externas, ni comparación, ni backtest, ni
> X-Rays, ni modificación de PMMA. **Cap. 4, cap. 19, cartera oficial y laboratorio X-Ray
> permanecen intactos.**

---

# 1. PREGUNTA PRINCIPAL

> ## **¿Puede PMMA representar de forma parsimoniosa y auditable las funciones económicas
> ## principales presentes en arquitecturas de cartera materialmente distintas, sin
> ## necesitar crear categorías *ad hoc* para cada una?**

## 1.1 Preguntas secundarias

| # | Pregunta | Qué la responde |
|---|---|---|
| **Q1** | ¿Los siete módulos representan funciones **realmente distintas**? | Matriz de solapamiento funcional *(§7.2)* |
| **Q2** | ¿Hay **dos módulos tan parecidos** que deberían fusionarse? | F2 + matriz de solapamiento |
| **Q3** | ¿Existe alguna **función importante** en otras arquitecturas que PMMA **no** pueda representar? | F3 + registro de funciones huérfanas |
| **Q4** | ¿Hay exposiciones que **no puedan clasificarse** por función dominante? | F1 + Red Team |
| **Q5** | ¿Las fronteras dependen **excesivamente del juicio del analista**? | F4 + prueba de reproducibilidad *(§9)* |
| **Q6** | ¿PMMA permite **comparar** carteras de filosofías muy distintas? | C8 + fichas comparadas |
| **Q7** | ¿Sigue siendo útil aunque **varios módulos tengan peso 0%**? | C10 + C11 |
| **Q8** | ¿Funciona **sin exigir** que cada módulo tenga un régimen macro favorable? | §11 — **ya resuelto por el cap. 19** |

## 1.2 Hipótesis inicial *(explícitamente falsable)*

> **[HIPÓTESIS]** Los siete módulos actuales —**Motor, Defensivos, Aceleración, Emergentes,
> Freno, Activos Reales, Asimetría**— constituyen una taxonomía funcional suficientemente
> **general, distinta y útil** para representar arquitecturas de cartera materialmente
> diferentes de *Peaky Minders Global 10Y*.

**Los siete módulos son la hipótesis inicial, NO el resultado.** Convicción y Reserva
Operativa son **capas transversales** y **no se convertirán automáticamente en módulos**.

**Resultados permitidos:** mantener 7 · reducir a 6 · aumentar a 8 · fusionar · dividir ·
redefinir fronteras · concluir que alguna categoría depende demasiado del mandato · concluir
que **PMMA no generaliza**.

**Prohibido:** partir de que los siete módulos son universales.

---

# 2. PRINCIPIO QUE SE PRESERVA

> ## **FUNCIÓN ANTES QUE PRODUCTO**

**No se clasifica por el nombre del activo.** Un REIT no pertenece automáticamente a Activos
Reales · *quality* no pertenece automáticamente a Defensivos · los TIPS no pertenecen
automáticamente a Activos Reales · el oro no define por sí mismo un módulo · una acción no
pertenece automáticamente a Motor.

**La clasificación depende de qué función justifica que esa exposición exista dentro de esa
cartera concreta.** El mismo instrumento puede cumplir funciones distintas bajo mandatos
distintos — **y eso es una propiedad del método, no un defecto**.

⚠️ **Consecuencia incómoda que se acepta desde ahora:** si la función depende del mandato,
**una misma exposición puede clasificarse distinto en dos carteras**, y eso **no** es una
inconsistencia. Lo que sí sería un fallo es que **dentro de la misma cartera** dos analistas
razonables la clasificaran distinto *(F4)*.

---

# 3. LAS DOS PREGUNTAS QUE NO SE MEZCLAN

| | Pregunta | Objeto de este estudio |
|---|---|---|
| **A · TAXONOMÍA** | ¿PMMA clasifica de forma útil las funciones de una cartera? | ✅ **SÍ** |
| **B · RENDIMIENTO** | ¿Las exposiciones utilizadas tienen evidencia histórica favorable? | ❌ **NO** |

> **La primera no depende de la segunda.** Una taxonomía puede describir correctamente una
> función **aunque la implementación concreta haya tenido mala rentabilidad**.

**Regla operativa:** **está prohibido usar rentabilidad, Sharpe, alfa o cualquier métrica de
resultado como argumento a favor o en contra de la existencia de un módulo.** Si aparece ese
razonamiento durante la ejecución, se marca como violación del protocolo.

---

# 4. CRITERIOS DE EXISTENCIA DE UN MÓDULO — **C1 a C12**

**Un módulo debe cumplir C1-C6 de forma necesaria.** C7-C12 son criterios de calidad y
parsimonia que se evalúan en conjunto.

| # | Criterio | Qué exige | Cómo se comprueba |
|---|---|---|---|
| **C1** | **Función económica diferenciable** | Debe poder explicarse **qué trabajo hace el capital**, en una frase, sin nombrar productos | Redacción de la función sin mencionar ningún vehículo |
| **C2** | **No redundancia** | No debe ser otra forma de expresar una función ya existente | Matriz de solapamiento funcional *(§7.2)* |
| **C3** | **Generalización** | Debe aparecer o tener sentido en **más de una arquitectura** | Recuento sobre la muestra de carteras |
| **C4** | **Independencia de producto** | Debe poder implementarse con **≥2 vehículos distintos** de naturaleza diferente | Enumeración de implementaciones alternativas |
| **C5** | **Gobernabilidad** | Debe permitir definir reglas de inclusión, peso, riesgo y revisión | ¿Puede escribirse una regla operativa no trivial? |
| **C6** | **Falsabilidad** | Debe existir **alguna observación capaz de cuestionar su necesidad** | Se exige redactarla explícitamente por módulo |
| **C7** | **Parsimonia de creación** | Crear un módulo debe aportar **más claridad de la que cuesta** en complejidad | Comparación con la taxonomía simple de referencia *(§6.2)* |
| **C8** | **Utilidad comparativa** | Debe ayudar a **comparar carteras distintas** | ¿Distingue arquitecturas que de otro modo se verían iguales? |
| **C9** | **Función dominante identificable** | Un **tercero razonable** debe poder comprender por qué una posición se asignó allí | Prueba de reproducibilidad *(§9)* |
| **C10** | **Peso cero permitido** | Una arquitectura **no necesita usar todos los módulos** para ser representable | Recuento de módulos a 0% por cartera |
| **C11** 🆕 | **Parsimonia de conservación** *(simétrica a C7)* | **Mantener** un módulo también debe justificar su coste. Un módulo que **nunca se usa en toda la muestra** y **cuya función queda cubierta por otro sin pérdida de información** es candidato a **eliminación o fusión** | Ver §4.1 |
| **C12** 🆕 | **Estabilidad de frontera** | La frontera con los módulos vecinos debe poder enunciarse **sin apelar a casos concretos** | Redacción de la frontera en abstracto |

## 4.1 ⚠️ Por qué existen C11 y C12 — **corrección de un sesgo del propio protocolo**

**C7 (parsimonia) solo se aplicaba a la creación de módulos nuevos.** Tal como estaba,
**protegía a los siete módulos actuales**: cualquier módulo propuesto tenía que justificarse,
pero **ninguno existente tenía que justificar su permanencia**. Eso es exactamente el sesgo
que este protocolo debe evitar.

> ### **C11 aplica la parsimonia en las dos direcciones.** La pregunta *«¿merece existir este
> ### módulo nuevo?»* y la pregunta *«¿merece seguir existiendo este módulo actual?»* se
> ### responden con el mismo listón.

**C10 y C11 no se contradicen:** C10 dice que **una cartera concreta** puede no usar un
módulo sin que eso invalide la representación. C11 dice que **si ningún caso de toda la
muestra lo usa y su función es absorbible**, el módulo sobra. **C10 protege la
representabilidad; no protege al módulo.**

---

# 5. CRITERIOS DE FALLO — **F1 a F9, con umbrales fijados ex ante**

> ⚠️ **Sin umbral, un criterio de fallo no es falsable.** «Numerosos activos» o «módulos
> parecidos» son inauditables. Por eso cada F lleva **su umbral escrito antes de mirar**.

| # | Fallo | Umbral preespecificado | Consecuencia si se cumple |
|---|---|---|---|
| **F1** | **Activos no clasificables sin excepción** | **> 15%** de las exposiciones del universo requieren excepción, Protocolo de Extensión o categoría *ad hoc* | 🔴 Cuestiona la cobertura del método |
| **F2** | **Dos módulos funcionalmente indistinguibles** | En **≥3 de las carteras** de la muestra, dos módulos reciben asignaciones que **un analista razonable podría intercambiar** sin cambiar la lectura | 🟠 Obliga a evaluar fusión |
| **F3** | **Función recurrente sin módulo** | Una función aparece en **≥3 carteras** de la muestra y **no encaja** en ninguno de los siete | 🔴 Obliga a evaluar módulo nuevo |
| **F4** | **Clasificación irreproducible** | **> 20%** de las asignaciones difieren en la prueba de reproducibilidad *(§9)* | 🔴 Cuestiona C9 y la auditabilidad |
| **F5** | **Redefinición constante** | Se necesita **modificar una definición de módulo más de 2 veces** durante el estudio para acomodar carteras | 🔴 El método se está ajustando a los datos |
| **F6** | **Los módulos describen productos, no funciones** | **≥2 módulos** solo pueden definirse enumerando los productos que contienen | 🔴 Contradice el principio central |
| **F7** | **Solo funciona para Global 10Y** | **≥3 carteras** de la muestra requieren «encaje con tensión» o «no encaja» | 🔴 No generaliza |
| **F8** | **No supera a una taxonomía más simple** | La **taxonomía simple de referencia** *(§6.2)* clasifica la muestra **con igual utilidad comparativa y menos categorías** | 🔴 La complejidad no se paga |
| **F9** 🆕 | **Módulo inutilizado y absorbible** | Un módulo queda a **0% en todas las carteras** de la muestra **y** su función es absorbible por otro sin pérdida de información | 🟠 Candidato a eliminación *(C11)* |

## 5.1 Qué NO cuenta como fallo

- **Que un módulo tenga peso 0% en algunas carteras** *(C10)*.
- **Que una misma exposición se clasifique distinto en carteras con mandatos distintos**
  *(§2)*.
- **Que un módulo no tenga un régimen macro favorable propio** *(§11 — resuelto por el
  cap. 19)*.
- **Que la implementación concreta de una función haya rendido mal** *(§3, pregunta B)*.

---

# 6. LA COMPARACIÓN OBLIGATORIA CONTRA ALTERNATIVAS MÁS SIMPLES

**F8 no es auditable sin definir contra qué se compara. Se fija ahora, antes de mirar.**

## 6.1 Por qué es imprescindible

El criterio de falsación del propio capítulo 4 exige que PMMA **mejore materialmente frente a
una clasificación convencional más sencilla**. Sin una alternativa concreta, esa exigencia es
retórica.

## 6.2 Las tres taxonomías de referencia — **congeladas**

| # | Taxonomía | Categorías | Por qué se elige |
|---|---|---|---|
| **T0 · Clases de activo** | Renta variable · Renta fija · Alternativos · Liquidez | **4** | Es el estándar de la industria. Si PMMA no bate esto, no aporta nada |
| **T1 · Funcional mínima** | Crecimiento · Estabilidad · Protección real · Opcionalidad | **4** | Es **la versión más sencilla del propio principio funcional**. Es el rival más duro |
| **T2 · PMMA** | Los siete módulos + 2 capas transversales | **7 + 2** | La hipótesis |

**Regla:** las tres taxonomías se aplican **a la misma muestra, con la misma plantilla y en
el mismo orden**, y se comparan con las métricas del §13. **T1 es el competidor real**, no T0.

⚠️ **Si T1 clasifica igual de bien con cuatro categorías, PMMA falla F8** — aunque cada
módulo cumpla C1-C6 por separado.

---

# 7. UNIVERSO DE EXPOSICIONES A TESTAR *(no se analiza todavía)*

## 7.1 Lista congelada — 26 exposiciones

**Renta variable:** global · EEUU · desarrollada ex-EEUU · emergentes · small caps · value ·
quality · momentum · low volatility · growth · sectores defensivos · un país concreto.
**Renta fija:** soberana · agregada · larga duración · corta duración · crédito grado de
inversión · high yield · ligada a inflación (TIPS) · monetario/cash.
**Reales y alternativos:** oro · cesta amplia de materias primas · inmobiliario/REIT ·
infraestructura · *managed futures* / *trend following* · private equity.
**Asimétricos:** bitcoin/cripto.

> **No se asume que ninguna necesite módulo propio.** La pregunta es la contraria:
> **¿qué función realiza?**

## 7.2 Matriz de solapamiento funcional — instrumento para Q1, Q2 y C2

Para cada par de módulos se registrará: **¿existe alguna exposición del universo que un
analista razonable pudiera asignar a cualquiera de los dos?** El resultado es una matriz
7×7 de **ambigüedad estructural**, no de correlación.

**Predicción registrada:** ver §16.

---

# 8. MUESTRA DE CARTERAS EXTERNAS *(no se analiza todavía)*

## 8.1 Principio de selección: **maximizar la tensión, no la comodidad**

⚠️ **Una muestra formada solo por carteras multiactivo estratégicas haría que PMMA encajara
trivialmente.** Por eso la muestra incluye deliberadamente **arquitecturas para las que PMMA
no fue diseñado**.

| # | Arquitectura | Por qué está en la muestra | Tensión esperada |
|---|---|---|---|
| **A** | **60/40 tradicional** | El caso más simple y más extendido | ¿PMMA aporta algo o es sobreingeniería? |
| **B** | **Permanent Portfolio** *(Browne)* | Cuatro bloques por escenario económico | 🔴 **Su lógica es de régimen, no funcional** |
| **C** | **All Weather / risk parity** | Asignación por contribución al riesgo | 🔴 **El peso no es la unidad de decisión** |
| **D** | **Golden Butterfly** | Variante con sesgo a small value | Frontera Motor/Aceleración |
| **E** | **Cartera global indexada de un solo fondo** | Un único vehículo | 🔴 **¿Se puede clasificar una cartera con una sola posición?** |
| **F** | **Cartera factorial multi-factor** | Value, momentum, quality, low vol | 🔴 **¿Todos los factores caben en Aceleración?** |
| **G** | **Modelo Endowment** *(estilo Swensen)* | Alternativos ilíquidos, private markets | 🔴 **Private equity, absolute return** |
| **H** | **Cartera de rentas / income** | Objetivo de flujo, no de crecimiento | 🔴 **El mandato es distinto: ¿PMMA lo cubre?** |
| **I** | **Trend following / managed futures puro** | Estrategia, no clase de activo | 🔴 **La función es dinámica, no estructural** |
| **J** | **Peaky Minders Global 10Y** | El caso de origen | Control: **debe encajar** — si no, hay un problema grave |

**Diez arquitecturas, de las cuales seis están elegidas por su capacidad de romper PMMA.**

## 8.2 Reglas de fuente para la Fase 1

1. **Fuentes primarias siempre que existan**: documento del creador, libro original,
   documentación institucional del gestor.
2. **Si una cartera tiene varias versiones, se declara cuál se usa y por qué.**
3. **No se fijan composiciones de memoria.** Ninguna cartera entra en el estudio sin fuente
   citada con autor, obra y año.
4. **Los blogs no son fuente principal.**
5. **Prohibido usar resultados del laboratorio X-Ray como validación universal** — es un
   entorno experimental congelado y no propagado *(D107)*.

---

# 9. PLANTILLA ÚNICA DE ANÁLISIS — **congelada**

**Se aplica idéntica a las diez arquitecturas y a las tres taxonomías. No se adapta después
de cada cartera.**

| Campo | Contenido |
|---|---|
| **Mandato** | Qué intenta conseguir |
| **Horizonte** | Largo / corto / indefinido |
| **Filosofía** | Qué lógica utiliza |
| **Fuente** | Autor, obra, año, versión declarada |
| **Exposiciones** | Qué contiene realmente |
| **Función de cada exposición** | Para qué está **en esa cartera** |
| **Módulo PMMA candidato** | Clasificación inicial |
| **Ambigüedad** | Baja / media / alta |
| **Alternativa posible** | Otro módulo razonable, si lo hay |
| **Función sin representación** | Si existe |
| **Módulo no utilizado** | Si existe |
| **Resultado** | ✅ Encaja · ⚠️ Encaja con tensión · ❌ No encaja |

## 9.1 Prueba de reproducibilidad — **para Q5 y F4**

**El problema:** la limitación **L1** del capítulo 4 —subjetividad inter-analista **no
testada**— sigue abierta. Un protocolo que pregunte Q5 sin poder responderla es débil.

**Diseño factible, con su limitación declarada:**

| Nivel | Prueba | Viabilidad |
|---|---|---|
| **Ideal** | Dos analistas independientes clasifican a ciegas las mismas 30 exposiciones | ⚠️ **Requiere una segunda persona.** Si el equipo puede aportarla, es el test correcto |
| **Mínimo viable** | **Clasificación a ciegas diferida**: las 30 exposiciones se clasifican **dos veces con ≥48h de separación**, sin consultar la primera tanda, y se mide la coincidencia | ✅ Ejecutable |
| **Complementario** | **Test del tercero**: por cada asignación se redacta la justificación **sin nombrar el producto**; si la justificación no permite reconstruir el módulo, cuenta como ambigua | ✅ Ejecutable |

> ⚠️ **Limitación declarada:** la prueba mínima mide **consistencia intra-analista**, no
> inter-analista. **No cierra L1.** Se declarará así en el resultado, sin presentarla como si
> lo hiciera.

---

# 10. RED TEAM PMMA — **fase obligatoria**

**Su trabajo es buscar deliberadamente casos que hagan incómodo a PMMA.** No se esconde
ninguno.

## 10.1 Casos duros preidentificados

| # | Caso | Por qué es duro |
|---|---|---|
| **R1** | **TIPS** | ¿Freno *(estabilidad nominal)* o Activos Reales *(protección real)*? **El propio cap. 4 lo declara «default revisable»** |
| **R2** | **REIT** | Motor si está dentro de un índice global; Activos Reales si es asignación específica. **Depende del mandato** |
| **R3** | **Quality** | Defensivos por resiliencia o Aceleración por prima. **El cap. 4 lo usa como ejemplo del orden del árbol** |
| **R4** | **Trend following / managed futures** | 🔴 **Función dinámica, no estructural.** ¿Es Asimetría, Freno o **una función que PMMA no tiene**? |
| **R5** | **High yield** | Renta fija con comportamiento de renta variable. **El cap. 4 ya lo manda al Protocolo de Extensión** |
| **R6** | **Private equity** | ¿Motor ilíquido, o una función distinta *(prima de iliquidez)*? |
| **R7** | **Infraestructura** | Entre Activos Reales, Defensivos y Motor |
| **R8** | **Opciones / estrategias de cobertura** | Función de seguro sin exposición direccional |
| **R9** | **Un fondo mixto o un multiactivo delegado** | Contiene **varias funciones en un solo vehículo** |
| **R10** | **Cash: Freno o Reserva** | **La distinción es de mandato, no de instrumento.** Riesgo de circularidad |
| **R11** | **Bitcoin** | ¿Asimetría, Activos Reales *(reserva de valor)* o especulación sin módulo? |
| **R12** | **Renta variable de un solo país** *(caso India del laboratorio)* | ¿Aceleración, Emergentes o Motor con sesgo? **Ya generó desacuerdo real** |

## 10.2 Regla del Red Team

**Un caso resuelto invocando el Protocolo de Extensión cuenta como excepción para F1.** El
Protocolo de Extensión es una válvula honesta, **pero cada uso es evidencia de cobertura
incompleta y se contabiliza como tal.**

---

# 11. RELACIÓN CON LOS CUATRO CLIMAS — **límite estricto**

> ## 🔴 **Queda descartado como condición de existencia:** *«cada módulo debe tener un
> ## cuadrante macro en el que funcione»*.

**El capítulo 19 ya lo resolvió** *(D97, y los parches D99-D104)*: de las siete hipótesis de
régimen, **una recibió apoyo, una parcial, tres no se confirmaron y dos no eran evaluables**.
Exigir un cuadrante favorable por módulo **contradiría evidencia propia ya cerrada**.

**PMMA es principalmente una arquitectura funcional, no un modelo de *timing* macro.**

| ✅ Los regímenes **podrán** usarse después para estudiar | ❌ Los regímenes **NO** se usarán para |
|---|---|
| Sensibilidades | Justificar la existencia de un módulo |
| Complementariedad entre funciones | Eliminar un módulo por no «ganar» un cuadrante |
| Concentración de vulnerabilidades | Reordenar la taxonomía |

**Ejemplos que quedan expresamente protegidos:** **Aceleración** puede existir por primas de
retorno a largo plazo · **Asimetría** por opcionalidad · **Motor** como fuente productiva
central. **Ninguno necesita ganar un cuadrante para justificar su existencia.**

---

# 12. MÉTRICAS DEL ESTUDIO — **sin puntuación agregada**

> ⚠️ **No se construirá ningún «PMMA Score».** Una puntuación agregada esconde las
> compensaciones y permite que un mal resultado se diluya en un promedio.

| # | Indicador | Cómo se mide | Se compara con |
|---|---|---|---|
| **M1** | **Cobertura sin excepción** | % de exposiciones clasificables sin excepción ni extensión | T0 y T1 |
| **M2** | **Ambigüedades** | Nº de asignaciones con ambigüedad media o alta | T0 y T1 |
| **M3** | **Funciones no representadas** | Nº de funciones huérfanas, con su frecuencia | T0 y T1 |
| **M4** | **Módulos nunca utilizados** | Nº de módulos a 0% en **toda** la muestra | — |
| **M5** | **Solapamientos recurrentes** | Pares de módulos ambiguos en ≥2 carteras | — |
| **M6** | **Discrepancia de clasificación** | % de asignaciones que difieren en la prueba de reproducibilidad | — |
| **M7** | **Necesidad de redefinición** | Nº de veces que hubo que retocar una definición | — |
| **M8** | **Parsimonia** | Categorías utilizadas / capacidad de distinguir arquitecturas | **T1 es el rival** |
| **M9** | **Usos del Protocolo de Extensión** | Recuento absoluto | — |

**Cada métrica se publica por separado, con su numerador y denominador.**

---

# 13. POSIBLES RESULTADOS — **predefinidos**

| | Resultado | Condición aproximada |
|---|---|---|
| 🟢 **A** | **PMMA SOBREVIVE** | Ningún F se cumple · M1 alto · PMMA aporta sobre T1 |
| 🟡 **B** | **SOBREVIVE CON AJUSTES** | Se cumplen **F2 o F5** de forma acotada: alguna frontera o definición necesita modificación, pero la estructura aguanta |
| 🟠 **C** | **REESTRUCTURACIÓN** | Se cumplen **F3, F9 o F2 de forma amplia**: la lógica funcional sirve, pero el número o la estructura de módulos debe cambiar materialmente |
| 🔴 **D** | **NO GENERALIZA** | Se cumplen **F1, F4, F7 u F8**: PMMA funciona principalmente como descripción de Global 10Y |

> **Los cuatro resultados son igualmente aceptables.** El estudio no tiene un desenlace
> preferido, y **el resultado D no es un fracaso del trabajo: es un hallazgo publicable.**

---

# 14. FUENTES REQUERIDAS

| Tipo | Exigencia |
|---|---|
| **Carteras externas** | Fuente primaria: libro, documento del creador o documentación institucional. **Versión declarada** |
| **Funciones económicas y factores** | Literatura académica revisada |
| **Datos de producto** | Documentación primaria del emisor |
| **Etiquetado obligatorio** | **[DATO]** · **[EVIDENCIA EXTERNA]** · **[INTERPRETACIÓN]** · **[HIPÓTESIS PMMA]** — **ninguna categoría se convierte en otra** |

---

# 15. CONTROL DE HINDSIGHT Y TRAZABILIDAD

> **Esta metodología se fija ANTES de estudiar sistemáticamente las carteras externas y
> ANTES de decidir si los siete módulos sobreviven.**

## 15.1 Tabla de trazabilidad de reglas

| Regla | Fecha de fijación | ¿Pre-resultados? | Cambio posterior | Motivo |
|---|---|---|---|---|
| **Pregunta principal y Q1-Q8** | 15-ago-2026 | ✅ Sí | — | — |
| **C1-C10** | 15-ago-2026 | ✅ Sí | — | Propuestos en el encargo |
| **C11 · parsimonia de conservación** | 15-ago-2026 | ✅ Sí | — | **Añadido en la autoauditoría §19: C7 solo penalizaba crear, no conservar** |
| **C12 · estabilidad de frontera** | 15-ago-2026 | ✅ Sí | — | Añadido para hacer operativo C9 |
| **F1-F8** | 15-ago-2026 | ✅ Sí | — | Propuestos en el encargo |
| **Umbrales cuantitativos de F1-F9** | 15-ago-2026 | ✅ Sí | — | **Sin umbral no eran falsables** |
| **F9 · módulo inutilizado** | 15-ago-2026 | ✅ Sí | — | Contrapartida de C11 |
| **T0 y T1 como taxonomías rivales** | 15-ago-2026 | ✅ Sí | — | **F8 no era auditable sin rival concreto** |
| **Muestra de 10 arquitecturas** | 15-ago-2026 | ✅ Sí | — | 6 elegidas por su capacidad de romper PMMA |
| **Predicciones registradas §16** | 15-ago-2026 | ✅ Sí | — | Anti-hindsight |
| *(filas siguientes)* | — | ❌ **POST HOC** | — | **Toda regla añadida después se etiqueta así** |

---

# 16. 🔮 PREDICCIONES REGISTRADAS — **antes de mirar**

> **El dispositivo anti-hindsight más fuerte del protocolo.** Si aciertan, los criterios
> capturaban algo real; si fallan, queda registrado que fallaron.

| # | Predicción | Falsable por |
|---|---|---|
| **P1** | **Emergentes será el módulo más cuestionado.** Es geográfico, no funcional: su función *(crecimiento)* ya la cubre Motor, y su justificación real parece ser **decisión dedicada modificable**, que es gobernanza, no función | Si sobrevive C1-C2 sin tensión |
| **P2** | **Defensivos y Freno se solaparán** en al menos dos carteras: ambos «estabilizan», con instrumentos distintos | Si M5 no los empareja |
| **P3** | **Trend following (R4) no tendrá módulo natural** y será el caso más fuerte a favor de F3 | Si encaja limpiamente |
| **P4** | **La cartera de un solo fondo (E) será representable pero trivial**, y pondrá a prueba C8 más que C1 | Si resulta no representable |
| **P5** | **All Weather (C) generará tensión de unidad de medida**: PMMA asigna por peso y ella por riesgo | Si no aparece esa tensión |
| **P6** | **PMMA superará a T0** con claridad **y le costará superar a T1** | Si T1 pierde con holgura |
| **P7** | **El resultado más probable es 🟡 B o 🟠 C**, no 🟢 A | Cualquier otro desenlace |

**Estas predicciones no condicionan el análisis. Se contrastarán al final como prueba de
calibración.**

---

# 17. LIMITACIONES DEL ESTUDIO — declaradas desde ahora

| # | Limitación |
|---|---|
| **L-U1** | **Un solo analista.** La prueba de reproducibilidad es intra-analista; **L1 del cap. 4 no se cierra** |
| **L-U2** | **La muestra de carteras es intencionada, no aleatoria.** Se elige para maximizar tensión, lo que **sesga hacia encontrar problemas** — declarado como sesgo deliberado y conservador |
| **L-U3** | **PMMA lo diseñó quien lo evalúa.** El conflicto es estructural y solo se mitiga con reglas escritas antes y publicación de todos los fallos |
| **L-U4** | **«Función» no es observable.** Se infiere del mandato declarado del creador; cuando el creador no lo declara, **la función se atribuye y eso se marca como ambigüedad alta** |
| **L-U5** | **El estudio es conceptual, no empírico.** No mide si las funciones se comportan como se supone — eso es la pregunta B, fuera de alcance |
| **L-U6** | **Diez arquitecturas no son la población de carteras posibles** |

---

# 18. PLAN DE EJECUCIÓN DE LA FASE 1 *(no se ejecuta ahora)*

| Paso | Contenido | Producto |
|---|---|---|
| **1** | **Fuentes**: localizar y citar las diez arquitecturas con versión declarada | Tabla de fuentes |
| **2** | **Universo de exposiciones**: función económica de cada una de las 26, **sin asignar módulo todavía** | Diccionario de funciones |
| **3** | **Clasificación ciega**: asignar módulo con la plantilla, una cartera cada vez | 10 fichas |
| **4** | **Prueba de reproducibilidad** *(§9.1)*, con ≥48h de separación | M6 |
| **5** | **Red Team** sobre los 12 casos duros | Registro de excepciones |
| **6** | **Aplicar T0 y T1** a la misma muestra | Comparación de M1, M2, M3, M8 |
| **7** | **Matriz de solapamiento funcional 7×7** | M5 |
| **8** | **Evaluar F1-F9** contra sus umbrales | Tabla de fallos |
| **9** | **Contrastar las predicciones §16** | Calibración |
| **10** | **Veredicto A/B/C/D** y, si procede, propuesta de arquitectura revisada | Informe final |

**Ningún paso puede adelantarse.** El paso 6 **no** puede hacerse después de conocer el
resultado de PMMA para ajustar la comparación.

---

# 19. 🔍 AUTOAUDITORÍA DEL PROTOCOLO — **antes de congelar**

## A · ¿Hay alguna regla diseñada para que sobrevivan los siete módulos?

🔴 **Sí, había una — y se ha corregido.** **C7 (parsimonia) penalizaba únicamente crear
módulos nuevos**, no conservarlos. Tal como estaba, cualquier propuesta de módulo adicional
tenía que justificarse mientras **los siete existentes no tenían que justificar su
permanencia**. **Corrección: se añaden C11 (parsimonia de conservación) y F9 (módulo
inutilizado y absorbible).**

🟠 **Segundo riesgo detectado: C10 («peso cero permitido»)** puede usarse para blindar un
módulo que nadie usa. **Corrección: C10 se acota explícitamente** — protege la
representabilidad de una cartera concreta, **no la existencia del módulo**, que responde ante
C11 y F9.

## B · ¿Algún criterio sería distinto si PMMA tuviera 6 u 8 módulos?

**Revisados C1-C12 uno a uno: ninguno menciona el número siete ni depende de él.** Todos se
formulan sobre **un módulo genérico**. La muestra, el universo, los umbrales y las taxonomías
rivales tampoco dependen del número actual.

⚠️ **Salvo un punto:** la matriz de solapamiento es **7×7** porque hoy hay siete. **Se
redimensionaría automáticamente** con otro número. **No es un sesgo, es una consecuencia.**

## C · ¿El protocolo permite realmente concluir que PMMA no generaliza?

**Sí, y por tres vías independientes:** F1 *(>15% de exposiciones necesitan excepción)* ·
F4 *(>20% de discrepancia)* · F7 *(≥3 carteras no encajan)* · **y F8**, que puede tumbar
PMMA **aunque todos los módulos cumplan C1-C6**, simplemente porque una taxonomía de cuatro
categorías haga el mismo trabajo.

**F8 es la vía más peligrosa para PMMA y está deliberadamente incluida**, con **T1
definida ex ante** para que no pueda elegirse después un rival cómodo.

## D · ¿Confundimos función económica con rentabilidad histórica?

**No, y está blindado en §3:** la pregunta A *(taxonomía)* y la B *(rendimiento)* se separan
formalmente, y **queda prohibido usar rentabilidad, Sharpe o alfa como argumento sobre la
existencia de un módulo**. Si ese razonamiento aparece durante la ejecución, **se marca como
violación del protocolo**.

## E · ¿Intentamos convertir los cuatro regímenes en algo que el cap. 19 ya demostró que no son?

**No.** §11 lo prohíbe expresamente y cita la evidencia: de siete hipótesis de régimen, **solo
una recibió apoyo**. **Exigir un cuadrante por módulo contradiría evidencia propia cerrada.**
Los regímenes quedan disponibles **después**, para estudiar sensibilidades — nunca como
condición de existencia.

## F 🆕 · Un sesgo adicional que detecto yo, y que conviene declarar

**El propio principio «función antes que producto» es difícil de falsar**, porque permite
reasignar cualquier caso incómodo diciendo «su función aquí es otra». **Esa flexibilidad es
la fuerza del método y a la vez su mayor riesgo epistemológico.**

**Contrapeso incorporado:** **C12 (estabilidad de frontera)** exige enunciar la frontera **sin
apelar a casos concretos**, y **F6** declara fallo si un módulo solo puede definirse
enumerando productos. **Sin esos dos criterios, PMMA sería infalsable por construcción.**

---

# 20. CIERRE DE LA FASE 0

**Este protocolo queda CONGELADO el 15 de agosto de 2026.**

| ✅ Verificado | |
|---|---|
| **Cap. 4** | Intacto — cerrado v2.1 *(D105)* |
| **Cap. 19** | Intacto — cerrado v1.2 *(D97)* |
| **Cartera oficial** | Intacta — congelada |
| **Laboratorio X-Ray** | Intacto — congelado y no propagado *(D107)* |
| **PMMA** | **No modificado.** Ni un módulo añadido, eliminado ni redefinido |
| **Fase 1** | **NO ejecutada** |

> ### **El objetivo no es que PMMA sobreviva. El objetivo es saber qué queda de PMMA después
> ### de intentar romperlo con reglas escritas antes de saber el resultado.**

---

## REGISTRO

**15-ago-2026 — Fase 0 de PMMA Universal.** Se fijan pregunta, hipótesis, criterios de
existencia *(C1-C12)*, criterios de fallo con umbrales *(F1-F9)*, taxonomías rivales
*(T0, T1)*, universo de 26 exposiciones, muestra de 10 arquitecturas, plantilla única, Red
Team de 12 casos, métricas M1-M9, límites frente a los regímenes, siete predicciones y
autoauditoría. **Pendiente de aprobación antes de ejecutar la Fase 1.**
