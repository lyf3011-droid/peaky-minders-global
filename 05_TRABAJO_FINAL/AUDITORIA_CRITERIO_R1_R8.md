# 🔍 AUDITORÍA DEL CRITERIO R1-R8

## 14 de agosto de 2026 · antes de descargar ninguna serie

> **Objetivo:** comprobar que ninguna regla deja margen de decisión discrecional, que
> ninguna mira al futuro, y que un tercero podría repetir la clasificación y obtener
> exactamente lo mismo.

---

## 1. Auditoría regla por regla

| # | Regla | ¿Sin ambigüedad? | ¿Sin mirar al futuro? | ¿Reproducible? | Observación |
|---|---|---|---|---|---|
| **R1** | Trimestre | ✅ | ✅ | ✅ | La unidad la impone el PIB |
| **R2** | Crecimiento = PIB real interanual | ✅ | ✅ | ✅ | Serie única identificada |
| **R3** | Inflación = IPC interanual | ✅ | ✅ | ✅ | Se usa el IPC **general**, no el subyacente *(fijado aquí: es el que vive la gente y el que tiene serie más larga)* |
| **R4** | Mediana móvil de 40 trimestres, excluyendo el clasificado | ✅ | ✅ **Solo pasado** | ✅ | La exclusión del propio trimestre está definida sin ambigüedad |
| **R5** | Episodio = ≥2 trimestres consecutivos | ✅ | ⚠️ **Ver §2.1** | ✅ | Un trimestre aislado **conserva su caja** para el cálculo por cajas; lo que exige ≥2 es llamarlo «episodio» |
| **R6** | Sin zona frontera; marca informativa con fórmula fija | ✅ | ✅ | ✅ | **La discrecionalidad de la v1 queda eliminada** |
| **R7** | Publicación de umbrales, código y series | ✅ | — | ✅ | Es la regla que hace auditable todo lo demás |
| **R8** | Reglas congeladas antes de mirar rentabilidades | ✅ | — | ✅ | Con procedimiento explícito si hubiera que cambiarlas |

## 2. Las cuatro ambigüedades detectadas — y cerradas aquí

### 2.1 R5 · ¿qué pasa con un trimestre aislado?

**Ambigüedad:** si un trimestre cae en la caja 4 rodeado de caja 3, ¿cuenta o no?

> **🔒 Cerrado:** **cuenta para el cálculo agregado por cajas** *(no se descarta ningún
> dato)*, pero **no constituye un «episodio»** ni entra en el recuento de episodios de la
> regla de consistencia del §9.1. Los trimestres aislados se publican en una tabla aparte.

### 2.2 Los 40 primeros trimestres de la muestra

**Ambigüedad:** los primeros 10 años no tienen ventana completa hacia atrás.

> **🔒 Cerrado:** **no se clasifican.** Con PIB desde 1947, la clasificación empieza en
> **1957**. Nada de rellenar con ventanas más cortas — eso daría umbrales inestables
> precisamente en el arranque.

### 2.3 Empates exactos con la mediana

**Ambigüedad:** ¿y si un valor coincide con la mediana?

> **🔒 Cerrado:** **valor ≥ mediana = «alto»**. Convención declarada, aplicada igual a
> ambas variables. *(Con datos continuos es prácticamente imposible, pero la regla existe
> para que no haya ni una decisión sin escribir.)*

### 2.4 Trimestre del IPC

**Ambigüedad:** el IPC es mensual; ¿qué mes representa al trimestre?

> **🔒 Cerrado:** **media de los tres meses del trimestre**, y la variación interanual se
> calcula sobre esa media trimestral. *(Alternativa descartada: usar el último mes — más
> volátil y menos comparable con un PIB que es un flujo del trimestre entero.)*

## 3. Riesgos que la auditoría NO puede eliminar

| Riesgo | Por qué persiste | Cómo se trata |
|---|---|---|
| **La elección misma de niveles vs sorpresas** | Es una decisión de diseño, no un error | Declarada en §1 del dossier |
| **La elección de EEUU** | Idem | Declarada en §12 |
| **Revisiones históricas del PIB** | Los datos originales no son recuperables sin pagar | Declarado en §5: descriptivo ex post |
| **Pocos episodios en la caja 4** | Es la historia, no el método | Regla de consistencia §9.1 |

**Ninguno de los cuatro se puede resolver: los cuatro se declaran.** Ésa es la diferencia
entre una limitación y un defecto.

## 4. Prueba de integridad exigida al código *(antes de usar resultados)*

1. **Suma de trimestres por caja = total de trimestres clasificados** *(sin pérdidas)*.
2. **Ningún umbral usa datos posteriores** al trimestre clasificado — verificable por
   construcción de la ventana.
3. La **clasificación alternativa** *(media de 10 años)* se calcula con el mismo código,
   cambiando un solo parámetro.
4. Los **resultados se guardan con la fecha de descarga de las series**.

## 5. Veredicto

> ### ✅ **El criterio R1-R8 queda CERRADO. No hay ninguna decisión metodológica abierta.**
>
> Las cuatro ambigüedades detectadas se han cerrado en §2 con reglas fijas *(trimestre
> aislado, arranque en 1957, empates, trimestralización del IPC)*, y forman parte del
> criterio congelado por R8.

**Queda por tanto habilitada la preparación de series y cálculos** — no la redacción del
capítulo.
