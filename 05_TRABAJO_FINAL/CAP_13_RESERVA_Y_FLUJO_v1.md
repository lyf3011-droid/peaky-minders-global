# CAPÍTULO 13 — RESERVA OPERATIVA Y FLUJO DE APORTACIONES

## Investment Book · Parte II · Borrador v1 · 13 de agosto de 2026

> **Convención:** **[MODELO]** = decisión propia · **[EVIDENCIA EXTERNA]** = requiere
> fuente.
>
> **La frase que gobierna este capítulo:**
>
> ### **«La aportación mensual no replica la cartera: la rebalancea.»**

---

## 13.1 El problema que resuelve el flujo

Cada mes entran 1.000 € nuevos. La reacción instintiva sería repartirlos como está
repartida la cartera: 440 al Motor, 120 a Defensivos… **[MODELO]** Ese reparto
proporcional es exactamente lo que **no** se hace, por una razón simple: perpetúa las
desviaciones en lugar de corregirlas — mete dinero en lo que ya está sobre su objetivo y
no repone lo que se quedó atrás.

En este mandato el flujo es una herramienta enorme: 12.000 € al año sobre una cartera
inicial de 100.000 permiten corregir las desviaciones típicas de todos los módulos
**sin vender nada** — con lo que el rebalanceo casi no genera coste ni fricción.

---

## 13.2 El árbol de decisión mensual

**[MODELO]** Cada mes, los 1.000 € siguen este camino y no otro:

```
ENTRAN 1.000 €
   │
   ├─ PASO 1 · ¿Hay alguna empresa del universo de Convicción
   │           con precio ≤ IDC y tesis intacta?
   │
   │     SÍ → CONVICCIÓN TIENE PRIORIDAD.
   │          La aportación puede ir íntegra a esa compra
   │          (más la Reserva disponible si hace falta).
   │
   └─ NO → PASO 2 · ¿Hay algún módulo por debajo de su objetivo?
              │
              ├─ SÍ → los 1.000 € van AL MÓDULO CON MAYOR DESVIACIÓN
              │        NEGATIVA (uno solo; no se reparte).
              │
              └─ NO → PASO 3 · los 1.000 € van AL MOTOR
                       (destino indexado por defecto).
```

Tres reglas cierran el árbol para que no admita interpretación:

1. **La Reserva participa en el ranking de infraponderación como un bloque más.** Si se
   consumió ejecutando una compra, compite por las aportaciones siguientes y se
   reconstruye sola — sin regla especial.
2. **La capa de Convicción NUNCA aparece en ese ranking.** Su objetivo es 0%; no tiene
   hueco que rellenar. Su única puerta es el paso 1: precio y tesis.
3. **Lo no ejecutado caduca.** Si un mes hubo cinco oportunidades y capital para dos, las
   tres restantes no quedan «pendientes»: el mes siguiente se reevalúa todo desde cero.

---

## 13.3 La Reserva en operación

**[MODELO]** La fórmula del capítulo 5 — *la política es permanente; el capital es
transitorio* — se traduce operativamente así:

- **Capacidad objetivo/máxima: 3%** del patrimonio, en efectivo remunerado.
- **Se consume** cuando una compra de Convicción necesita más que la aportación del mes.
- **Se reconstruye** por el árbol del §13.2: al quedar por debajo de su capacidad, entra
  en el ranking y las aportaciones la reponen.
- **No se recarga por miedo** — su tamaño no sube porque el mercado «parezca caro», ni
  baja porque parezca barato. No expresa opiniones.

Ejemplo completo con números redondos: en un mes aparecen tres empresas en precio.
Financiación disponible: 1.000 € de aportación + 3.000 € de Reserva = 4.000 €. Se ejecutan
las compras por orden de descuento *(cap. 12)*; la Reserva queda en 1.000 €. Los meses
siguientes, sin nuevas oportunidades, el árbol la detecta infraponderada y la reconstruye
hacia el 3%. **Ninguna venta en todo el proceso.**

---

## 13.4 Lo que las aportaciones no pueden hacer

**[MODELO]** El mecanismo tiene un límite estructural que hay que decir en voz alta:

> ### **Las aportaciones solo suman. Nunca restan.**

Pueden corregir un módulo que se quedó **corto**; no pueden reducir uno que creció
**demasiado**. Si una posición muy volátil se multiplica y desborda sus límites, el flujo
mensual tardaría años en diluirla — la única herramienta real para eso son las ventas, y
**la política de ventas por sobreponderación está pendiente y registrada como tal**
*(D47b)*. Este libro no la improvisa: declara el hueco y remite a su cierre.

Mientras tanto, la vigilancia existe: los pesos se comparan con sus objetivos en cada
revisión, y una sobreponderación material dispara la elaboración de esa política, no una
venta impulsiva.

---

## 13.5 Los dos relojes, versión operativa

El principio del capítulo 5 *(el mercado es continuo; el capital, periódico)* se concreta
aquí en tres consecuencias prácticas:

1. **Entre revisiones no hay cambios rutinarios por ruido de mercado.** Las subidas y
   bajadas normales no disparan órdenes.
2. **Las reglas predefinidas sí actúan en cualquier momento**: una empresa que alcanza su
   IDC, la invalidación de una tesis, un problema sobrevenido en un vehículo. Toda
   actuación fuera de calendario ejecuta una regla escrita — nunca improvisa.
3. **El despliegue de oportunidades es gradual por diseño.** La capacidad de un mes es la
   aportación más la Reserva; si las oportunidades exceden eso, se ejecutan las de mayor
   descuento y el resto caduca. Se prefiere comprar menos al precio correcto que forzar
   liquidez para comprarlo todo.

---

## 13.6 Síntesis

> **Mil euros al mes con un árbol de tres pasos: primero la oportunidad con precio y
> tesis; si no la hay, el módulo más rezagado; si no lo hay, el Motor. La Reserva se
> consume ejecutando y se reconstruye sola. Y el límite queda declarado: las aportaciones
> corrigen lo que falta, nunca lo que sobra — para eso hará falta la política de ventas,
> que está pendiente y no se improvisa aquí.**

---

## CIERRE — control de auditoría

| Decisiones | Evidencia | Limitaciones | Visuales | Fuentes pendientes | Remisiones |
|---|---|---|---|---|---|
| D56 *(árbol de asignación dinámica y sus tres reglas)* · D57-D58 *(importes y priorización)* · D59 *(dos relojes y despliegue gradual)* · D50 *(Reserva)* · D5 *(bandas evaluadas en revisión, no en continuo)* | El árbol es ejecutable sin interpretación *(verificado en el protocolo operativo del proyecto con las ocho preguntas que antes exigían criterio)* · el ejemplo del §13.3 con la aritmética completa | 🔴 **Política de ventas por sobreponderación PENDIENTE** *(D47b)* — el límite del §13.4 queda sin su segunda mitad · el rendimiento del efectivo remunerado de la Reserva, pendiente de cifra con fuente *(cap. 22)* | ① El árbol mensual ② El ciclo consumo→reconstrucción de la Reserva ③ La asimetría «suman/no restan» | 🟡 remuneración del efectivo operativo *(cap. 22)* | **Cap. 12** *(qué es una oportunidad válida)* · **Cap. 5** *(el principio de la capa de ejecución)* · **D47b** *(ventas — pendiente)* · **Cap. 23** *(rebalanceo completo y bandas)* |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-13 | **Borrador v1** — el árbol mensual con sus tres reglas de cierre *(la Reserva compite, Convicción nunca, lo no ejecutado caduca)*, la Reserva en operación con ejemplo numérico completo, el límite estructural declarado *(las aportaciones no restan — D47b pendiente)* y los dos relojes en versión operativa |
