# 🗺️ COBERTURA HISTÓRICA POR MÓDULO — CAPÍTULO 19

## Qué puede evaluarse con rigor y qué no · 14 de agosto de 2026

> **Principio del documento:** es mejor decir **«no se puede evaluar con suficiente rigor»**
> que rellenar un hueco con un proxy débil para que la tabla tenga siete filas completas.
> **Cuatro de las trece líneas de este documento son huecos declarados.**

---

# 1. Módulos CON cobertura suficiente

## 🚀 Motor

| | |
|---|---|
| **Función** | Capturar el crecimiento económico y empresarial de largo plazo |
| **Proxy** | Mercado de acciones EEUU ponderado por capitalización, retorno total |
| **Fuente** | Biblioteca de datos Kenneth French *(Dartmouth)*, base CRSP 202606 |
| **Periodo** | **1958Q1 → 2026Q2** *(la serie llega a 1926; la limita la clasificación)* |
| **Representa bien** | El comportamiento de la renta variable amplia en cada clima; el orden de magnitud de sus retornos reales |
| **NO representa** | Nuestro Motor real *(que es mitad global, mitad EEUU)*; costes, fiscalidad ni divisa euro |
| **Confianza** | 🟢 **Alta** — 273 trimestres, 50 episodios |

## 🌿 Defensivos

| | |
|---|---|
| **Función** | Mantener exposición productiva reduciendo la sensibilidad al ciclo |
| **Proxy** | Carteras sectoriales *Consumer NonDurables* y *Healthcare* |
| **Fuente** | Kenneth French, 12 Industry Portfolios *(value-weighted)* |
| **Periodo** | **1958Q1 → 2026Q2** |
| **Representa bien** | El comportamiento relativo de sectores defensivos frente al mercado |
| **NO representa** | La definición sectorial de los índices MSCI que usan nuestros ETF; **la composición del sector salud de 1960 no se parece a la actual** |
| **Confianza** | 🟡 **Media-alta.** ⚠️ **Rebajada a media tras la prueba de robustez**: en la caja 3, qué defensivo cumple **depende del umbral elegido** |

## ⚡ Aceleración *(tamaño y valor)*

| | |
|---|---|
| **Función** | Fuentes adicionales de rentabilidad esperada sobre el núcleo |
| **Proxy** | Media de las tres carteras pequeñas · media de las dos de alto valor contable |
| **Fuente** | Kenneth French, 6 Portfolios 2×3 *(tamaño × valor contable/precio)* |
| **Periodo** | **1958Q1 → 2026Q2** |
| **Representa bien** | El comportamiento de las primas de tamaño y valor |
| **NO representa** | Un producto invertible: **son carteras académicas sin costes, sin impuestos y sin límites de liquidez**. Y el Robeco es gestión activa, no una cartera de factor |
| **Confianza** | 🟢 **Alta para la prima** · 🟡 **media para nuestros vehículos** |

---

# 2. Módulo con cobertura PARCIAL

## ⚓ Freno — **solo la pata monetaria**

| | |
|---|---|
| **Función** | Estabilizar y exponer a factores distintos de los activos productivos |
| **Proxy disponible** | Letra del Tesoro EEUU a 1 mes |
| **Fuente** | Kenneth French *(Ibbotson hasta 2024-05; ICE BofA 1-Month T-Bill después)* |
| **Periodo** | 1958Q1 → 2026Q2 |
| **Representa bien** | Los **6 de 9 puntos** que son fondo monetario *(AXA Trésor Court Terme)* |
| **NO representa** | 🔴 **Los 3 puntos de renta fija con duración.** No hay serie de retorno total de bonos largos en las fuentes descargadas |
| **Por qué no se aproxima** | Construir retornos de bonos a partir de rendimientos exige supuestos de duración y convexidad: **sería inventar una serie**, no medirla |
| **Confianza** | 🟡 **Media, y solo para la pata monetaria.** **H4 no puede evaluarse completa** |

## 🥇 Activos Reales — **solo oro, y solo desde 1971Q4**

| | |
|---|---|
| **Función** | Comportamiento ligado a inflación y confianza monetaria |
| **Proxy disponible** | Precio del oro, fixing PM de Londres, USD |
| **Fuente** | **LBMA** *(fuente primaria oficial)* |
| **Periodo** | Serie desde 1968-04 *(precio de mercado privado válido desde el origen)*; **utilizada desde 1971Q4 por decisión de alcance** |
| **Por qué se recorta** | ⚠️ **Por homogeneidad de régimen, no por falta de dato.** Desde marzo de 1968, disuelto el London Gold Pool, existía un **sistema de dos niveles** con **mercado privado a precio libre**; el precio oficial de 35 $/onza regía solo entre autoridades monetarias. Se excluye el tramo anterior a la **suspensión de la convertibilidad del dólar en oro (15-ago-1971)** para no mezclar dos regímenes distintos *(fuente: Federal Reserve History)* |
| **Representa bien** | El oro físico — que es exactamente lo que tenemos *(ETC de oro asignado)*. **Es el proxy más fiel de toda la matriz** |
| **NO representa** | 🔴 **El cobre** *(2 de los 9 puntos)*: sin serie pública gratuita con historia larga |
| **Confianza** | 🟢 **Alta para el oro** *(9 episodios en la caja 4, robusto a las dos clasificaciones)* · ⛔ **nula para el cobre** |

---

# 3. Módulos SIN cobertura — declarados, no rellenados

## 🌍 Emergentes — ⛔ **no evaluable**

| | |
|---|---|
| **Función** | Exposición estratégica diferenciada a economías emergentes |
| **Proxy** | **Ninguno disponible** |
| **Por qué** | Los índices de emergentes no existen antes de finales de los ochenta. **No cubrirían ninguno de los episodios de inflación alta de los años setenta**, que son justo los que interesan |
| **Qué NO se hace** | **No se sustituye por acciones de EEUU** — sería exactamente lo contrario de lo que el módulo representa |
| **Confianza** | ⛔ **H6 no evaluable** |

## 💥 Asimetría — ⛔ **no evaluable**

| | |
|---|---|
| **Función** | Opcionalidad de alto potencial con pérdida acotada por tamaño |
| **Proxy** | **Ninguno** |
| **Por qué** | **Bitcoin existe desde 2009.** No hay historia anterior, y **no se inventa** |
| **Qué cubre lo poco que hay** | Ni los setenta, ni 2000-02, ni 2008. Solo una parte del periodo reciente, insuficiente para la regla de consistencia |
| **Confianza** | ⛔ **Nula.** El módulo se justifica por diseño *(tamaño acotado)*, **no por evidencia histórica de régimen** |

## 💧 Reserva — ⚪ **no aplica**

Es **capacidad operativa**, no una fuente de retorno. H8 se declaró desde el principio como
no comprobable con datos de rentabilidad.

---

# 4. Cuadro resumen

| Módulo | Peso | Cobertura | Desde | Confianza |
|---|---:|---|---|---|
| 🚀 Motor | 44% | ✅ Completa | 1958Q1 | 🟢 Alta |
| 🌿 Defensivos | 12% | ✅ Completa | 1958Q1 | 🟡 Media *(rebajada por robustez en caja 3)* |
| ⚡ Aceleración | 12% | ✅ Completa | 1958Q1 | 🟢 Alta para la prima |
| ⚓ Freno | 9% | ⚠️ **Parcial** *(6 de 9 puntos)* | 1958Q1 | 🟡 Media |
| 🥇 Activos Reales | 9% | ⚠️ **Parcial** *(7 de 9 puntos)* | 1971Q4 | 🟢 Alta *(oro)* |
| 🌍 Emergentes | 7% | ⛔ **Ninguna** | — | ⛔ |
| 💥 Asimetría | 4% | ⛔ **Ninguna** | — | ⛔ |
| 💧 Reserva | 3% | ⚪ No aplica | — | — |

## 4.1 La cifra que el capítulo debe declarar

> **Del 97% de la cartera asignado a módulos, el análisis histórico cubre con datos
> suficientes el 68%** *(Motor 44 + Defensivos 12 + Aceleración 12)*, **parcialmente el
> 18%** *(Freno 9 + Reales 9, con 5 de esos 18 puntos sin serie)*, **y no cubre en absoluto
> el 11%** *(Emergentes 7 + Asimetría 4)*.

**Consecuencia directa:** **H7 —«cada caja tiene algo que funcione»— solo puede afirmarse
sobre los módulos evaluables, nunca sobre la cartera completa.** El capítulo 19 lo dirá con
esas palabras, y el tribunal tiene derecho a saberlo antes de preguntarlo.
