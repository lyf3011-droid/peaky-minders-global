# 🧬 AUDITORÍA DE VERSIONADO — CARTERA OFICIAL ↔ BASE DEL LABORATORIO

## 15 de agosto de 2026 · genealogía reconstruida con evidencia

> **Nada modificado.** Ni cartera, ni capítulos, ni fuente de verdad, ni Dxx, ni PMMA.
> **No se han ejecutado pruebas X-Ray, ni validación histórica, ni R-1 a R-6.**

---

# 0. Las tres entidades, separadas *(regla de autoridad)*

| | Entidad | Qué es | Documento |
|---|---|---|---|
| **A** | **CARTERA OFICIAL DOCUMENTADA** | Última versión formalmente aprobada en el Investment Book | `CARTERA_V1_0_FUENTE_DE_VERDAD.md` + `XRAY_OFICIAL_2026-08-13.md` |
| **B** | **BASE OPERATIVA DEL LABORATORIO** | Cartera real sobre la que se ejecutaron **todos** los X-Rays | `mi_cartera.txt` *(«PEAKY MINDERS GLOBAL v10»)* |
| **C** | **CANDIDATA FINAL** | B + India + commodities | `CARTERA_GANADORA.txt` · X-Ray 34 |

**A partir de aquí no se mezclan.** Que **B** no se hubiera propagado a **A** no invalida las
pruebas hechas entre **B** y **C**.

---

# 1. Cronología reconstruida — con marcas de tiempo verificables

| Momento | Evento | Evidencia |
|---|---|---|
| **11-ago** | AXA Trésor entra en el catálogo **con una advertencia**: *«Ojo: se usa como liquidez pero por dentro es 57% bonos y 29% otros, no efectivo puro»* | `catalogo.json`, campo `fecha_dato: 2026-08-11` |
| **13-ago** | **SPDR Global Aggregate se cataloga con análisis detallado**: composición por tipo de emisor, geografía, **⚠️ clase de distribución** y **⚠️ «2022: −13,16%»** | `catalogo.json`, `fecha_dato: 2026-08-13` |
| **14-ago 01:10** | **Commit del X-Ray oficial** con **Freno = AXA 6,19 + PIMCO 3,09** | `git 9c590da` |
| **14-ago 12:09** | **Commit de la fuente de verdad v1.0** con el mismo Freno | `git 138aaae` *(D85)* |
| **14-ago 17:46** | 🔴 **Se fija `mi_cartera.txt` v10 con SPDR 9,28 sustituyendo a AXA+PIMCO** | `mtime` del archivo |
| **14-ago 19:53** | **Primer X-Ray del laboratorio** *(`00_BASE-v10`)* | `mtime` del PDF |
| **14-ago 19:53 → 15-ago 02:19** | Las 33 pruebas restantes | `mtime` de los 35 PDF |

> ### ⏱️ **La BASE se fijó 2 horas y 7 minutos ANTES del primer X-Ray, y no se tocó después.**
> **[RESULTADO]** El archivo `mi_cartera.txt` no ha vuelto a modificarse desde las 17:46 del
> 14-ago, mientras los X-Rays se generaron entre las 19:53 y las 02:19. **La baseline es
> anterior a todos los resultados.**

## 1.1 Matiz importante sobre «desfase documental»

**[DATO]** La documentación oficial **no estaba desactualizada por antigüedad**: el X-Ray
oficial se comprometió a la **01:10** y la fuente de verdad a las **12:09 del mismo día**.
El cambio del Freno se produjo **5 horas y 37 minutos después** de la fuente de verdad.

**[INTERPRETACIÓN]** No es una deriva de semanas sin propagar: es **un cambio operativo del
mismo día, posterior a la documentación y no comunicado**. Eso no lo hace ilegítimo —pero
sí cambia la etiqueta: **no es «documentación vieja», es «decisión nueva sin registrar»**.

---

# 2. GENEALOGÍA COMPLETA — todos los cambios, no solo el Freno

**Referencia usada: el X-Ray oficial del 13-ago** *(`XRAY_OFICIAL_2026-08-13.md`)*, porque es
**la fotografía medida** de la cartera oficial, no su descripción. Pesos en columna X-Ray
*(normalizada al 97%)* para que sean directamente comparables.

| Elemento | Cartera anterior *(A)* | BASE v10 *(B)* | Cambio | Evidencia / fecha | ¿Deliberado? | Estado |
|---|---|---|---|---|---|---|
| **Motor · S&P 500** | `IE00B5BMR087` **23,00** | `IE00B5BMR087` **23,00** | **Ninguno** | X-Ray oficial + `mi_cartera.txt` | — | ✅ **Idéntico** |
| **Motor · All-World** | `IE00BK5BQT80` **22,36** | `IE00BK5BQT80` **22,36** | **Ninguno** | Ídem. El reparto interno **50,7/49,3** está **explícito en el X-Ray oficial** | — | ✅ **Idéntico** |
| **Defensivos · consumo** | `IE00BM67HN09` 6,19 | `IE00BM67HN09` 6,19 | Ninguno | Ídem | — | ✅ Idéntico |
| **Defensivos · salud** | `IE00B43HR379` 6,19 | `IE00B43HR379` 6,19 | Ninguno | Ídem | — | ✅ Idéntico |
| **Aceleración · Robeco** | `LU0203975437` 4,12 | `LU0203975437` 4,12 | Ninguno | Ídem | — | ✅ Idéntico |
| **Aceleración · multifactor** | `IE00BZ0PKV06` 4,12 | `IE00BZ0PKV06` 4,12 | Ninguno | Ídem | — | ✅ Idéntico |
| **Aceleración · small caps** | X-Ray usó **SPDR** `IE00BCBJG560` *(proxy D77)* | **Vanguard** `IE00B42W4L06` **(el vehículo real)** | 🟢 **El laboratorio usa el REAL en vez del proxy** | Fuente de verdad §2.2 · `mi_cartera.txt` | ✅ Sí | 🟢 **MEJORA sobre A** |
| **Activos reales · oro** | X-Ray usó **clase estándar** `JE00B1VS3770` *(proxy)* | **Core** `JE00BN2CJ301` **(el real)** | 🟢 **El laboratorio usa el REAL** | Fuente de verdad §2.3 | ✅ Sí | 🟢 **MEJORA sobre A** |
| **Activos reales · cobre** | X-Ray usó **EUR Daily Hedged** *(proxy)* | `GB00B15KXQ89` **sin cubrir (el real)** | 🟢 **El laboratorio usa el REAL** — y era **la única divergencia que cambiaba el comportamiento** según la propia fuente de verdad | Fuente de verdad §2.4 | ✅ Sí | 🟢 **MEJORA sobre A** |
| **Asimetría · bitcoin** | `CH1199067674` 4,12 | `CH1199067674` 4,12 | Ninguno | Ídem | — | ✅ Idéntico |
| **Emergentes** | Real: clase **S** `IE000QAZP7L2` · X-Ray del libro: clase **D** `IE00BYWYCC39` | **Instl** `IE00B3D07F16` | 🟡 **Proxy distinto del mismo fondo** | `mi_cartera.txt` **lo documenta en el propio archivo**, invoca **la regla D77** y explica que la clase S no tiene serie histórica | ✅ **Sí, y por escrito** | 🟡 **Proxy documentado — tres clases circulando** |
| **⚓ FRENO** | **AXA `FR0000447823` 6,19 + PIMCO `IE00B84J9L26` 3,09** | **SPDR `IE00BF1QPL78` 9,28** | 🔴 **CAMBIO SUSTANTIVO de instrumentos** | Catálogo con análisis del SPDR fechado **13-ago** · sustitución el **14-ago 17:46** · **ningún Dxx** *(verificado: `IE00BF1QPL78` aparece 0 veces en `ESTADO.md`)* | ⚠️ **Probablemente sí** *(ver §3)* | 🔴 **Decisión operativa de laboratorio pendiente de propagación documental** |
| **Reserva** | 3,00 fuera del informe | 3,00 fuera del informe | Ninguno | Ídem | — | ✅ Idéntico |

## 2.1 Recuento — la divergencia es **una**, no varias

| Categoría | Nº | Posiciones |
|---|---:|---|
| ✅ **Idénticas** | **8** | S&P, All-World, ambos defensivos, Robeco, multifactor, bitcoin, reserva |
| 🟢 **El laboratorio usa el vehículo REAL donde el libro usaba proxy** | **3** | Small caps, oro, cobre |
| 🟡 **Proxy distinto, documentado en ambos lados** | **1** | Emergentes |
| 🔴 **Divergencia sustantiva** | **1** | **Freno** |

> ### **Conclusión de la genealogía: la BASE v10 no es «otra cartera». Es la cartera oficial
> ### con UN cambio de instrumento en el Freno — y con tres posiciones donde el laboratorio
> ### es MÁS fiel a la realidad que el propio X-Ray oficial del libro.**

**Esto rebaja materialmente el alcance de H-1 tal como lo formulé en la v1 de la auditoría.**

---

# 3. ¿Fue deliberado el cambio del Freno? — evidencia a favor y en contra

## 3.1 A favor de que fue deliberado

| # | Evidencia | Fuerza |
|---|---|---|
| **1** | **El SPDR se catalogó el 13-ago con análisis detallado**: 10.369 bonos, desglose por tipo de emisor y geografía, aviso de clase de distribución y **aviso explícito de «2022: −13,16%»**. **Nadie documenta así un vehículo que no está considerando** | 🟢 Alta |
| **2** | **AXA llevaba desde el 11-ago una advertencia en el catálogo**: *«se usa como liquidez pero por dentro es 57% bonos y 29% otros, no efectivo puro»*. **Hay un motivo documentado y anterior para no usarlo como Freno puro** | 🟢 Alta |
| **3** | **AXA sigue en el catálogo**: no se borró ni se descartó — se dejó de usar. Es coherente con una elección, no con un olvido | 🟠 Media |
| **4** | **La sustitución es limpia**: 6,19 + 3,09 = 9,28 exactos. **El peso del módulo se conserva al céntimo** | 🟢 Alta |
| **5** | **`mi_cartera.txt` documenta escrupulosamente el otro proxy** *(Emergentes, con la regla D77 citada)*. Quien documenta un proxy y no el otro **probablemente no lo considera un proxy**, sino el vehículo elegido | 🟠 Media |

## 3.2 En contra / lo que falta

| # | Hueco |
|---|---|
| **1** | 🔴 **No existe ningún Dxx**, nota, comentario ni línea de registro que diga «se sustituye el Freno». **Verificado**: `IE00BF1QPL78` aparece **0 veces** en `ESTADO.md` |
| **2** | 🔴 **`mi_cartera.txt` no lleva nota explicativa en la línea del Freno**, a diferencia de Emergentes, que sí la lleva |
| **3** | 🟠 **PIMCO desaparece sin rastro**: `IE00B84J9L26` **no aparece en ningún archivo del laboratorio**, ni siquiera en el catálogo |
| **4** | 🟠 **El cambio se produjo 5h37m después de commitear la fuente de verdad** que decía lo contrario. No es deriva antigua: es divergencia del mismo día |
| **5** | 🟠 **Los tres documentos del laboratorio llaman «Freno · bonos globales» al bloque** y razonan sobre él como si fuera renta fija agregada — **coherente internamente, pero incompatible con la descripción oficial** |

## 3.3 Veredicto sobre la deliberación

> **[INTERPRETACIÓN]** **Hay evidencia razonable de que el cambio fue deliberado** —el
> análisis del SPDR fechado el día anterior y la advertencia sobre AXA son difíciles de
> explicar de otro modo—, **pero no hay evidencia directa de la decisión**, y **el motivo es
> reconstruido, no documentado**.
>
> **Clasificación:** **decisión operativa de laboratorio pendiente de propagación
> documental**, con **motivo plausible reconstruido pero no declarado**.

⚠️ **Lo que NO puedo afirmar:** que el cambio se hiciera *por una razón de inversión*
*(p. ej. sustituir un monetario impuro por un agregado global)* frente a *por comodidad de
medición* *(el SPDR tiene serie X-Ray larga y limpia; un monetario francés y un fondo
PIMCO clase E podrían no tenerla)*. **Son dos motivos muy distintos y solo tú puedes
decir cuál fue.**

---

# 4. ¿Es BASE v10 una baseline metodológicamente válida?

| Criterio exigido | Evidencia | Cumple |
|---|---|---|
| **Fijada antes de ejecutar las pruebas** | `mi_cartera.txt` a las **17:46**; primer X-Ray a las **19:53**; sin modificaciones posteriores | ✅ **Sí, con marca de tiempo** |
| **Cambios deliberados respecto a la anterior** | Análisis del SPDR el 13-ago + advertencia sobre AXA el 11-ago | 🟡 **Probable, no probado** |
| **No modificada retrospectivamente para favorecer resultados** | **`mtime` congelado en 17:46** frente a 35 informes generados después. **Es la prueba más fuerte del expediente** | ✅ **Sí** |
| **Reconstruible posición a posición** | ✅ **Reconstruida en §2**: 8 idénticas, 3 mejoras, 1 proxy documentado, 1 divergencia | ✅ **Sí** |

> ## 🟢 **BASE v10 ES UNA BASELINE METODOLÓGICAMENTE VÁLIDA.**
> **Fue fijada antes de los resultados, no se tocó después, y su composición es
> reconstruible al céntimo.** El laboratorio **es internamente válido respecto a su propia
> BASE**, y **G2 es un resultado válido dentro de ella**.

## 4.1 Lo que sigue sin poder afirmarse

**Que BASE v10 sea ya la cartera oficial.** Son dos preguntas distintas y solo la primera
está resuelta:

| Pregunta | Estado |
|---|---|
| **¿El experimento es válido dentro de BASE v10?** | 🟢 **Sí** |
| **¿BASE v10 debe convertirse en la cartera oficial?** | 🔴 **Decisión pendiente, no auditable con los datos** |
| **¿Commodities supera además la validación histórica independiente?** | 🔴 **Pendiente de §K** |

---

# 5. AUDITORÍA DEL 47% — ¿rompe realmente la reclasificación de Robeco?

**Tenías razón en pedir que lo auditara antes de declarar contradicción.**

## 5.1 Las tres posibilidades, evaluadas

| Hipótesis | ¿Qué implicaría? | Veredicto |
|---|---|---|
| **(a) Solo cambia la clasificación funcional de Robeco** | Ningún euro se mueve; cambia la etiqueta del módulo | ✅ **Cierto: es una reclasificación, no una asignación** |
| **(b) Cambia el peso económico del macrobloque** | El 47% pasaría a 51% | ❌ **Falso.** No entra ni sale capital. **El 47% es una identidad de gobernanza, no una suma de módulos** |
| **(c) Revela que la definición debe actualizarse** | El texto del cap. 5 no distingue los casos | 🟢 **Ésta es la correcta** |

## 5.2 Por qué (c) y no (b)

**[DATO]** El capítulo 5 define la bolsa como **«44 Motor ordinario + 3 Reserva + 0
Convicción = 47%»**, y el término clave es **«Motor ordinario»**, no «módulo Motor».

**[DATO]** El propio libro clasifica a Robeco como **posición estructural con forma de
gestión ③ *(activa delegada)***, explícitamente **no** como parte del flujo ordinario:
*«Robeco es capital del módulo Aceleración cuya administración se ha delegado en un gestor…
es una posición estructural con forma de gestión ③ — no una capa superpuesta»*.

**[INTERPRETACIÓN]** Si Robeco se reclasifica a Motor, pasa a ser **«Motor + activa
delegada»**. **Y «Motor ordinario» —el capital indexado que participa del flujo mensual y
de la bolsa de gobernanza— seguiría siendo 44.** Bajo esa lectura, **la identidad
47 = 44 + 3 + 0 se mantiene intacta**.

> ### 🟡 **No hay contradicción definitiva: hay una definición incompleta.**
> El capítulo 5 nunca tuvo que distinguir entre «módulo Motor» y «Motor ordinario» porque
> **hasta ahora coincidían**. La reclasificación de Robeco **es el primer caso que los
> separa** — y eso es un **hueco de definición**, no una ruptura del sistema.

**Corrección a mi propia auditoría:** en la v1 escribí que Motor 48% *«rompe»* la identidad.
**Es más preciso decir que la obliga a explicitarse.** Aplico aquí la máxima del propio
proyecto: *«la Convicción explica cómo se compró; el módulo explica para qué está»* — y
añado su corolario: **la bolsa del 47% explica cómo se gobierna, y no tiene por qué
coincidir con la suma de los módulos**.

**Lo que sigue haciendo falta antes de ejecutar:** **una decisión explícita** que fije si
«Motor ordinario» = capital indexado del Motor *(el 44 se mantiene)* o = módulo Motor
completo *(el 47 pasa a 51)*. **Es una decisión de una línea, no un rediseño.**

---

# 6. QUÉ NECESITARÍA FORMALIZARSE PARA CONVERTIR BASE v10 EN CARTERA OFICIAL

| # | Decisión a formalizar | Tipo | Bloquea a |
|---|---|---|---|
| **F-1** | **Sustitución del Freno: AXA 6% + PIMCO 3% → SPDR Global Aggregate 9%.** Con motivo declarado, fecha y **el efecto sobre la función del módulo** *(pasa de «monetario + renta fija flexible» a «renta fija agregada global»)* | 🔴 **Cambio de vehículo Y de exposición** *(nivel alto en la escala del cap. 10)* | Todo el laboratorio |
| **F-2** | **Cierre de la revisión de PIMCO por coste** *(pendiente desde D-a)*. **El laboratorio la resolvió de facto eliminándolo** — hay que decidirlo explícitamente, no por omisión | 🔴 Decisión pendiente ya identificada | F-1 |
| **F-3** | **Actualizar `CARTERA_V1_0_FUENTE_DE_VERDAD.md`** con los tres vehículos reales que el laboratorio ya usa *(Vanguard small caps, oro Core, cobre sin cubrir)* — **el libro los tiene como proxies en su X-Ray y el laboratorio usa los reales** | 🟢 Menor: es propagación, no cambio | — |
| **F-4** | **Fijar el proxy de Emergentes**: tres clases circulando *(`IE000QAZP7L2` real · `IE00BYWYCC39` proxy del libro · `IE00B3D07F16` proxy del laboratorio)*. **Elegir uno para X-Ray y declararlo** | 🟠 Media | Coherencia entre informes |
| **F-5** | **Definición de «Motor ordinario»** para la bolsa del 47% *(§5)* | 🟠 Media, una línea | Reclasificación de Robeco |
| **F-6** | **Regenerar el X-Ray oficial** con la composición aprobada, para que **A** y **B** vuelvan a coincidir | 🟠 Media | Caps. 15-18 |
| **F-7** | **Registrar BASE v10 como versión** *(v1.1 de la cartera)* con su fecha real: **14-ago 17:46** | 🟢 Menor | Trazabilidad |

## 6.1 Lo que **no** hace falta

**No hace falta repetir las 33 pruebas.** Son válidas dentro de su baseline, que está
fechada, congelada y es reconstruible. **Lo que hace falta es formalizar la baseline.**

⚠️ **Con una excepción, y es la de siempre:** si **F-1 se rechaza** y el Freno vuelve a
AXA+PIMCO, entonces **G2 sí habría que repetirlo** *(R-2 y R-3 de la auditoría)*, porque la
financiación del 1% de commodities saldría de instrumentos distintos. **Las demás pruebas
seguirían siendo válidas**, porque el Freno no interviene en ellas salvo por dilución.

---

# 7. RESUMEN

| Pregunta que hiciste | Respuesta |
|---|---|
| **Genealogía exacta** | §2 — **13 posiciones comparadas una a una** |
| **Todos los cambios** | **8 idénticas · 3 mejoras · 1 proxy documentado · 1 divergencia sustantiva** |
| **Cuáles están documentados** | El proxy de Emergentes *(con la regla D77 citada en el propio archivo)*. **Ninguno más** |
| **Deliberados pero no propagados** | **El Freno.** Evidencia indirecta sólida *(catálogo 13-ago + advertencia sobre AXA 11-ago + sustitución al céntimo)*, **sin decisión registrada** |
| **Que no puedo explicar** | **Por qué desapareció PIMCO sin dejar rastro** en ningún archivo del laboratorio · **y cuál fue el motivo real del cambio** *(inversión o comodidad de medición)* |
| **¿BASE v10 es baseline válida?** | 🟢 **Sí.** Fijada 2h07m antes del primer X-Ray, congelada desde entonces, reconstruible al céntimo |
| **Qué formalizar** | **F-1 a F-7** — encabezado por la sustitución del Freno y el cierre de PIMCO |

## 7.1 Reformulación final de H-1

> ## 🟠 **H-1 · Divergencia de versionado entre la cartera documental oficial y la BASE v10
> ## realmente usada en el laboratorio.**
>
> **El laboratorio es internamente válido respecto a su propia BASE v10**, que fue fijada
> antes de ejecutar las pruebas, no se modificó retrospectivamente y es reconstruible
> posición a posición. **G2 es un resultado válido dentro de BASE v10.**
>
> **Lo que todavía no puede afirmarse es que BASE v10 sea la cartera oficial definitiva.**
> La divergencia se reduce a **una posición —el Freno—** y a **un proxy de clase
> —Emergentes—**; en las otras tres diferencias **el laboratorio es más fiel a la realidad
> que el X-Ray oficial del libro**.
>
> **Acción:** formalizar F-1 a F-7. **No rehacer las 33 pruebas.**

---

**Estado:** auditoría de versionado completada. **Sin ejecutar R-1 a R-6, sin validación
histórica, sin tocar el Investment Book y sin abrir PMMA Universal.**
