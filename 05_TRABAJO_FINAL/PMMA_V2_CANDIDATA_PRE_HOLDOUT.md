# 🔒 PMMA v2 — CANDIDATA CONGELADA ANTES DEL HOLDOUT

## Arquitectura bidimensional · congelada el 15 de agosto de 2026

> ## ⚠️ **NINGÚN RESULTADO DE VALIDACIÓN EXTERNA NUEVA.**
> Esta candidata se ha diseñado **exclusivamente contra los fallos ya observados en D111**.
> **No se ha buscado ni utilizado ninguna cartera nueva.** La muestra *holdout* está
> **intacta y sin mirar**.
>
> **PMMA v1 sigue vigente y sin modificar.** **D111 es inmutable.** Esta candidata **no
> sustituye a nada** hasta que se valide.

---

# 1. PRINCIPIO DE DISEÑO

> ## **Una función reparte el capital. Los atributos lo describen.**

**El capital se parte una sola vez y por una sola razón: qué trabajo hace.** Todo lo demás
—dónde está, de qué estilo es, cómo se gestiona, con qué vehículo, con qué liquidez, con
cuánta convicción y si reparte o acumula— **son propiedades de ese mismo capital, no trozos
adicionales de él**.

**Es la regla que PMMA v1 ya aplicaba a la Convicción**, generalizada:

> *«La Convicción explica cómo se compró; el módulo explica para qué está.»*

---

# 2. EJE 1 · FUNCIÓN PRIMARIA — **reparte el capital, suma 100%**

| # | Función | Definición *(sin nombrar ningún producto)* | Pregunta de control |
|---|---|---|---|
| **F1** | **Crecimiento productivo** | Capital que se remunera por **la actividad económica de empresas o proyectos** | *¿Su rendimiento depende de que la economía real produzca y venda?* |
| **F2** | **Estabilidad y liquidez** | Capital cuyo trabajo es **conservar valor nominal y estar disponible** | *¿Está aquí para no perder valor nominal y poder usarse?* |
| **F3** | **Cobertura de duración** | Capital que **se revaloriza cuando caen los tipos de interés**, típicamente en shocks de crecimiento o desinflación | *¿Su rendimiento depende de la caída de los tipos?* |
| **F4** | **Protección real** | Capital cuyo comportamiento **se vincula a la inflación o a la confianza monetaria**, distinto de acciones y bonos nominales | *¿Está aquí por su relación con el poder adquisitivo del dinero?* |
| **F5** | **Retorno divergente** | Capital cuyo **perfil de resultado es convexo o descorrelacionado por construcción**, no por la clase de activo que contiene | *¿Su perfil de resultado lo produce **cómo está construido**, no **qué contiene**?* |

## 2.1 Fronteras — enunciadas **sin apelar a casos concretos** *(exigencia C12)*

| Frontera | Qué la define |
|---|---|
| **F1 ↔ F4** | **El origen de la remuneración**: actividad productiva *(F1)* frente a relación con el valor del dinero *(F4)* |
| **F2 ↔ F3** | **La duración**: F2 no la tiene y por eso conserva valor nominal; **F3 la tiene y por eso gana cuando los tipos caen y pierde cuando suben** |
| **F3 ↔ F4** | **El escenario que las remunera**: caída de tipos *(F3)* frente a pérdida de poder adquisitivo *(F4)*. **Son opuestos, no vecinos** |
| **F5 ↔ todas** | **F5 no se define por lo que contiene sino por cómo se construye.** Un mismo activo puede estar en F1 y en F5 según si se posee direccionalmente o dentro de una estructura convexa |

> ### 🔴 **REGLA DURA CONTRA EL CAJÓN DE SASTRE *(riesgo RN2)*:**
> **F5 exige demostrar convexidad o divergencia POR CONSTRUCCIÓN. «No encaja en las otras
> cuatro» NO es criterio de F5.** Lo que no encaja va al **Protocolo de Extensión**, igual
> que en v1.

---

# 3. EJE 2 · ATRIBUTOS ORTOGONALES — **anotan, NO reparten**

> ## 🔒 **LISTA CERRADA EN SIETE.** Añadir un atributo durante la validación se registra
> ## como **FALLO**, no como mejora *(mitigación de RN1 y RN3)*.

| | Atributo | Valores | Qué recupera de v1 |
|---|---|---|---|
| **A1** | **Geografía** | global · desarrollado · emergente · país único | **El antiguo módulo Emergentes** |
| **A2** | **Factor o estilo** | valor · tamaño · momentum · calidad · baja volatilidad · sectorial · ninguno | **Aceleración y el sesgo de Defensivos** |
| **A3** | **Liquidez** | diaria · periódica · ilíquida | *(nuevo — v1 no lo tenía)* |
| **A4** | **Forma de gestión** | pasiva/indexada · sistemática · activa delegada · convicción directa | **Ya existía en v1, sin cambios** |
| **A5** | **Vehículo** | fondo · ETF · ETC/ETP · directo · derivado | Ya existía en el modelo de datos |
| **A6** | **Concentración y convicción** | diversificado · dedicado · convicción | **La capa de Convicción y el «tamaño acotado» de Asimetría** |
| **A7** | **Perfil de distribución** | acumulación · reparto | **La función «rentas»**, huérfana en v1 |

## 3.1 Reglas del eje 2

1. **Los atributos NO suman 100%** ni reparten capital.
2. **Una posición tiene exactamente una función y tantos atributos como apliquen.**
3. 🔴 **Si una asignación del eje 1 solo puede decidirse mirando el eje 2, es un fallo del
   eje 1** — no una virtud del eje 2 *(mitigación de RN1)*.
4. **La ficha debe seguir siendo correcta leyendo solo el eje 1** *(mitigación de RN4)*.

## 3.2 Capas transversales que se conservan

| Capa | Estado en v2 |
|---|---|
| **Reserva Operativa** | ✅ **Se conserva como capa de ejecución.** No es F2: F2 es asignación estratégica, la Reserva es infraestructura |
| **Convicción** | ✅ **Se conserva**, ahora formalizada como **A6 = convicción**. **Sigue sin ser un módulo** |

---

# 4. ÁRBOL DE CLASIFICACIÓN

## Paso 1 · Función primaria — **orden fijo, de lo más específico a lo más general**

```
P1  ¿Su perfil de resultado lo produce CÓMO ESTÁ CONSTRUIDO
    (convexidad o divergencia demostrable), y no qué contiene?      → F5
                                     │ no
P2  ¿Su función dominante es vincularse a la inflación
    o a la confianza monetaria?                                     → F4
                                     │ no
P3  ¿Su función dominante depende de la DURACIÓN — se revaloriza
    cuando caen los tipos?                                          → F3
                                     │ no
P4  ¿Está para conservar valor nominal y estar disponible?          → F2
                                     │ no
P5  ¿Se remunera por la actividad económica de empresas
    o proyectos?                                                    → F1
                                     │ no
                            → PROTOCOLO DE EXTENSIÓN
```

**Por qué este orden:** de lo más específico a lo más general, como en v1. **F1 va la última
por ser la más ancha**, no por ser la menos importante — si se preguntara primero, absorbería
casos que pertenecen a F4 o F5.

## Paso 2 · Atributos

**Sin orden.** Se anotan los siete que apliquen. **Este paso no puede cambiar el resultado
del paso 1** *(regla 3 del §3.1)*.

---

# 5. EJEMPLOS CONCEPTUALES

> ⚠️ **Todos proceden de casos YA publicados en D111.** **Ninguno es una cartera nueva.**

| Caso *(de D111)* | PMMA v1 | **PMMA v2 candidata** | Fallo que resuelve |
|---|---|---|---|
| **Bonos del Tesoro a largo** *(Permanent Portfolio)* | Freno | **F3** + A1 desarrollado | 🔴 **D-FRENO** |
| **Efectivo** *(Permanent Portfolio)* | Freno *(el mismo)* | **F2** | 🔴 **D-FRENO** |
| **Bonos largos + bonos cortos** *(Golden Butterfly)* | Freno *(uno solo, 40%)* | **F3 + F2, separados** | 🔴 **D-FRENO** |
| **Small cap value** *(Golden Butterfly)* | Aceleración | **F1** + A2 *(tamaño, valor)* | ⚡↔🌿 frontera |
| **Quality** *(multifactorial)* | ¿Aceleración o Defensivos? | **F1** + A2 *(calidad)* | ⚡↔🌿 **desaparece la frontera** |
| **Momentum** *(multifactorial)* | Aceleración *(indistinguible de value)* | **F1** + A2 *(momentum)* | **D-GRANULARIDAD** |
| **Renta variable emergente** *(Swensen)* | Emergentes | **F1** + A1 *(emergente)* + A6 *(dedicado)* | 🌍 **Emergentes geográfico** |
| **TIPS** *(Swensen)* | Activos Reales *(contra su propio default)* | **F4** + A1 | R1 — **ya no hay «default» que contradecir** |
| **REITs** *(Swensen)* | Activos Reales | **F4** + A2 *(sectorial)* + A3 *(diaria)* | R2 |
| **Trend following** | ❌ **sin módulo** | **F5** + A4 *(sistemática)* + A5 *(derivado)* | 🔴 **O-DINÁMICA** |
| **Bitcoin** *(Global 10Y)* | Asimetría | **F5** + A6 *(convicción)* — **el tamaño acotado pasa a ser atributo, no definición** | 💥 **Asimetría estrecha** |
| **Renta variable de dividendo** *(rentas)* | Motor *(se pierde el rasgo)* | **F1** + **A7 *(reparto)*** | 🟡 **O-RENTAS, parcialmente** |
| **High yield** *(rentas)* | Extensión | **Extensión** *(sin cambio)* | ⬜ No resuelto |

## 5.1 Qué **no** resuelve la candidata

| Caso | Estado |
|---|---|
| **High yield** | Sigue yendo al Protocolo de Extensión. **v2 no lo mejora** |
| **«Generación de rentas» como función** | **A7 captura el rasgo, no la intención.** Queda pendiente decidir si es **función, atributo o propiedad del mandato** |
| **Private equity, infraestructura, opciones y país único** | **No testados en D111.** **Su tratamiento en v2 es una hipótesis sin comprobar** |

---

# 6. COMPARACIÓN ESTRUCTURAL v1 → v2 *(candidata)*

| | **PMMA v1** | **PMMA v2 candidata** |
|---|---|---|
| **Categorías que reparten capital** | **7** | **5** |
| **Dimensiones mezcladas** | **5** *(función, geografía, factor, payoff, gobernanza)* | **2, explícitas y separadas** |
| **Capas transversales** | Convicción · Reserva | **Reserva** *(Convicción pasa a A6)* |
| **Atributos formalizados** | 1 *(forma de gestión)* | **7, lista cerrada** |
| **Módulos por geografía** | 1 *(Emergentes)* | **0** |
| **Módulo definido por payoff** | 1, con condición de tamaño | **1, sin condición de tamaño** |

---

# 7. CÓMO SE VALIDARÁ — **y cómo puede fracasar**

> **Esta candidata se someterá a la muestra HOLDOUT con las mismas reglas C1-C12 y F1-F9, y
> con la misma regla F8 frente a T0 y T1. Las reglas no se renegocian.**

| Podría fracasar si… | Fallo asociado |
|---|---|
| **F5 acaba absorbiendo lo que no encaja** | RN2 · F6 |
| **Hace falta un octavo atributo** | 🔴 **RN1/RN3 — se registra como fallo, no como mejora** |
| **Alguna asignación del eje 1 solo se resuelve mirando el eje 2** | 🔴 **Regla 3 del §3.1** |
| **T1 vuelve a cumplir las cuatro condiciones de F8** | 🔴 **F8 — la complejidad no se paga** |
| **Aparecen funciones huérfanas nuevas en ≥3 arquitecturas** | F3 |
| **Las cinco funciones no se identifican en ≥2 arquitecturas externas cada una** | C3 |

## 7.1 La advertencia que debe acompañar a esta candidata

> ### 🔴 **Esta arquitectura resuelve 6,5 de los 7 fallos porque fue diseñada exactamente
> ### contra ellos. Eso NO es evidencia: es tautología.**
> **El único dato con valor será el de la muestra holdout, que no se ha mirado.**

---

## REGISTRO

**15-ago-2026 — Candidata PMMA v2 congelada antes del holdout.** Arquitectura bidimensional:
**cinco funciones que reparten capital** *(crecimiento productivo · estabilidad y liquidez ·
cobertura de duración · protección real · retorno divergente)* y **siete atributos
ortogonales de lista cerrada** que anotan sin repartir. Incluye definiciones, fronteras
enunciadas en abstracto, árbol de clasificación de cinco preguntas, trece ejemplos
conceptuales procedentes **solo de D111** y las condiciones bajo las que puede fracasar.
**Sin ninguna cartera nueva. Sin validación. PMMA v1 intacto.**
