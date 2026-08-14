# 🩹 PARCHE P-1 — ✅ **EJECUTADO**

## Aceleración: retirar la justificación por régimen · D98 · 14 de agosto de 2026

> ✅ **EJECUTADO el 14-ago-2026 (D99).** El capítulo 4 lleva las dos ediciones aplicadas y
> verificadas. **Trazabilidad de commits:** `d208500` es el **commit sustantivo de
> preparación (D98)**; `cca60da` es **únicamente la reparación posterior de un enlace del
> registro**, sin contenido sustantivo.

---

# 1. Qué se cambia — exactamente dos puntos del capítulo 4

## 🔹 CAMBIO 1 · La fila «Aceleración» del mapa módulo→régimen *(línea 151)*

**ANTES** *(texto actual, verbatim)*:

```
| Aceleración | **favorable** | mixto | adverso | adverso |
```

**DESPUÉS** *(ejecutado)*:

```
| Aceleración | — | — | — | — |
```

⚠️ **Cambio respecto a la propuesta inicial, por el control 1.** Se comprobó cómo renderiza
realmente el formato heredado de «Asimetría»: **el texto queda dentro de la primera columna
de régimen y las otras tres salen vacías**, de modo que **puede leerse como si la nota
afectara solo a «Crecim.↑ Infl.↓»**. Es ambiguo. Se adopta por tanto la alternativa
indicada: **`—` en las cuatro celdas y la explicación completa en la nota inferior**.

🟡 **Observación registrada, no ejecutada:** la fila «Asimetría» arrastra esa misma
ambigüedad de formato. **No se toca** —está fuera del alcance de P-1— pero conviene
resolverla en la maquetación final.

---

## 🔹 CAMBIO 2 · Nota nueva inmediatamente debajo de la tabla *(tras la línea 155)*

**ANTES:** no existe — la tabla termina y sigue el separador `---`.

**DESPUÉS** *(texto propuesto, íntegro)*:

> **[MODELO — actualizado tras el capítulo 19 · D98]** **La prueba histórica del capítulo
> 19 no proporciona apoyo suficiente para justificar Aceleración como una exposición
> específicamente orientada a determinados regímenes macroeconómicos.** Por ello, la
> justificación principal del módulo se mantiene en la búsqueda de **primas o fuentes
> adicionales de rentabilidad esperada a largo plazo**, no en una función táctica por
> régimen.
>
> ⚠️ **Esto no equivale a afirmar que Aceleración sea independiente del régimen
> económico.** La prueba realizada no permite una conclusión tan general: **es una retirada
> de justificación, no una afirmación contraria.** El detalle está en el capítulo 19 §19.12
> y §19.13 *(C-3)*.

---

# 2. Qué NO se cambia — verificado línea a línea

| Elemento | Línea | Estado |
|---|---|---|
| **Peso del módulo** *(12%)* | — | ✅ **Intacto** — el capítulo 4 no contiene pesos; están en el cap. 10 |
| **Vehículos** *(small caps, Robeco, multifactor)* | — | ✅ **Intactos** |
| **Función del módulo** | 116 | ✅ **Intacta**: *«Introducir fuentes adicionales de rentabilidad esperada sobre el núcleo neutral»* — ya estaba formulada como prima, no como régimen. **No requiere cambio** |
| Pregunta de control del módulo | 116 | ✅ Intacta |
| Robeco como *Aceleración + activa delegada* | 169-174 | ✅ Intacto — es forma de gestión, no régimen |
| Árbol de clasificación *(P6 → Aceleración)* | 326, 351 | ✅ Intacto — clasifica por prima, no por régimen |
| Correlaciones elevadas en Aceleración | 31, 562 | ✅ Intacto — es evidencia de implementación, no justificación por régimen |
| **Las otras seis filas del mapa** *(Motor, Defensivos, Emergentes, Freno, Reales, Asimetría)* | 149-155 | ✅ **Intactas** — corresponden a P-2, P-3 y P-4, **no autorizados** |
| Encabezado del mapa como «hipótesis de diseño» | 141-145 | ✅ Intacto |
| Tabla resumen final *(«mapa módulo→régimen sin validar hasta el cap. 19»)* | 562 | ⚠️ **Intacto por ahora** — actualizarlo pertenece a **P-6** *(columna de nivel de apoyo empírico)*, no autorizado |

---

# 3. Efecto en cadena — dónde más habría que mirar *(no se toca ahora)*

| Documento | Afirmación relacionada | ¿Se toca? |
|---|---|---|
| **Cap. 11** *(módulos implementados)* | La ficha de Aceleración menciona la prima como argumento y ya declara la evidencia como discutida | ❌ **No en P-1.** Conviene revisarlo cuando se aprueben los demás parches, para que los dos capítulos digan lo mismo |
| **Cap. 19** | §19.12 y §19.13 C-3 | ❌ **Cerrado.** No se modifica |
| `CONTRADICCIONES_HIPOTESIS_CAP4_VS_EVIDENCIA.md` | Acción propuesta nº 5 | Se marcará **ejecutada** cuando el parche se aplique |

---

# 4. Resumen para aprobar

> **Dos ediciones en el capítulo 4: una fila de tabla y una nota nueva.** Nada más.
>
> **Ni peso, ni vehículos, ni función del módulo, ni las otras seis filas del mapa.**
> **P-2 a P-6 siguen sin tocar.**

**Estado: ✅ EJECUTADO (D99).** Verificaciones superadas: función intacta · sin pesos en el
capítulo 4 · vehículos intactos · las otras seis filas del mapa intactas · capítulo 19
intacto · **P-2 a P-6 sin ejecutar**.
