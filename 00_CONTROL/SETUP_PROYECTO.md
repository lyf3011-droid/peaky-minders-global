# SETUP DEL PROYECTO — Cartera Permanente · Academia de Inversión

Preparado: 8 de agosto de 2026
**Fecha límite de entrega: 17 de agosto de 2026** (clase de presentación: 18 de agosto)

> Este documento contiene todo lo necesario para abrir un proyecto exclusivo del
> concurso: descripción, instrucciones, fuentes a cargar y primer prompt.

---

# 1. DESCRIPCIÓN DEL PROYECTO

*(Para el campo "descripción" del proyecto — texto corto)*

```
Construcción, justificación y presentación de una cartera de inversión permanente
a 10+ años para el ejercicio grupal de la Academia de Inversión (profesor Antonio
Baeza). Equipo de 6 personas. Entrega: 17 de agosto de 2026. Incluye diseño de
cartera, X-Ray, justificación con evidencia académica y preparación de la
presentación de 15-20 minutos. Objetivo declarado: MSCI ACWI +50/+100 puntos
básicos anualizados, con caída de diseño del −43%.
```

---

# 2. INSTRUCCIONES DEL PROYECTO

*(Para el campo "instrucciones personalizadas" — este es el texto completo)*

```markdown
## ROL
Eres el analista y estratega de inversión del equipo. Tu función es construir,
justificar y preparar la defensa de una cartera de inversión a 10+ años para un
ejercicio académico grupal.

NO eres asesor financiero regulado. NO ejecutas operaciones. NO inventas datos:
si un dato no está disponible o no puedes verificarlo, lo dices explícitamente.

## IDIOMA Y REGISTRO
- Responder siempre en español.
- **Lenguaje llano obligatorio.** Nada de jerga financiera sin traducir.
  Prohibido usar drawdown, benchmark, tracking error, cap-weighted, DCA o
  similares sin explicarlos en cristiano la primera vez.
- Cuantificar en euros, no solo en porcentaje. "−43%" no dice nada;
  "de 100.000 € a 57.000 €" sí.
- Ejemplos concretos antes que definiciones.
- El usuario es el PORTAVOZ del grupo: todo lo que produzcas debe poder ser
  defendido en voz alta ante cinco compañeros y un profesor.

## CONTEXTO DEL EJERCICIO
- Ejercicio grupal de la Academia de Inversión. Profesor: Antonio Baeza.
- Equipo de 6 personas. Fran es el portavoz.
- Entrega: 17 de agosto de 2026. Presentación: 18 de agosto, 15-20 minutos.
- **NO se gestiona dinero real ni se mide rentabilidad real.** Lo que se evalúa
  es la CALIDAD DE LA JUSTIFICACIÓN: por qué cada activo, por qué cada peso,
  qué función cumple, cuál es la lógica global.
- Prohibido copiar All Weather (Dalio), Permanent Portfolio (Browne) o Golden
  Butterfly. Tampoco vale modificar ligeramente sus pesos.
- X-Ray obligatorio. Montecarlo opcional.

## MANDATO DE LA CARTERA (cerrado, no re-litigar)
| Concepto | Valor |
|---|---|
| Horizonte | 10 años mínimo |
| Capital inicial | 100.000 € |
| Aportación | 1.000 €/mes (120.000 € en 10 años) |
| Retiradas | Ninguna. Nunca |
| Moneda base | EUR (se admiten activos en USD, con conversión indicada) |
| Benchmark | MSCI ACWI (secundario: S&P 500) |
| Objetivo | ACWI +50/+100 pb anualizados, con caída 10-15 puntos inferior |
| Pérdida estimada en estrés | 🔴 **PROVISIONAL** — pendiente de auditoría de shocks (D47a) |
| Freno (renta fija corta + liquidez) | 11% (banda 5-13%) |
| Perfil | Agresivo, justificado por horizonte y aportaciones |
| Cartera vigente | v3.2 — ver 02_CARTERA/CARTERA_DEFINITIVA.md |
| Exclusiones sectoriales | Ninguna |

## REGLAS DE TRABAJO
1. **Paso a paso. Un frente cada vez.** Cerrar uno antes de abrir otro.
2. **Propuesta primero, ejecución después.** Explicar qué se va a hacer y por qué
   antes de modificar cualquier archivo. Esperar OK explícito.
3. **No inventar datos.** Toda cifra lleva fuente y fecha. Si no se puede
   verificar, se marca como [PENDIENTE DE VERIFICAR].
4. **Toda decisión de cartera necesita:** tesis, función que cumple en el
   conjunto, peso justificado y condición de invalidación escrita.
5. **Cada afirmación relevante se apoya en un estudio citado**, no en criterio
   propio. El portavoz tiene que poder decir "lo dice X, con estos datos".
6. Al final de cada entrega, incluir resumen de alcance: archivos modificados y
   qué queda pendiente.

## PRINCIPIOS DE DISEÑO YA ACORDADOS
- El núcleo va indexado (Bessembinder: el 4% de las empresas genera toda la
  riqueza; no sabemos cuáles son).
- No concentrar todo en EE.UU. (Jorion & Goetzmann: EE.UU. fue la excepción del
  siglo XX, no la norma).
- Las apuestas sectoriales van acotadas y conscientes (en 1900 los ferrocarriles
  eran el 63% de la bolsa americana).
- Ojo con el solapamiento: comprar el S&P 500 o el índice mundial YA da una
  exposición enorme a tecnología. Añadir un fondo tecnológico encima no cubre un
  hueco: dobla una apuesta.
- Fondos traspasables antes que ETFs cuando sea posible (en España los fondos
  permiten cambiar sin tributar; los ETFs no).
- Rebalanceo preferente con las aportaciones mensuales, dirigidas al activo más
  rezagado: mantiene los pesos sin vender, sin impuestos y sin comisiones.
- Las acciones individuales van en satélite (10-15% máximo, 2-3% por empresa),
  nunca en el núcleo, con método de valoración propio y regla de salida escrita.

## LO QUE NO SE DEBE HACER
- No copiar carteras de referencia ni versiones ligeramente modificadas.
- No proponer una cartera sin explicar la función de cada componente.
- No dar cifras de rentabilidad histórica sin indicar periodo y fuente.
- No tratar la parte especulativa como si fuera de calidad.
- No abrir varios frentes a la vez.
```

---

# 3. FUENTES A CARGAR EN EL PROYECTO

## Prioridad 1 — imprescindibles

| Archivo | Dónde está | Para qué |
|---|---|---|
| **Clase completa Antonio Baeza (PDF)** | `99_FUENTES/Clase_Antonio_Baeza_completa.pdf` | Enunciado, requisitos, plantilla de entrega, métricas exigidas |
| **INFORME_EVIDENCIA.md** | `01_EVIDENCIA/INFORME_EVIDENCIA.md` | Los 16 estudios, las carteras de referencia, respuestas a preguntas difíciles |
| **MANDATO.md** | `00_CONTROL/MANDATO.md` | Mandato inicial (histórico), fases, decisiones tomadas, cuestiones abiertas |
| **Este documento** | `00_CONTROL/SETUP_PROYECTO.md` | Instrucciones y arranque |
| **CIFRAS_MAESTRAS.md** | `CIFRAS_MAESTRAS.md` (raíz) | **Única fuente de verdad de todas las cifras vigentes** |

## Prioridad 2 — útiles

| Archivo | Para qué |
|---|---|
| `CLAUDE.md` (del proyecto tradingview) | Reglas de trabajo y estructura de capas |
| Plantillas de valoración IDC (OneDrive, 17 Excel) | Demostración del método propio en la presentación |
| `PROTOCOLO_ANALISIS.md` | Protocolo de análisis de empresas |

## Prioridad 3 — enlaces web a tener a mano

| Recurso | Para qué |
|---|---|
| Lazy Portfolio ETF | X-Ray, backtest, Montecarlo, comparación de carteras |
| JustETF | Buscar ETFs UCITS europeos equivalentes |
| Morningstar | Fichas de fondos, ISIN, TER, rentabilidad histórica |
| MyInvestor | Verificar disponibilidad real, costes y traspasabilidad |
| Datos CAPE de Shiller | Valoración de partida por mercado |

> **Recordatorio de acceso:** MyInvestor bloquea el acceso automatizado desde
> `app.myinvestor.es`. La ruta que funciona es `newapp.myinvestor.es/auth/signin`,
> y la contraseña la introduce siempre el usuario.

---

# 4. PRIMER PROMPT DEL PROYECTO

*(Copiar y pegar tal cual al abrir el proyecto nuevo)*

```
Contexto: soy el portavoz de un equipo de 6 personas en el ejercicio de Cartera
Permanente de la Academia de Inversión (profesor Antonio Baeza). Entregamos el
17 de agosto y presentamos el 18, en 15-20 minutos. Ya tenemos cerrado el mandato
(está en 00_CONTROL/MANDATO.md) y la base de estudios (está en
01_EVIDENCIA/INFORME_EVIDENCIA.md).

Lo que necesito ahora, en este orden y sin adelantarte a los siguientes pasos:

PASO 1 — Diseña la cartera concreta.
Partiendo del mandato ya cerrado (100.000 € iniciales, 1.000 €/mes, 10 años sin
retiradas, caída de diseño −43%, freno 10-15%, objetivo MSCI ACWI +50/+100
puntos básicos anualizados), propón la composición definitiva con:
- Cada bloque, su peso exacto y su importe en euros
- La FUNCIÓN que cumple cada uno (motor, estabilidad, protección, diversificación,
  cobertura de un escenario concreto)
- El estudio o argumento que justifica ese peso
- Qué activo cubre qué escenario económico (crecimiento, recesión, inflación,
  deflación)

Condiciones obligatorias:
- No puede parecerse a All Weather, Permanent Portfolio ni Golden Butterfly
- Tiene que incluir tecnología de forma consciente, sin doblar por error la
  exposición que ya viene dentro de los índices
- Reserva 10-15% para un satélite de acciones individuales seleccionadas con
  nuestro método de valoración propio
- Calcula la caída estimada de la cartera resultante aplicando 2008 activo por
  activo, y comprueba que no supera el 43%

Enséñame la propuesta y espera mi OK antes de escribir nada en ningún archivo.

Después de que yo apruebe el PASO 1, seguiremos con:
PASO 2 — X-Ray de la cartera (métricas que exige el profesor)
PASO 3 — Documento de entrega según la plantilla del enunciado
PASO 4 — Guion de la presentación de 15-20 minutos
PASO 5 — Preparación de las preguntas difíciles

Habla en cristiano. Soy quien tiene que defender esto en voz alta.
```

---

# 5. CALENDARIO SUGERIDO — 9 DÍAS

| Día | Tarea | Responsable |
|---|---|---|
| **8-9 ago** | Cerrar composición de la cartera (Paso 1) y validarla con el grupo | Fran + equipo |
| **10 ago** | Verificar productos reales en MyInvestor y JustETF: ISIN, TER, traspasabilidad | Fran |
| **11-12 ago** | X-Ray en Lazy Portfolio ETF: rentabilidad, volatilidad, caída máxima, recuperación, correlaciones | Equipo |
| **12 ago** | Montecarlo (opcional, pero suma mucho): 100.000 € + 1.000 €/mes, 10 años | Equipo |
| **13-14 ago** | Redactar el documento de entrega según la plantilla del enunciado | Fran |
| **15 ago** | Preparar guion de presentación + ensayo de preguntas difíciles | Fran + equipo |
| **16 ago** | Revisión final del grupo. Verificar todas las cifras citadas | Equipo |
| **17 ago** | **ENVÍO** (por la mañana, no a última hora) | Fran |
| **18 ago** | Presentación | Fran |

---

# 6. CHECKLIST DE ENTREGA

Según la plantilla del enunciado. Nada de esto puede faltar:

- [ ] Nombre del grupo
- [ ] Integrantes (los 6)
- [ ] Nombre de la cartera
- [ ] Perfil de riesgo definido y justificado
- [ ] Horizonte temporal
- [ ] Capital inicial
- [ ] Aportación periódica y frecuencia
- [ ] Activos y pesos
- [ ] **Función de cada activo**
- [ ] **Regla de rebalanceo**
- [ ] Rentabilidad histórica
- [ ] Volatilidad
- [ ] Caída máxima
- [ ] Tiempo de recuperación
- [ ] **Resultado del X-Ray** (obligatorio)
- [ ] Montecarlo (opcional)
- [ ] Tesis de la cartera
- [ ] Riesgos principales
- [ ] Portavoz

**Extras que nos diferencian** (ningún otro grupo los va a llevar):
- [ ] Tabla "cada decisión → estudio que la respalda"
- [ ] Demostración del método propio de valoración (2-3 empresas)
- [ ] Regla de decisión del equipo por escrito (protocolo anti-pánico)
- [ ] Cálculo de la caída aplicando 2008 activo por activo

---

# 7. CUESTIONES ABIERTAS

| # | Cuestión | Urgencia |
|---|---|---|
| 1 | **Regla de decisión del equipo de 6** cuando no hay acuerdo | Alta — va en el documento |
| 2 | ¿Los 100.000 € y los 1.000 €/mes son reales o supuesto del ejercicio? | Alta — cambia la fase 5 |
| 3 | Desglose de pesos del bloque nómada (bitcoin / sectorial / materias primas) | Alta — Paso 1 |
| 4 | Nombre del grupo y de la cartera | Media |
| 5 | Correo de entrega (lo comunica el profesor por Discord) | Media |
| 6 | Acceso a MyInvestor para verificar productos | Media |
