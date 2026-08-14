# 🩹 PARCHE P-4 — ✅ **EJECUTADO**

## Defensivos: acotar la lectura a una sola celda · 14 de agosto de 2026

> ✅ **EJECUTADO el 14-ago-2026 (D102).** Tres ediciones: **una celda de Defensivos**,
> **«filas» → «celdas»** en el encabezado y **la nota**, con «recibieron apoyo» en lugar de
> «mantuvieron apoyo» para usar exactamente el lenguaje del capítulo 19. **P-5 y P-6 sin
> ejecutar.**

---

# 1. Por qué P-4 es distinto de P-1, P-2 y P-3

Es **el primer parche que retira una sola celda**, no una fila entera. Y ése es exactamente
el principio de intervención mínima: **se retira lo que no se sostiene, no lo que está al
lado**.

| Parche | Alcance | Motivo |
|---|---|---|
| P-1 · Aceleración | Fila completa | Sin apoyo como lectura de régimen |
| P-2 · Motor | Fila completa | Lectura direccional no respaldada |
| P-3 · Freno | Fila completa | **No evaluable** |
| **P-4 · Defensivos** | **Una celda** | **Resultado no estable entre clasificadores** |

---

# 2. El cambio propuesto

## 🔹 CAMBIO 1 · La fila «Defensivos» *(línea 152)*

**ANTES** *(verbatim)*:

```
| Defensivos | favorable | mixto | mixto | **menos adverso** |
```

**DESPUÉS** *(propuesto)*:

```
| Defensivos | favorable | mixto | mixto | — |
```

**Mapeo de las cuatro columnas y qué se hace con cada una:**

| Columna | Equivale a | Dice hoy | Qué encontró el cap. 19 | Decisión P-4 |
|---|---|---|---|---|
| **Crecim.↑ Infl.↓** | caja 1 | favorable | — *(H2 no se formuló sobre crecimiento fuerte)* | ✅ **No se toca** |
| **Crecim.↑ Infl.↑** | caja 2 | mixto | — *(ídem)* | ✅ **No se toca** |
| **Crecim.↓ Infl.↑** | caja 4 | **mixto** | **Apoyo estable con los dos clasificadores** *(consumo y salud)* | ⚠️ **NO se mejora la etiqueta.** Ver §2.1 |
| **Crecim.↓ Infl.↓** | caja 3 | **menos adverso** | **Resultado inestable**: el proxy que cumplía cambiaba al cambiar el criterio | 🔴 **Se retira** |

## 2.1 La decisión más delicada: no premiar la celda que sí salió bien

**La celda de crecimiento débil + inflación alta se queda como «mixto» aunque el capítulo 19
encontrara apoyo estable.** El motivo es metodológico y conviene que quede escrito: mejorar
`mixto → favorable` después de conocer el resultado **sería contrario al mismo principio de
evitar el ajuste retrospectivo que inspira R8** — no una violación literal de R8, que rige
sobre las reglas de clasificación del capítulo 19 y no sobre las etiquetas de este mapa. Se
retira lo que no se sostiene; **no se recompensa lo que sí, porque el mapa sigue siendo un
mapa de diseño, no un cuadro de resultados.**

*(Ese reconocimiento del apoyo empírico es precisamente lo que P-6 propone canalizar con una
columna específica de nivel de apoyo — no retocando las etiquetas de diseño.)*

## 🔹 CAMBIO 2 · Párrafo nuevo en la nota bajo la tabla

Se insertaría **el último**, tras el párrafo del Freno *(orden actual de las notas:
Motor → Aceleración → Freno → **Defensivos**)*. **Texto propuesto, con tu formulación:**

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

# 3. 🔴 El encabezado sí necesita ajuste — y tenías razón al preguntarlo

**Texto vigente** *(tras P-3)*:

> **Las filas que aparecen sin valor** son aquellas cuya lectura por régimen no recibió apoyo
> suficiente en esa prueba, o no pudo contrastarse con la evidencia disponible; **las filas
> que conservan valores** siguen expresando hipótesis de diseño, no resultados históricos
> medidos.

**El problema:** hasta ahora todas las retiradas eran **filas completas**, y el encabezado
está escrito en términos de filas. **Defensivos sería la primera fila mixta** — tres celdas
con valor y una vacía. Con el texto actual, esa fila **no cae en ninguna de las dos
categorías** que el encabezado describe: ni «aparece sin valor», ni «conserva valores» sin
más.

**Ajuste mínimo propuesto — dos palabras:**

> **Las celdas que aparecen sin valor** son aquellas cuya lectura por régimen no recibió
> apoyo suficiente en esa prueba, o no pudo contrastarse con la evidencia disponible; **las
> celdas que conservan valor** siguen expresando hipótesis de diseño, no resultados
> históricos medidos.

**Por qué funciona sin más cambios:** «celda» cubre **los dos casos a la vez** — una fila
entera vacía es simplemente el caso en que **todas** sus celdas se retiraron, y sigue siendo
cierto para Motor, Aceleración y Freno. **No hay que añadir ninguna frase nueva.**

⚠️ **No ejecutado.** Si prefieres una alternativa —por ejemplo mantener «filas» y añadir una
frase sobre retiradas parciales— es más texto para el mismo efecto; **recomiendo el cambio
de dos palabras**.

---

# 4. Frases verificadas que **NO** quedan incoherentes

| Elemento | Línea | Por qué se mantiene |
|---|---|---|
| **Función de Defensivos** — *«Mantener exposición productiva reduciendo sensibilidad al ciclo»* | 115 | Es una función, no una afirmación por régimen. **Intacta** |
| **Pregunta de control** — *«¿Mantiene exposición empresarial pero pretende mejorar el comportamiento relativo en escenarios adversos?»* | 115 | 🟡 **Verificada, y merece una línea:** está formulada como **intención** *(«pretende»)*, no como resultado, y por eso **sobrevive sin cambio**. El capítulo 19, además, **encontró apoyo** en el escenario adverso con inflación alta — así que ni siquiera queda en tensión con los datos |
| *«El mismo ETF comprado deliberadamente para reducir la ciclicidad cumple una función defensiva»* | 86-87 | Ilustra el **Principio de Función Dominante**: instrumento idéntico, función distinta. Sin régimen |
| *«La calidad puede ser Defensivos si se compra por resiliencia…»* | 137 | Regla de **clasificación por tesis** |
| **El caso *quality* en el árbol** *(P5 Defensivos / P6 Aceleración)* | 392-394 | Ilustra el **orden** del árbol, no el comportamiento por clima |
| Árbol de clasificación → P5 Defensivos | 366 | Clasifica por función |
| *«Un fondo puede contener internamente sectores defensivos»* | 305 | Es **modo de construcción** *(look-through)*, no régimen |
| Criterio de falsación | 499-510 | **Organizativo** |
| Las tres filas restantes *(Emergentes, Activos Reales, Asimetría)* | 153-155 | **Corresponden a P-5 y siguientes. No autorizados** |

**Ni pesos ni vehículos:** el capítulo 4 no contiene ninguno *(verificado en P-1, P-2 y P-3)*.

---

# 5. Alcance exacto si apruebas

| | |
|---|---|
| **Ediciones en el cap. 4** | **2** *(una celda de la fila + párrafo en la nota)*, **o 3** con el ajuste del encabezado §3 |
| **No se toca** | Función y pregunta de control de Defensivos · las **tres celdas restantes** de su fila · el caso *quality* · el árbol · el criterio de falsación · las otras tres filas del mapa |
| **No se abre** | **P-5 y P-6** |
| **Capítulo 19** | **Cerrado, no se toca** |

## 5.1 Reglas que el texto propuesto cumple

✅ Intervención mínima: **una sola celda** · ✅ **no se mejora retrospectivamente** ninguna
etiqueta · ✅ las dos cajas de crecimiento fuerte **no se reinterpretan**, porque H2 se
formuló sobre crecimiento débil · ✅ no cambia función, pregunta de control, pesos ni
vehículos · ✅ el detalle empírico se remite al capítulo 19.

**Estado: ✅ EJECUTADO (D102).** Encabezado ajustado a «celdas» dentro de P-4. Para **P-6**
quedan la tabla resumen final y la futura columna de nivel de apoyo empírico.
