# CAPÍTULO 4 — PEAKY MINDERS MODULAR ARCHITECTURE

## Investment Book · Parte I · ✅ **CERRADO v2** · aprobado el 13 de agosto de 2026 *(D79)*

> **Convención tipográfica de este capítulo:**
> **[MODELO]** = afirmación propia de PMMA, sostenida por su coherencia interna y por la
> evidencia de implementación de este trabajo.
> **[EVIDENCIA EXTERNA]** = afirmación que requiere cita académica o fuente primaria,
> recogida en la tabla final de fuentes pendientes.
> Nada de lo marcado [MODELO] se presenta como hecho empírico demostrado.

---

## 4.1 El problema que resuelve

Una cartera de inversión suele construirse en el orden equivocado. El inversor —particular
o profesional— parte de los productos: un fondo que ha leído recomendado, un ETF con buena
rentabilidad reciente, una acción con una historia atractiva. El resultado es una
**acumulación de instrumentos individualmente defendibles y colectivamente inexplicables**:
nadie puede decir qué trabajo hace cada posición dentro del conjunto, qué pasaría si se
eliminara, ni cuántas fuentes de riesgo independientes existen realmente bajo la aparente
variedad de nombres.

**[MODELO]** Este trabajo denomina a ese estado *cartera-lista*: una colección de productos
sin arquitectura. Frente a él, PMMA propone la *cartera-sistema*: una estructura en la que
cada posición existe porque responde a una pregunta formulada antes de comprarla.

El problema no es teórico. Tiene tres manifestaciones medibles:

1. **Diversificación aparente.** Diez ETF pueden ser diez versiones del mismo riesgo.
   En la propia implementación de este trabajo, vehículos del módulo Aceleración
   —formalmente distintos— presentan **correlaciones materialmente elevadas en
   determinadas parejas** entre sí y con el núcleo de la cartera *(los valores exactos,
   con ventana, frecuencia, fuente y fecha, se incorporan en el capítulo 18)*. La variedad
   de tickers no era variedad de comportamiento, y **PMMA obliga explícitamente a
   comprobarlo**.
2. **Decisiones sin registro.** Sin arquitectura previa, cada compra se justifica después
   de hecha. La literatura sobre sesgos del inversor documenta la facilidad con la que la
   narrativa posterior sustituye al criterio anterior. **[EVIDENCIA EXTERNA]** — sesgo
   retrospectivo y racionalización *post hoc* (Kahneman; Montier, *Behavioural Investing*).
3. **Incomparabilidad.** Dos carteras construidas con lógicas distintas no pueden
   compararse posición a posición. Sin un lenguaje común de funciones, la comparación
   **tiende a apoyarse** en rentabilidades pasadas, que es una métrica poco informativa
   sobre la calidad del diseño. **[EVIDENCIA EXTERNA]** — la persistencia de rentabilidad
   como criterio de selección es débil (SPIVA Persistence Scorecard).

**[MODELO]** PMMA responde a los tres con una sola operación: separar la **función** que el
capital debe cumplir del **instrumento** que la implementa, y hacer esa separación
**auditable** en cada eslabón.

---

## 4.2 Función antes que producto

**[MODELO]** El principio ordenador de PMMA se enuncia en cuatro palabras:

> ### **Función antes que producto.**

Primero se decide qué funciones necesita la cartera dado su mandato; después se decide qué
exposición implementa cada función; solo al final se elige el vehículo concreto. El ticker
aparece en el último paso del proceso, no en el primero.

La cadena completa del método es:

```
OBJETIVO → MANDATO → FUNCIÓN → MÓDULO → PESO → EXPOSICIÓN → VEHÍCULO
        → X-RAY → RIESGO → EJECUCIÓN → CONTROL
```

Cada flecha es un punto de control documentable. La aportación no está en ninguna casilla
individual —todas existen por separado en la práctica profesional— sino en exigir que la
cadena entera quede escrita y sea verificable, de modo que cualquier tercero pueda recorrer
el camino desde el objetivo hasta el último ISIN y encontrar en cada paso una decisión
fechada con su motivo.

Este capítulo describe el método. Los capítulos 10 a 14 muestran la cadena aplicada a la
implementación *Peaky Minders Global 10Y*; el registro de decisiones (anexo B) constituye
la prueba documental de que el orden se respetó.

---

## 4.3 El Principio de Función Dominante

**[MODELO]** La misma clase de activo puede desempeñar funciones distintas según el motivo
por el que se incorpora. Un ETF de salud dentro de un índice global no necesita separarse:
forma parte del núcleo. El mismo ETF comprado deliberadamente para reducir la ciclicidad de
la cartera cumple una función defensiva. El instrumento es idéntico; la función, no.

De ahí la regla central de clasificación:

> **Toda posición se asigna principalmente al módulo que mejor explique la razón
> estratégica por la que está presente en la cartera.**

La pregunta decisiva no es *«¿qué contiene este ETF?»* sino *«¿por qué existe esta posición
dentro de esta cartera?»*. La primera pregunta la responde cualquier folleto; la segunda
solo puede responderla el constructor, y PMMA le obliga a dejarla escrita (campo `tesis`
del modelo de datos, §4.11).

Esta elección tiene un coste que el método reconoce en lugar de ocultar: la función
dominante es un juicio del analista, no una propiedad observable del instrumento. La
sección 4.14 trata esa subjetividad como limitación estructural y describe los cinco
mecanismos que la acotan.

---

## 4.4 Los siete módulos estructurales

**[MODELO]** PMMA organiza la asignación estratégica en siete módulos. Cada uno se define
por su misión y se verifica con una pregunta de control; ninguno prescribe productos ni
pesos.

| # | Módulo | Misión | Pregunta de control |
|---|---|---|---|
| 1 | 🚀 **Motor** | Capturar el crecimiento económico y empresarial de largo plazo | *Si elimino esta posición, ¿reduzco significativamente la capacidad central de crecimiento?* |
| 2 | 🌿 **Defensivos** | Mantener exposición productiva reduciendo sensibilidad al ciclo | *¿Mantiene exposición empresarial pero pretende mejorar el comportamiento relativo en escenarios adversos?* |
| 3 | ⚡ **Aceleración** | Introducir fuentes adicionales de rentabilidad esperada sobre el núcleo neutral | *¿Existiría esta exposición si solo quisiera replicar el mercado?* |
| 4 | 🌍 **Emergentes** | Exposición estratégica diferenciada a economías emergentes | *¿Existe una asignación a emergentes modificable independientemente del Motor?* |
| 5 | ⚓ **Freno** | Estabilizar, aportar liquidez estratégica y exponer a factores distintos de los activos productivos | *¿Forma parte estructural de la cartera para estabilizar o responder a escenarios distintos de la renta variable?* |
| 6 | 🥇 **Activos Reales** | Comportamiento vinculado a inflación y confianza monetaria, distinto de acciones y bonos nominales | *¿El objetivo principal es una fuente de comportamiento ligada a activos reales o inflación?* |
| 7 | 💥 **Asimetría** | Opcionalidad de alto potencial con pérdida máxima acotada por tamaño | *¿Aceptaríamos la pérdida prácticamente total sin comprometer el plan patrimonial?* |

Cuatro propiedades completan la definición:

- **Los módulos son funciones, no productos.** El Motor no «es» un índice mundial; es la
  función de capturar crecimiento agregado, que en un mandato concreto puede implementarse
  con uno u otro instrumento.
- **Un módulo puede pesar 0%.** El cero también informa: significa que esa función no ha
  sido incorporada deliberadamente. Una cartera 90/10 usa dos módulos y sigue siendo una
  implementación válida del sistema.
- **Los pesos dependen del mandato.** PMMA no prescribe porcentajes; los pesos de la
  implementación de este trabajo (capítulo 10) son una parametrización, no una regla.
- **La frontera entre módulos la fija la tesis, no el instrumento.** Un REIT puede ser
  Motor (dentro de un índice global) o Activos Reales (asignación inmobiliaria específica);
  los TIPS son Freno por defecto —su función habitual es estabilizadora y de respuesta a
  regímenes, y económicamente siguen siendo renta fija— sin que ello impida asignarlos a
  otra función si la tesis registrada lo justifica; la calidad (*quality*) puede ser
  Defensivos si se compra por resiliencia o Aceleración si se compra como prima de
  retorno — el árbol de clasificación (§4.9) resuelve el orden y la tesis registrada deja
  constancia del motivo.

**[MODELO — mapa de diseño contrastado posteriormente en el capítulo 19]** Como referencia
de diseño, cada módulo llevaba asociado un comportamiento *esperado* por régimen económico
(crecimiento × inflación). Su desarrollo, datación histórica y contraste cuantitativo se
realizaron en el capítulo 19. **Las celdas que aparecen sin valor son aquellas cuya lectura
por régimen no recibió apoyo suficiente en esa prueba, o no pudo contrastarse con la
evidencia disponible; las celdas que conservan valor siguen expresando hipótesis de
diseño, no resultados históricos medidos.**

| Módulo | Crecim.↑ Infl.↓ | Crecim.↑ Infl.↑ | Crecim.↓ Infl.↑ | Crecim.↓ Infl.↓ |
|---|---|---|---|---|
| Motor | — | — | — | — |
| Defensivos | favorable | mixto | mixto | — |
| Aceleración | — | — | — | — |
| Emergentes | favorable | **mixto/favorable** | adverso | adverso |
| Freno | — | — | — | — |
| Activos Reales | neutro | **favorable** | **favorable** | mixto |
| Asimetría | *idiosincrático — no asignable a régimen* | | | |

> **[MODELO — actualizado tras el capítulo 19 · D100]** **La fila del Motor aparece sin
> valor en las cuatro columnas.** La prueba histórica del capítulo 19 **no respalda la
> lectura direccional que este mapa proponía**: el comportamiento real más favorable del
> Motor no se observó con crecimiento fuerte, sino **con crecimiento débil e inflación
> baja**, que la tabla anterior calificaba de adverso. Lo único que la prueba sostiene con
> claridad es que **el Motor obtuvo su peor comportamiento real con crecimiento débil e
> inflación alta**. Las cifras están en el capítulo 19 *(§19.10)*.
>
> ⚠️ **No se sustituye una lectura direccional por otra.** El análisis empareja
> macroeconomía y rentabilidad del **mismo trimestre**, de modo que mide **coincidencia, no
> causa**; las explicaciones posibles quedan registradas en el capítulo 19 §19.13 *(C-1)*
> **como hipótesis interpretativas, no adoptadas**.

> **[MODELO — actualizado tras el capítulo 19 · D98]** **La fila de Aceleración aparece sin
> valor en las cuatro columnas.** El motivo: **la prueba histórica del capítulo 19 no
> proporciona apoyo suficiente para justificar Aceleración como una exposición
> específicamente orientada a determinados regímenes macroeconómicos.** Por ello, la
> justificación principal del módulo se mantiene en la búsqueda de **primas o fuentes
> adicionales de rentabilidad esperada a largo plazo**, no en una función táctica por
> régimen.
>
> ⚠️ **Esto no equivale a afirmar que Aceleración sea independiente del régimen
> económico.** La prueba realizada no permite una conclusión tan general: **es una retirada
> de justificación, no una afirmación contraria.** El detalle está en el capítulo 19 §19.12
> y §19.13 *(C-3)*.
>
> **Alcance:** este cambio afecta **solo a la fila de Aceleración**. La función del módulo,
> su peso, sus vehículos y las demás filas del mapa permanecen sin modificar.

> **[MODELO — actualizado tras el capítulo 19 · D101]** **La fila de Freno aparece sin valor
> en las cuatro columnas porque la prueba histórica no permitió evaluar el módulo en su
> forma completa.** El análisis cubrió la pata monetaria, pero **no la renta fija con
> duración**. Dentro de la parte evaluable, el comportamiento relativo —**siempre frente al
> Motor, no en términos absolutos**— **no reprodujo el patrón previsto por la hipótesis
> inicial**. **Ese resultado parcial no autoriza a invertir ni a reformular la lectura del
> módulo completo.**
>
> ⚠️ **La ausencia de valores significa evidencia insuficiente para contrastar la hipótesis
> original, no evidencia de que Freno carezca de comportamiento diferenciado según el
> entorno. Su función estructural permanece intacta.**

> **[MODELO — actualizado tras el capítulo 19 · D102]** **La lectura de Defensivos se acota
> tras la prueba histórica.** En **crecimiento débil + inflación alta**, los proxies de
> consumo básico y salud **recibieron apoyo bajo los dos clasificadores examinados**. En
> **crecimiento débil + inflación baja**, el resultado **no fue estable**: el proxy que
> cumplía cambiaba al modificar el criterio de clasificación. Por ello, **se retira la
> lectura de esa última celda**.
>
> ⚠️ **No se modifica retrospectivamente la celda de crecimiento débil + inflación alta para
> hacerla más favorable.** El mapa conserva su hipótesis de diseño allí donde no ha sido
> retirada; **el detalle empírico y su nivel de apoyo corresponden al capítulo 19**.

---

## 4.5 Management Mode: la segunda dimensión

**[MODELO]** La función estructural no agota la descripción de una posición. Una segunda
dimensión, **ortogonal** a la primera y denominada **Management Mode** (modo de gestión),
indica *cómo* se gestiona el capital:

| Modo | Quién decide | Ejemplo en la implementación |
|---|---|---|
| ① **Pasiva / indexada** | Un índice | Núcleo del Motor |
| ② **Sistemática / factorial** | Una regla predefinida | Small cap, multifactor |
| ③ **Activa delegada** | Un gestor externo con mandato acotado | Robeco (Aceleración) · PIMCO (Freno) |
| ④ **Convicción directa** | El propio equipo, empresa a empresa, con protocolo | Conviction Overlay |

Toda posición tiene un módulo **y** un modo. El fondo Robeco BP Global Premium se describe
como *Aceleración + activa delegada*: su función es capturar la prima de valor; su modo es
la delegación en un gestor. **Es una posición estructural del módulo Aceleración, no una
capa superpuesta**: el modo de gestión describe cómo se administra ese capital, sin
alterar su lugar en la arquitectura. Lo mismo vale para el PIMCO dentro del Freno.

**Conviction Overlay** es un término reservado: designa exclusivamente la capa condicional
de selección directa de compañías de *Global 10Y* (modo ④), que sí es una capa superpuesta
porque puede existir o no, y que opera bajo un protocolo propio (precio de entrada IDC,
Fecha Cero, dos tramos de compra, evaluación contra el Motor), desarrollado en el capítulo
12. Confundir Convicción con «cualquier fondo activo» destruiría la distinción más
importante de la capa activa: quién toma la decisión y bajo qué reglas escritas.

---

## 4.6 Las capas transversales: Conviction Overlay y Execution Layer

**[MODELO]** Sobre los siete módulos operan dos capas que **no son clases de activo** y por
tanto no se suman a la asignación estructural como filas adicionales.

**Conviction Overlay.** La capa condicional de selección directa (modo ④). El capital que
gestiona cuenta una sola vez, en su módulo estructural; el overlay explica bajo qué
protocolo se tomó la decisión, no añade un *cuánto*. Las posiciones estructurales con modo
③ (activa delegada) **no forman parte del overlay**: son módulos gestionados por terceros
bajo mandato.

**Execution Layer — la Reserva Operativa.** Capital destinado a la ejecución de la
estrategia: aportaciones en tránsito, compras planificadas, rebalanceos. Su formulación
exacta en este trabajo es:

> **La política de Reserva es permanente; el capital que la ocupa es transitorio.**

Existe una capacidad operativa objetivo/máxima (en esta implementación, el 3%), pero su
saldo fluctúa con las aportaciones y la ejecución. La distinción crítica es con el Freno:
un 20% mantenido permanentemente en letras del tesoro como estabilizador es Freno
(asignación estratégica); un 3% esperando ejecutar una compra es Reserva (infraestructura).
Confundir ambas cosas es confundir una decisión de inversión con una restricción operativa
— los reembolsos de fondos tardan días y las oportunidades no esperan.

---

## 4.7 Las tres vistas analíticas del capital

**[MODELO]** La coexistencia de módulos, Reserva y overlay exige reglas de agregación
explícitas, sin las cuales el mismo euro podría contarse dos veces — o la suma de módulos
presentarse como el total del capital cuando no lo es. PMMA adopta **tres vistas
analíticas simultáneas**:

**A. Total Capital View.** Representa dónde está físicamente todo el dinero:

> **siete módulos + Reserva = 100% del capital total.**

En la Fecha Cero de *Global 10Y*: módulos estratégicos 97% + Reserva Operativa 3% = 100%.
Los siete módulos, por sí solos, **no** suman el 100% del capital total cuando existe
Reserva.

**B. Strategic Allocation View.** Excluye la Reserva operativa y normaliza los siete
módulos estratégicos sobre 100%. Responde a la pregunta *«¿cómo está distribuida la
cartera estratégica?»* y **aplica la misma lógica de normalización sobre el capital
analizado que utiliza el X-Ray al excluir la Reserva** (capítulo 15).

**C. Governance / Funding View.** Registra bajo qué protocolo se administra el capital.
En esta implementación, la identidad de gobernanza se denomina **47% Governance Funding
Pool** — el término evita confundir el Motor como *función estructural* con el *capital
que financia operativamente Convicción*:

> **44 Motor ordinario + 3 Reserva + 0 Convicción = 47%** en Fecha Cero,
> evaluado en las fechas de revisión,

con un techo de Convicción del 14% que es presupuesto máximo de riesgo, no objetivo.
Tras una compra de Convicción, la posición recibe **además** su clasificación funcional
correspondiente en la Structural Exposure View: *Microsoft comprada por Convicción →
**Motor** en Structural Exposure View + **Convicción Directa** en Governance View*.
El capital cuenta una sola vez en las vistas A y B: **no existe doble contabilización.**

La regla que une las tres vistas:

> **Módulo = qué función económica desempeña el capital.
> Convicción = bajo qué protocolo se tomó y se gestiona la decisión.
> Convicción es una etiqueta de gobernanza, nunca una clase adicional de activo, y las
> dimensiones no se suman en una misma tabla.**

---

## 4.8 Position Mode y Look-Through Mode

**[MODELO]** PMMA analiza toda cartera en dos modos complementarios.

**Position Mode** (predeterminado). Cada vehículo se asigna íntegramente a su función
dominante. Un índice global usado como núcleo es 100% Motor, aunque contenga
internamente sectores defensivos o mercados emergentes. Es el modo de **construcción,
comunicación y gobierno**: refleja la decisión real del constructor.

**Look-Through Mode.** Descompone cada vehículo en su exposición económica subyacente:
países, sectores, factores, compañías, duración, crédito, divisa. Es el modo de
**auditoría**: mide lo que realmente se posee, con independencia de la intención.
Formalmente, para **exposiciones aditivas** (pesos por país, sector, factor o compañía),
la exposición de la cartera al atributo *A* es la suma, sobre todas las posiciones, del
peso de cada posición por su exposición interna a *A*:

```
Exposición(A) = Σᵢ  pesoᵢ × exposiciónᵢ(A)        [válida solo para atributos aditivos]
```

⚠️ **Esta linealidad no es general.** La volatilidad, el drawdown, la contribución al
riesgo y determinadas métricas de crédito **no se agregan linealmente**: dependen de
correlaciones y de efectos de composición, y requieren agregación específica. Sumar
volatilidades ponderadas, por ejemplo, sobreestima el riesgo de una cartera diversificada.
El capítulo 17 detalla qué métricas admiten cada tipo de agregación.

La frase que resume la relación entre ambos modos —y entre la Parte I y la Parte III de
este trabajo— es:

> ### **La arquitectura expresa la intención. El X-Ray verifica el resultado.**

Ninguno de los dos modos basta por separado. Position Mode sin look-through permite
autoengaño (la «diversificación» de diez ETF idénticos); look-through sin Position Mode
disuelve la decisión en una nube de porcentajes sin autor. El capítulo 15 aplica esta
doble lectura a la implementación, incluida su consecuencia más incómoda: la regla de no
duplicidad de Emergentes se satisface en Position Mode y se verifica en Look-Through,
donde la exposición emergente total (bloque específico más la contenida en el núcleo
global) se cuantifica y se declara como sobreponderación deliberada.

---

## 4.9 El árbol de clasificación

**[MODELO]** Para reducir la discrecionalidad del Principio de Función Dominante, toda
posición nueva atraviesa ocho preguntas **en orden fijo**. Cada pregunta interroga por la
**función dominante** de la posición dentro de esta cartera — nunca por su mera clase de
activo, porque la clase no determina la función (§4.3). El orden no es estético: decide
los casos ambiguos (una posición que podría responder «sí» a dos preguntas recibe el
módulo de la primera), y por eso el orden mismo forma parte del método.

```
P1  ¿Es capital destinado a la EJECUCIÓN de la estrategia —aportaciones en
    tránsito, compras planificadas— y no una asignación estratégica?
                                              → Reserva (Execution Layer)

P2  ¿Su función dominante es ESTABILIZAR la cartera, aportar liquidez
    estratégica o responder a escenarios distintos de los activos productivos?
                                              → Freno

P3  ¿Su función dominante es aportar un comportamiento ligado a ACTIVOS REALES
    o a la inflación, distinto de acciones y bonos nominales?
                                              → Activos Reales

P4  ¿Es una exposición DEDICADA a mercados emergentes, modificable
    independientemente del Motor?              → Emergentes

P5  ¿Es renta variable incorporada específicamente por su carácter DEFENSIVO?
                                              → Defensivos

P6  ¿Existe una tesis explícita de PRIMA ADICIONAL o diferenciación frente al
    núcleo neutral de mercado?                 → Aceleración

P7  ¿Forma parte de la exposición PRODUCTIVA CENTRAL de largo plazo?
                                              → Motor

P8  ¿Es una posición de alta OPCIONALIDAD cuya pérdida total, acotada por
    tamaño, no comprometería el plan?          → Asimetría

—   Sin función dominante honesta              → Protocolo de Extensión (§4.10)
```

Tres precisiones evitan que el árbol degenere en clasificación por clase de activo:

- **La clase no responde por la función.** Un bono responde «sí» en P2 solo si su función
  es estabilizadora; un bono high yield comprado como fuente de retorno no la tiene clara
  y debe seguir bajando por el árbol — posiblemente hasta el Protocolo de Extensión.
- **Los casos ambiguos no se fuerzan.** TIPS: por defecto Freno, porque su función
  habitual es estabilizadora y de respuesta a regímenes — pero es un *default* revisable
  por tesis, no un automatismo de clase. REIT: Motor si vive dentro de un índice global,
  Activos Reales si es una asignación inmobiliaria específica — lo decide la tesis.
  Crédito privado, deuda mezzanine o estrategias híbridas **no tienen respuesta
  automática**: si ninguna pregunta captura su función dominante con honestidad, terminan
  en Extensión, no encajados a la fuerza.
- **El caso *quality*** ilustra el mecanismo del orden: comprada por resiliencia responde
  «sí» en P5 (Defensivos); comprada como prima de retorno responde «no» en P5 y «sí» en
  P6 (Aceleración). La tesis registrada documenta cuál de las dos razones operó.

Cada clasificación lleva además un campo de **confianza** (alta / media / ambigua) y, en
caso de ambigüedad, una segunda revisión independiente (§4.14, mecanismos de acotación).

---

## 4.10 El Protocolo de Extensión

**[MODELO]** Una taxonomía se corrompe cuando se deforma para aparentar que todo encaja.
Existen instrumentos sin función dominante honesta dentro de los siete módulos: gestión
alternativa (managed futures, market neutral, arbitraje), capital privado, crédito privado,
estrategias de volatilidad, estructurados, apalancamiento.

La regla es doble:

- **Si existe función dominante clara**, se asigna al módulo correspondiente con etiqueta
  descriptiva.
- **Si no existe**, la posición se clasifica temporalmente como **Extensión / Estrategia
  Alternativa** hasta que su función quede justificada — o se decide que no pertenece a la
  cartera.

> **Es preferible reconocer una excepción que falsear la arquitectura.**

El protocolo cumple dos papeles: permite crecer sin romper la coherencia y actúa como
declaración de límites — el marco no pretende describirlo todo, y lo dice.

---

## 4.11 El modelo de datos

**[MODELO]** Para que el método sea operable y no solo conceptual, cada posición se
registra con un conjunto mínimo de campos. El modelo original de PMMA (26 campos:
identificación, pesos actual y objetivo, módulo y submódulo, marcas de overlay y reserva,
benchmark, exposiciones, coste, riesgo, tesis y regla de revisión) se amplía en este
trabajo con **nueve campos adicionales cuya necesidad demostró la propia implementación**:

| Campo añadido | Lección que lo exige |
|---|---|
| **ISIN** | El ticker es ambiguo en vehículos UCITS con múltiples cotizaciones |
| **Clase de participación** | Misma cartera, distinta clase, distinto coste (caso clases S/D) |
| **Proxy analítico** (sí/no + cuál) | Sin él, la regla de atribución real-vs-proxy no es registrable |
| **Cobertura de divisa** | El único caso no equivalente del X-Ray fue exactamente éste |
| **Traspasabilidad fiscal** | Decidió la elección fondo vs ETF en pequeña capitalización |
| **Acumulación / distribución** | Atributo operativo de primer orden omitido en el modelo original |
| **Fuente y fecha del dato** | Distingue «verificado en KID» de «tomado de plataforma» |
| **Confianza de clasificación** | Convierte la subjetividad del §4.3 en dato auditable |
| **Contribución al riesgo** | El peso de capital no es el peso de riesgo |

El modelo completo (35 campos) figura en el anexo H y es la interfaz prevista con
cualquier implementación posterior en hoja de cálculo o base de datos.

---

## 4.12 El Gate de aceptación

**[MODELO]** Ninguna cartera construida con PMMA se considera aceptada hasta superar diez
preguntas, cada una respondida con evidencia y no con adjetivos:

| # | Gate | Pregunta |
|---|---|---|
| 1 | **Mandato** | ¿Está perfectamente definido el objetivo? |
| 2 | **Función** | ¿Cada posición tiene un trabajo identificable? |
| 3 | **Arquitectura** | ¿Los pesos de los módulos responden al objetivo? |
| 4 | **Diversificación** | ¿Existen realmente distintas fuentes de comportamiento? |
| 5 | **Solapamiento** | ¿Estamos duplicando riesgos sin saberlo? |
| 6 | **Riesgo** | ¿Conocemos volatilidad, drawdown y concentraciones? |
| 7 | **Liquidez** | ¿Podemos ejecutar el plan cuando sea necesario? |
| 8 | **Coste** | ¿La complejidad adicional justifica sus costes? |
| 9 | **Ejecución** | ¿Existen reglas de aportación y rebalanceo? |
| 10 | **Comportamiento** | ¿Mantendríamos esta cartera en un escenario realmente adverso? |

Una cartera que no supere alguna pregunta necesita revisión antes de ser seleccionada.
La implementación de este trabajo pasa explícitamente por el Gate en el capítulo 26, con
la evidencia acumulada en las Partes III a V — incluidas las preguntas donde la respuesta
honesta es hoy incompleta.

---

## 4.13 Gobernanza y escalabilidad

**[MODELO]** Diez principios condensan el método en reglas verificables. Los esenciales:
ninguna posición sin función; ningún módulo existe porque exista un producto atractivo;
función antes que ticker; un mismo activo no se contabiliza dos veces; el overlay no
modifica la contabilidad estructural; la reserva operativa no se confunde con la liquidez
estratégica; más productos no significan más diversificación; target y peso actual se
registran por separado; la arquitectura se valida mediante X-Ray; lo que no encaja
honestamente pasa por el Protocolo de Extensión.

**Escalabilidad.** El marco se declara aplicable desde una cartera simple de tres
posiciones hasta una estructura patrimonial multi-cuenta, añadiendo profundidad de
información (look-through, riesgo, divisas, consolidación) sin cambiar las siete funciones.
Esta afirmación debe leerse con precisión: **lo que este trabajo demuestra es la
aplicación completa a un mandato concreto** (nivel intermedio de esa escala) **y la
capacidad descriptiva del lenguaje sobre ocho arquitecturas ajenas** (capítulo 8).
La escalabilidad a estructuras patrimoniales complejas queda como extensión declarada,
no como resultado.

---

## 4.14 Limitaciones y falsabilidad

Un marco que no declara sus límites no es un método: es una marca. PMMA reconoce cuatro
limitaciones estructurales y un criterio de falsación.

**L1 — Subjetividad de la función dominante.** Dos analistas pueden clasificar el mismo
instrumento de forma distinta. El método la acota con cinco mecanismos —árbol de orden
fijo, pregunta de control por módulo, tesis registrada obligatoria, campo de confianza de
clasificación y segunda revisión en caso de ambigüedad— pero no la elimina. La
comparabilidad *entre analistas* no ha sido testada empíricamente y se declara como
extensión futura.

**L2 — Riesgo de racionalización ex post.** PMMA se desarrolló en paralelo a la cartera
que lo implementa; un lector escéptico puede sospechar que el marco describe lo que ya se
había decidido. Las defensas son el registro de decisiones fechado —que documenta el orden
real de las decisiones— y la validación sobre arquitecturas ajenas al proyecto (capítulo
8). Ambas mitigan; ninguna elimina la sospecha por completo, y así se declara.

**L3 — La separación funcional no es separación estadística — y no pretende serlo.** Que
dos posiciones cumplan funciones distintas no garantiza que se comporten distinto. La
propia implementación lo ilustra: determinadas parejas de posiciones presentan
correlaciones materialmente elevadas entre módulos y dentro de ellos *(cuantificado en el
capítulo 18)*. **Una correlación alta entre módulos no invalida por sí misma la
clasificación funcional**: el marco no promete independencia estadística; obliga a medirla
y a no confundir diversificación funcional con diversificación estadística. Donde ambas
divergen, la divergencia se declara y se decide con ese dato.

**L4 — El marco describe; no predice ni optimiza.** PMMA no es una predicción de mercado,
ni un optimizador, ni una garantía de rentabilidad o descorrelación futura. Es un sistema
de arquitectura, clasificación, documentación y control. Todo lo que promete es
trazabilidad; todo lo que no promete es alfa.

**Criterio de falsación.** **[MODELO]** Un marco descriptivo corre el riesgo de ser
infalsable: siempre «funciona» porque solo etiqueta. El claim central de PMMA es
**organizativo, de trazabilidad y de gobernanza** — y por tanto su falsación debe
evaluarse en ese terreno, no en el estadístico. El criterio principal es:

> **PMMA debe rechazarse como aportación si, frente a una clasificación convencional más
> sencilla (por clase de activo o por tipo de producto), no mejora materialmente:
> ① la reproducibilidad de la clasificación; ② la trazabilidad de las decisiones;
> ③ la identificación de duplicidades; ④ la separación función/vehículo;
> ⑤ la gobernanza de los cambios; ⑥ la auditabilidad del conjunto; y
> ⑦ la capacidad descriptiva sobre carteras heterogéneas.**

Cada dimensión es evaluable: ① y ⑦ mediante ejercicios de clasificación (capítulo 8 y
extensión inter-analista declarada en L1); ② a ⑥ mediante la comparación del expediente
que produce el método frente al que produce la alternativa convencional — este propio
trabajo, con su registro íntegro de decisiones, constituye el caso de prueba.

Como **test complementario, no como falsación principal**, se examina además si la
agrupación funcional aporta información sobre el comportamiento (correlaciones, respuesta
por régimen — capítulos 18 y 20). Este test puede arrojar resultados desfavorables en
partes de la cartera sin refutar el marco, por lo dicho en L3: la ausencia de separación
estadística es un dato que el método obliga a descubrir y declarar, no una promesa
incumplida.

---

## 4.15 Relación con los métodos existentes

La pregunta obligada es por qué construir un marco propio existiendo el asset allocation
clásico, el core-satellite, el factor investing y el risk parity. La respuesta honesta
tiene dos partes.

**Primera: PMMA no compite con ellos en su terreno.** No aporta una teoría de formación de
precios (como el factor investing, **[EVIDENCIA EXTERNA]** Fama-French; Asness et al.), ni
un principio de asignación por riesgo (como el risk parity, **[EVIDENCIA EXTERNA]**
Bridgewater, *The All Weather Story*), ni una estructura núcleo-satélite de gestión.
Cada uno de esos marcos puede convivir con PMMA: de hecho, la implementación de este
trabajo usa factor investing *dentro* del módulo Aceleración y una lógica núcleo-satélite
*dentro* del macrobloque de gobernanza.

**Segunda: lo que PMMA aporta es integración explícita, no piezas inéditas.** La práctica
profesional dispone de elementos equivalentes —los roles de cartera de las plataformas de
análisis, las políticas de inversión institucionales (IPS), la construcción por objetivos
(**[EVIDENCIA EXTERNA]** goals-based investing; Swensen, *Unconventional Success*, como
antecedente de asignación por función)—. **PMMA no sostiene que estas piezas sean
inexistentes en otros marcos; propone integrarlas explícitamente dentro de un único flujo
operativo y documentado**: un lenguaje único (siete funciones, dos dimensiones, tres
vistas, dos modos de análisis), un procedimiento de clasificación con orden fijo y
protocolo de excepciones, un modelo de datos que lo hace operable y un gate que lo hace
exigible — demostrado sobre una implementación real con su registro de decisiones íntegro.

Dicho sin defensa: con otros siete nombres, el método funcionaría igual.

> **La aportación de PMMA no reside en la originalidad nominal de los módulos, sino en
> las separaciones que formaliza entre mandato, función, exposición, instrumento, modo de
> gestión, riesgo, ejecución y control; y en que esas separaciones quedan documentadas y
> son posteriormente auditables.**

---

## 4.16 Síntesis del capítulo

> **Los módulos no representan productos. Representan trabajos que el capital debe
> realizar.** Una cartera puede usar todos los módulos o solo algunos. Los módulos
> proporcionan el lenguaje; el mandato determina los pesos; los productos implementan la
> estrategia; el X-Ray verifica el resultado; y las reglas de seguimiento lo mantienen en
> el tiempo.

Los capítulos 5 a 7 desarrollan las piezas instrumentales aquí introducidas; el capítulo 8
somete el lenguaje a la prueba de describir ocho arquitecturas ajenas; el capítulo 9 reúne
las limitaciones; y la Parte II muestra la cadena completa aplicada, decisión a decisión,
a *Peaky Minders Global 10Y*.

---

## CIERRE DEL CAPÍTULO — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes |
|---|---|---|---|---|
| D75 *(arquitectura modular v1.0)* · D78 *(Management Mode, política/capital de la Reserva, vistas analíticas, mapa módulo→régimen como hipótesis)* · D63 *(gestión activa delegada)* · D50 *(Reserva)* · D48 *(macrobloque 47%)* | Correlaciones materialmente elevadas en Aceleración *(valores exactos pendientes del cap. 18, con ventana, frecuencia, fuente y fecha)* · registro D1-D78 como prueba del orden de decisión · conciliación real-vs-proxy *(D77)* como origen de 4 de los 9 campos añadidos | Subjetividad inter-analista **no testada** *(L1)* · desarrollo paralelo marco-cartera *(L2)* · separación funcional ≠ estadística, **declarada sin que invalide la clasificación** *(L3)* · marco descriptivo, no predictivo *(L4)* · mapa módulo→régimen **sin validar hasta el cap. 19** · linealidad del look-through **solo para exposiciones aditivas** · escalabilidad a family office **declarada, no demostrada** | ① Esquema de 3 capas *(módulos / Conviction Overlay / Execution Layer)* ② Árbol de clasificación de 8 preguntas ③ Tablero del Gate *(10 semáforos)* ④ Las tres vistas analíticas de la misma cartera ⑤ Cadena OBJETIVO→CONTROL ⑥ Cuadrante módulo→régimen *(marcado «hipótesis de diseño»)* | 🔴 SPIVA Persistence Scorecard *(persistencia débil)* · 🔴 Kahneman / Montier *(sesgo retrospectivo)* · 🟠 Fama-French y Asness et al. *(primas factoriales)* · 🟠 Bridgewater *All Weather Story* *(risk parity)* · 🟠 Swensen *Unconventional Success* *(asignación funcional)* · 🟡 literatura goals-based investing · 🟡 documentación Morningstar sobre roles de cartera |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | Borrador v1 completo — 16 secciones |
| 2026-08-13 | **Borrador v2 tras auditoría.** Aplicadas las 10 correcciones: tres vistas analíticas *(Total Capital · Strategic Allocation · Governance/Funding)* sustituyen a las dos vistas contables; falsación principal reescrita sobre el claim organizativo con la separación estadística como test complementario; árbol reescrito para preguntar por función dominante *(P1-P3 reformuladas; ambiguos sin clasificación automática)*; Management Mode como dimensión general y Conviction Overlay como término reservado *(Robeco y PIMCO son posiciones estructurales, no overlay)*; «vistas contables» → «vistas analíticas»; linealidad del look-through acotada a exposiciones aditivas; sobreafirmaciones suavizadas; referencias internas corregidas *(§4.11, §4.9, §4.14)*; correlaciones exactas sustituidas por formulación provisional hasta el cap. 18; cierre de §4.15 sustituido por la formulación aprobada. Auditoría superada |
| 2026-08-13 | ✅ **CERRADO v2 (D79).** Commit de sincronización: término **47% Governance Funding Pool**, Strategic Allocation View sin equivalencia estricta con el X-Ray, ejemplo explícito de doble vista tras compra de Convicción. **Sin más cambios conceptuales.** La v1 se conserva como trazabilidad |
