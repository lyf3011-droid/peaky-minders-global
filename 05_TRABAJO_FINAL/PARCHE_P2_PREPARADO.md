# 🩹 PARCHE P-2 — ✅ **EJECUTADO**

## Motor: reformular su lectura por régimen · 14 de agosto de 2026

> ✅ **EJECUTADO el 14-ago-2026 (D100)**, con las dos decisiones tomadas: **nota sin cifra**
> y **ajuste del encabezado dentro de P-2**. **P-3 a P-6 sin ejecutar.**

---

# 1. Qué dice hoy el capítulo 4 y qué encontró el capítulo 19

**Fila actual** *(línea 149)*:

```
| Motor | **favorable** | mixto | adverso | adverso |
```

**Las columnas del mapa, mapeadas contra los resultados** *(rentabilidad real anualizada,
cap. 19 §19.10.1)*:

| Columna del mapa | Equivale a | Dice el cap. 4 | Midió el cap. 19 | Veredicto |
|---|---|---|---:|---|
| **Crecim.↑ Infl.↓** | caja 1 | **favorable** | **+9,83%** | ✅ **Compatible** — la celda no era incorrecta |
| **Crecim.↑ Infl.↑** | caja 2 | mixto | **+5,54%** | ✅ Compatible |
| **Crecim.↓ Infl.↑** | caja 4 | adverso | **+0,95%** | ✅ **Confirmado — es la peor** |
| **Crecim.↓ Infl.↓** | caja 3 | **adverso** | **+15,76%** | 🔴 **CONTRADICCIÓN DIRECTA — calificada de adversa, resultó la más favorable** |

> **Diagnóstico calibrado.** **La contradicción directa está en una sola celda: crecimiento
> débil + inflación baja**, calificada de adversa y que resultó la más favorable. **La celda
> «favorable» de crecimiento fuerte + inflación baja no era incorrecta** y no se corrige por
> no haber sido la mejor. **Lo que impide mantener el mapa es el resultado conjunto:** la
> lectura general *«crecimiento fuerte favorable / crecimiento débil adverso»* deja de
> sostenerse cuando uno de los dos climas de crecimiento débil resulta el más favorable de
> los cuatro. Lo único que la prueba respalda sin matices es que **el peor clima para el
> Motor fue crecimiento débil + inflación alta**.

---

# 2. El cambio propuesto

## 🔹 CAMBIO 1 · La fila «Motor» *(línea 149)*

**ANTES** *(verbatim)*:

```
| Motor | **favorable** | mixto | adverso | adverso |
```

**DESPUÉS** *(propuesto)*:

```
| Motor | — | — | — | — |
```

*(Mismo tratamiento que P-1: guiones en las cuatro celdas y la explicación completa abajo.
Evita la ambigüedad de formato ya detectada y no introduce una jerarquía que los datos no
sostienen.)*

## 🔹 CAMBIO 2 · Ampliar la nota existente bajo la tabla

La nota creada por P-1 pasaría a cubrir los dos módulos. **Texto propuesto para el párrafo
nuevo**, que se insertaría **antes** del párrafo de Aceleración:

> **[MODELO — actualizado tras el capítulo 19]** **La fila del Motor aparece sin valor en
> las cuatro columnas.** La prueba histórica del capítulo 19 **no respalda la lectura
> direccional que este mapa proponía**: el mejor comportamiento real del Motor no se
> observó con crecimiento fuerte, sino **con crecimiento débil e inflación baja**, que la
> tabla anterior calificaba de adverso. Lo único que la prueba sostiene con claridad es que
> **el Motor obtuvo su peor comportamiento real con crecimiento débil e inflación alta**.
>
> ⚠️ **No se sustituye una lectura direccional por otra.** El análisis empareja
> macroeconomía y rentabilidad del **mismo trimestre**, de modo que mide **coincidencia, no
> causa**; las explicaciones posibles quedan registradas en el capítulo 19 §19.13 *(C-1)*
> **como hipótesis interpretativas, no adoptadas**.

### ⚠️ Decisión que necesito de ti: ¿la nota lleva la cifra?

La propuesta original *(`PROPUESTA_PARCHES_CAP4.md`)* incluía **«(+0,95% real)»**. **El
capítulo 4 no publica cifras**: es un capítulo de método, y por eso habla de *«correlaciones
materialmente elevadas»* remitiendo los valores exactos al capítulo 18. Dos opciones:

| | Opción |
|---|---|
| **A** *(la del texto de arriba)* | **Sin cifra**, remitiendo al capítulo 19. **Respeta la convención del capítulo 4** |
| **B** | **Con cifra** *(«+0,95% real anualizado»)*. Más concreto, pero rompe la convención del capítulo |

**Recomendación: A.** El capítulo 4 describe método; los números viven en la Parte IV.

---

# 3. 🔴 Frases que quedarían necesariamente incoherentes

## 3.1 El encabezado del mapa *(líneas 141-145)* — **incoherencia real, ya activa**

**Texto actual**:

> **[MODELO — hipótesis de diseño, no evidencia validada]** Como referencia de diseño, cada
> módulo lleva asociado un comportamiento *esperado* por régimen económico (crecimiento ×
> inflación). Este mapa se presenta aquí únicamente como intención de cobertura; su
> desarrollo, datación histórica y validación cuantitativa **corresponden al capítulo 19, y
> hasta ese capítulo ninguna celda debe leerse como resultado medido**:

**Por qué queda incoherente:** el capítulo 19 **ya existe y está cerrado**. La frase habla
en futuro de algo que ya ocurrió, y afirma que ninguna celda debe leerse como resultado
medido **cuando dos filas ya remiten a resultados medidos**.

⚠️ **Esta incoherencia no la crea P-2: la creó P-1** y P-2 la agrava. **Ajuste mínimo
propuesto** *(solo la parte temporal, sin añadir columna de apoyo empírico — eso es P-6)*:

> …su desarrollo, datación histórica y contraste cuantitativo **se realizaron en el
> capítulo 19**; **las filas sin valor son aquellas cuya lectura por régimen no recibió
> apoyo suficiente en esa prueba**, y las que conservan valor **siguen siendo hipótesis de
> diseño, no resultados medidos**.

**Necesito que decidas si este ajuste entra en P-2 o se difiere a P-6.** Sin él, el capítulo
queda con una frase que se contradice con sus propias filas.

## 3.2 La tabla resumen final *(línea 562)* — **incoherencia menor, territorio de P-6**

Dice: *«mapa módulo→régimen **sin validar hasta el cap. 19**»*. Con el capítulo 19 cerrado y
dos filas actualizadas, la formulación queda desfasada. **Corresponde a P-6** *(columna de
nivel de apoyo empírico)* y **no se toca en P-2**.

## 3.3 Lo que NO queda incoherente — verificado

| Elemento | Línea | Por qué no |
|---|---|---|
| **Función del Motor** *(«capturar el crecimiento económico y empresarial de largo plazo»)* | 114 | Es una función de **largo plazo**, no una afirmación por régimen. **Sin cambio** |
| Pregunta de control del Motor | 114 | Ídem |
| *«El Motor no es un índice mundial; es la función de capturar crecimiento agregado»* | 124 | Distinción función/producto, sin régimen |
| Motor como núcleo indexado *(forma de gestión ①)* | 183 | Forma de gestión |
| Bolsa del 47% · Motor ordinario · Convicción | 251-260 | Gobernanza, sin régimen |
| Árbol de clasificación → Motor | 336-345, 360 | Clasifica por función |
| **Criterio de falsación** | 499-510 | Es **organizativo**, no estadístico: no depende del mapa |
| Emergentes «modificable independientemente del Motor» | 117 | Relación estructural, no régimen |

---

# 4. Alcance exacto si apruebas

| | |
|---|---|
| **Ediciones en el cap. 4** | **2** *(fila del Motor + párrafo nuevo en la nota)*, **o 3** si incluyes el ajuste del encabezado §3.1 |
| **No se toca** | Función, pregunta de control, pesos *(no están en el cap. 4)*, vehículos, **las otras cinco filas del mapa** *(Defensivos, Emergentes, Freno, Activos Reales, Asimetría)*, el criterio de falsación y todo lo de §3.3 |
| **No se abre** | **P-3, P-4, P-5 y P-6** |
| **Capítulo 19** | **Cerrado, no se toca** |

**Estado: ✅ EJECUTADO (D100).** Decisiones aplicadas: **nota sin cifra** *(opción A)* ·
**encabezado corregido dentro de P-2**. Para **P-6** quedan la tabla resumen final y la
futura columna de nivel de apoyo empírico.
