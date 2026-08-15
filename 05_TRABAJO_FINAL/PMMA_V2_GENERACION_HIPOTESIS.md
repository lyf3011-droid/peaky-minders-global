# 🧬 PMMA v2 — GENERACIÓN DE HIPÓTESIS

## 15 de agosto de 2026 · **muestra de desarrollo = exclusivamente los fallos de D111**

> ## ⚠️ **NO SE HA BUSCADO NI UTILIZADO NINGUNA CARTERA NUEVA.**
> Todo el material de este documento procede **únicamente de los fallos ya observados y
> publicados en D111**. **No hay validación**: la muestra *holdout* está intacta y sin mirar.
>
> **PMMA v1 y el capítulo 4 no se modifican.** **D111 queda aceptado e inmutable** como
> resultado de PMMA v1.

---

# 1. LA HIPÓTESIS A COMPROBAR

> **[HIPÓTESIS]** **PMMA v1 puede estar mezclando dimensiones conceptualmente distintas
> dentro de una sola taxonomía.**

Si es cierta, explicaría **por qué fallaron cosas que a primera vista no tienen relación
entre sí**: un módulo geográfico que no generaliza, dos módulos con frontera borrosa, un
módulo contenedor y una función huérfana.

---

# 2. ANÁLISIS DIMENSIONAL DE LOS SIETE MÓDULOS ACTUALES

**Pregunta aplicada a cada módulo:** *¿qué tipo de cosa es realmente esta categoría?*

| Módulo | Función económica | Geografía | Factor / tilt | Perfil de payoff | Forma de gestión | Gobernanza |
|---|---|---|---|---|---|---|
| 🚀 **Motor** | ✅ **Sí — crecimiento productivo** | ⬜ neutro | ⬜ neutro | Direccional convergente | ⬜ indiferente | Núcleo ordinario |
| 🌿 **Defensivos** | 🟡 Parcial — crecimiento **con menor ciclicidad** | ⬜ | 🔴 **Sí — sesgo sectorial y de baja beta** | Direccional atenuado | ⬜ | ⬜ |
| ⚡ **Aceleración** | 🟡 «Fuentes adicionales de retorno» | ⬜ | 🔴 **ES un factor/tilt, no otra función** | Direccional | ⬜ | ⬜ |
| 🌍 **Emergentes** | 🔴 **La misma que Motor** | 🔴 **ES geografía** | ⬜ | Direccional | ⬜ | 🟡 «decisión dedicada» |
| ⚓ **Freno** | 🔴 **DOS funciones distintas** | ⬜ | ⬜ | 🔴 **Dos payoffs opuestos** *(duración larga vs nula)* | ⬜ | ⬜ |
| 🥇 **Activos Reales** | ✅ **Sí — vínculo con inflación y confianza monetaria** | ⬜ | ⬜ | Distinto de acciones y bonos nominales | ⬜ | ⬜ |
| 💥 **Asimetría** | 🟡 Opcionalidad | ⬜ | ⬜ | 🔴 **ES un perfil de payoff** | ⬜ | 🔴 **«pérdida acotada por tamaño» es gobernanza** |

## 2.1 Veredicto sobre la hipótesis

> ### 🔴 **CONFIRMADA.** Los siete módulos de PMMA v1 **no pertenecen todos a la misma
> ### dimensión conceptual**. Conviven al menos **cinco tipos de cosa distintos** bajo una
> ### sola etiqueta llamada «módulo».

| Dimensión | Módulos que en realidad pertenecen a ella |
|---|---|
| **Función económica** | Motor · Freno *(dos)* · Activos Reales |
| **Geografía** | **Emergentes** |
| **Factor / estilo** | **Aceleración** · parcialmente **Defensivos** |
| **Perfil de payoff** | **Asimetría** |
| **Gobernanza / tamaño** | la coletilla de **Asimetría** *(«pérdida acotada por tamaño»)* |

## 2.2 La hipótesis explica **los siete fallos observados**, no solo algunos

| Fallo de D111 | Explicación dimensional |
|---|---|
| **D-FRENO** | Un solo nombre cubre **dos funciones económicas** con payoff opuesto |
| **Emergentes no generaliza** | Es un **atributo geográfico** disfrazado de función. Solo aparece cuando alguien decide separarlo, no cuando la función existe |
| **Aceleración ↔ Defensivos** | **Ambos son tilts sobre la misma función** *(crecimiento)*. La frontera es borrosa porque **no hay dos funciones que separar**, solo dos intenciones |
| **Trend following huérfano** | Su rasgo definitorio es el **perfil de payoff**, y el único módulo de payoff —Asimetría— estaba **cerrado por una condición de gobernanza** |
| **Asimetría demasiado estrecha** | Mezcla **payoff** *(opcionalidad)* con **tamaño** *(gobernanza)*. La segunda condición excluyó al primer candidato legítimo |
| **Función rentas huérfana** | El **perfil de distribución** es otra dimensión más, ausente por completo |
| **Pérdida de información de T1** | T1 resuelve el problema **eliminando las dimensiones sobrantes en lugar de separarlas** |

> **Una sola causa explica los siete síntomas.** Eso es lo que convierte esto en una
> hipótesis de arquitectura y no en una lista de parches.

---

# 3. LAS TRES CANDIDATAS

## CANDIDATA A — **T1** *(cuatro funciones)*

**Crecimiento · Estabilidad · Protección Real · Opcionalidad.**

| | |
|---|---|
| **Naturaleza** | Una sola dimensión: función, con granularidad mínima |
| **Cómo resuelve** | **Eliminando** las dimensiones sobrantes: sin geografía, sin factor, sin gobernanza |
| **Precedente** | **Es la taxonomía que empató o superó a PMMA v1 en F8** |

## CANDIDATA B — **función pura con separación del Freno** *(cinco funciones)*

| # | Función | Qué resuelve |
|---|---|---|
| **1** | **Crecimiento productivo** | Absorbe Motor, Aceleración, Defensivos y Emergentes |
| **2** | **Estabilidad / liquidez** | **Separa la primera mitad del Freno** |
| **3** | **Cobertura de duración / deflación** | **Separa la segunda mitad del Freno** |
| **4** | **Protección real** | Hereda Activos Reales |
| **5** | **Diversificación convexa / retorno divergente** | **Sustituye a Asimetría sin la condición de tamaño** |

| | |
|---|---|
| **Naturaleza** | Una sola dimensión: función, con granularidad correcta |
| **Cómo resuelve** | **Separando** lo que estaba fusionado y **eliminando** lo que no era función |

## CANDIDATA C — **arquitectura bidimensional**

### Eje 1 · **FUNCIÓN PRIMARIA** — *particiona el capital, suma 100%*

**Las cinco funciones de la candidata B.**

### Eje 2 · **ATRIBUTOS ORTOGONALES** — *anotan, NO particionan, no suman 100%*

| | Atributo | Valores |
|---|---|---|
| **A1** | **Geografía** | global · desarrollado · emergente · país único |
| **A2** | **Factor o estilo** | valor · tamaño · momentum · calidad · baja volatilidad · sectorial · ninguno |
| **A3** | **Liquidez** | diaria · periódica · ilíquida |
| **A4** | **Forma de gestión** | pasiva/indexada · sistemática · activa delegada · convicción directa |
| **A5** | **Vehículo** | fondo · ETF · ETC/ETP · directo · derivado |
| **A6** | **Concentración y convicción** | diversificado · dedicado · convicción |
| **A7** | **Perfil de distribución** | acumulación · reparto |

| | |
|---|---|
| **Naturaleza** | **Dos dimensiones separadas explícitamente** |
| **Cómo resuelve** | **Separando** las funciones **y conservando** la información que A y B tiran |

> **Clave de diseño:** **el capital se reparte una sola vez, por función. Los atributos
> anotan ese mismo capital y nunca lo dividen.** Es **exactamente el principio que PMMA v1
> ya aplica a la Convicción** —*«la Convicción explica cómo se compró; el módulo explica
> para qué está»*— **generalizado a seis atributos más**. No es una invención nueva.

---

# 4. EVALUACIÓN CONTRA LOS SIETE FALLOS CONOCIDOS

**Solo se usan los fallos de D111. Ninguna cartera nueva.**

| Fallo | **A · T1** | **B · función pura** | **C · bidimensional** |
|---|:--:|:--:|:--:|
| **D-FRENO** | ❌ *«Estabilidad» sigue fusionando duración larga y efectivo* | ✅ **Separadas en F2 y F3** | ✅ **Separadas** |
| **Emergentes geográfico** | ✅ *(por eliminación)* | 🟡 *(elimina el módulo y pierde el dato de decisión dedicada)* | ✅ **F1 + A1 emergente + A6 dedicado — se conserva la información** |
| **Aceleración ↔ Defensivos** | ✅ *(colapso)* | 🟡 *(colapso: desaparece la frontera y también la distinción)* | ✅ **F1 + A2 = calidad / tamaño / valor. No hay frontera que trazar** |
| **Trend following** | ✅ *(Opcionalidad, por vaguedad)* | ✅ **F5 por construcción** | ✅ **F5 + A4 sistemática** |
| **Asimetría demasiado estrecha** | ✅ | ✅ **La condición de tamaño sale de la definición** | ✅ **Sale a A6, donde le corresponde** |
| **Función rentas** | ❌ | ❌ | 🟡 **A7 reparto captura el rasgo; queda por decidir si «rentas» es función o mandato** |
| **Pérdida de información de T1** | ❌ **Es el problema** | 🟡 **Menor, pero pierde factores y geografía** | ✅ **La conserva toda en el eje 2** |
| **RESUELTOS** | **4 / 7** *(dos por colapso)* | **4,5 / 7** | **6,5 / 7** |

---

# 5. CRITERIOS DE SELECCIÓN — **escritos antes de elegir**

| # | Criterio | Por qué |
|---|---|---|
| **S1** | **Resuelve el mayor número de fallos observados** | Es el objetivo del ejercicio |
| **S2** | **Parsimonia sobre el eje que reparte capital** | F8 penaliza categorías que particionan; **no penaliza anotaciones** |
| **S3** | **No pierde información que las arquitecturas declaran explícitamente** | Fue el fallo de T1 |
| **S4** | **Deriva de un principio ya presente en el proyecto**, no de una invención *ad hoc* | Evita construir a medida del problema |
| **S5** | **Es falsable** | Sin esto no puede validarse en el holdout |

## 5.1 Puntuación

| | **A** | **B** | **C** |
|---|:--:|:--:|:--:|
| **S1** *(fallos resueltos)* | 4/7 | 4,5/7 | **6,5/7** |
| **S2** *(categorías que particionan)* | **4** ✅ | 5 🟡 | 5 🟡 |
| **S3** *(conserva información)* | ❌ | 🟡 | ✅ |
| **S4** *(deriva de principio propio)* | 🟡 | 🟡 | ✅ **generaliza la regla de la Convicción** |
| **S5** *(falsable)* | ✅ | ✅ | 🟡 **requiere blindaje explícito — ver §7** |

---

# 6. CANDIDATA SELECCIONADA

> # 🏆 **CANDIDATA C — ARQUITECTURA BIDIMENSIONAL**

## 6.1 Por qué gana

1. **Resuelve 6,5 de 7 fallos**, frente a 4 y 4,5.
2. **Es la única que resuelve sin destruir.** A y B resuelven la frontera
   Aceleración↔Defensivos **haciendo desaparecer la distinción**; C la resuelve
   **trasladándola al eje donde siempre perteneció**.
3. **Cuesta lo mismo que B en el eje que importa para F8.** Ambas parten el capital en
   **cinco** categorías. **Los atributos no reparten capital, luego no cuentan como
   categorías de partición.**
4. **Explica los siete síntomas con una sola causa** *(§2.2)* — es una arquitectura, no un
   conjunto de parches.
5. **No inventa un principio nuevo:** generaliza el que PMMA v1 ya usa para la Convicción.

## 6.2 Por qué NO gana la candidata A, pese a haber ganado F8

**T1 ganó F8 en D111 por ser menos específica** *(declarado en D111 §7.4)*. Resuelve cuatro
fallos **a base de no poder representar aquello que los causaba**. Bajo **S3 es la peor de
las tres**: es literalmente el fallo nº 7 de la lista.

⚠️ **Pero A sigue siendo el rival a batir en el holdout.** Que pierda aquí **no la descarta**:
si en la muestra nueva C no consigue superar a T1 bajo la regla F8, **la conclusión será que
la complejidad no se paga** — y ese resultado también será aceptable.

---

# 7. RIESGOS NUEVOS QUE INTRODUCE LA CANDIDATA C

| # | Riesgo | Gravedad | Mitigación propuesta *(a congelar antes del holdout)* |
|---|---|---|---|
| **RN1** | 🔴 **Infalsabilidad por flexibilidad.** Con un eje de atributos, **casi todo es describible** — y una taxonomía que nunca falla no informa | 🔴 **Alta** | **Lista de atributos CERRADA en siete.** Añadir uno durante la validación = **fallo registrado**, no mejora. **Y regla dura: si una asignación del eje 1 solo puede decidirse mirando el eje 2, es un fallo del eje 1** |
| **RN2** | 🔴 **F5 se convierte en cajón de sastre**, exactamente el papel en que fracasó Asimetría | 🔴 **Alta** | **F5 exige demostrar convexidad o divergencia POR CONSTRUCCIÓN**, no por ausencia de mejor destino. **«No encaja en las otras cuatro» NO es criterio de F5** |
| **RN3** | 🟠 **Proliferación de atributos** | 🟠 Media | Contador explícito; **cada atributo nuevo debe justificar C1-C12 como si fuera un módulo** |
| **RN4** | 🟠 **Complejidad de lectura**: dos ejes son más difíciles de explicar que cuatro cajas | 🟠 Media | La ficha debe poder leerse **solo con el eje 1** y seguir siendo correcta |
| **RN5** | 🔴 **SOBREAJUSTE A LA MUESTRA DE DESARROLLO** | 🔴 **La más grave** | **C se ha diseñado exactamente contra los fallos que resuelve.** Que resuelva 6,5/7 **no es evidencia**: es tautología. **Solo el holdout puede decir algo** |
| **RN6** | 🟠 **F8 sin comprobar**: C parte el capital en 5 categorías frente a las 4 de T1 | 🟠 Media | Se comprobará en el holdout **con la misma regla y sin renegociarla** |

> ### ⚠️ **RN5 es la razón de existir del holdout.** Este documento **no valida nada**.

---

# 8. LO QUE ESTE DOCUMENTO **NO** HACE

- ❌ **No busca ni usa ninguna cartera nueva.**
- ❌ **No valida** ninguna candidata.
- ❌ **No modifica** PMMA v1, el capítulo 4, el 19 ni la cartera.
- ❌ **No revisa** D111, que queda **aceptado e inmutable**.
- ❌ **No ejecuta** el holdout.

---

## REGISTRO

**15-ago-2026 — Generación de hipótesis para PMMA v2.** Confirmada la hipótesis de mezcla de
dimensiones: los siete módulos de v1 pertenecen a **cinco tipos de cosa distintos**, y esa
única causa explica **los siete fallos** de D111. Tres candidatas evaluadas **solo contra los
fallos conocidos**. **Seleccionada la candidata C**, bidimensional, con **seis riesgos nuevos
declarados** — el principal, **el sobreajuste a la propia muestra de desarrollo**.
**Congelada en `PMMA_V2_CANDIDATA_PRE_HOLDOUT.md`.**
