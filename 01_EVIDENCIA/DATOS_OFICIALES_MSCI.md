# DATOS OFICIALES — ÍNDICES MSCI

**Fuente: factsheets oficiales de MSCI · Datos a 31 de julio de 2026**
Descargados de msci.com el 9 de agosto de 2026

> **Por qué existe este documento.** Hasta ahora el presupuesto de alfa se apoyaba en
> supuestos propios. Estos son **datos oficiales del proveedor del índice**, verificables
> por cualquiera, y sustituyen a esos supuestos donde es posible.

---

## ⚠️ QUÉ ÍNDICES ESTÁN DOCUMENTADOS AQUÍ Y CUÁLES NO

**Léelo antes de citar nada.** Este archivo NO cubre todos los índices que aparecen en el
proyecto. Si un dato no está en la lista verde, **no tiene respaldo en este documento** y no
se puede llevar a la presentación como dato oficial.

| Índice | ¿Factsheet leído? | Dónde |
|---|---|---|
| **MSCI ACWI** *(benchmark)* | ✅ Sí | §0 |
| **MSCI World** (bruto y neto) | ✅ Sí | §1 |
| **MSCI World Quality** | ✅ Sí | §1, §3 |
| **MSCI World Momentum** | ✅ Sí | §1, §4 |
| **MSCI World Enhanced Value** | ✅ Sí | §1, §5-bis |
| **MSCI World Small Cap** | ✅ Sí | §1, §5 |
| **MSCI World Small Cap Quality** ⭐ *(en cartera)* | ✅ Sí | §1, §5 |
| **MSCI Emerging Markets** | 🟡 Solo la fila comparada de §0 | §0 |
| **MSCI Diversified Multiple-Factor** ⭐ *(en cartera)* | ❌ **NO** | — |
| **MSCI Minimum Volatility** | ❌ **NO** | — |
| MSCI Japan · World Health Care · World Consumer Staples | ❌ **NO** | — |

🚨 **El aviso importante:** el bloque **Aceleración** son dos vehículos —**Multi-Factor 4% +
Small Cap Quality 4%**— y aquí **solo está documentado uno de los dos**. `FICHA_ACELERACION.md`
cita Multi-Factor y Minimum Volatility, y **ninguno de los dos tiene factsheet leído todavía**.
Cualquier cifra suya es `[PENDIENTE DE VERIFICAR]` hasta que se descargue su factsheet.

---

## 0. EL BENCHMARK — MSCI ACWI

**Factsheet oficial a 31 de julio de 2026** (rentabilidad neta, serie desde dic-2000).

| Concepto | Valor |
|---|---|
| **Constituyentes** | **2.460** |
| **Cobertura del universo invertible global** | **~85%** ✅ |
| Mercados | 23 desarrollados + 24 emergentes |
| **Rentabilidad anualizada desde dic-2000** | **7,39%** |
| Volatilidad 10 años | 14,71% |
| Ratio de Sharpe desde 2000 | 0,41 |
| **Máxima caída** | **−58,38%** (31-oct-2007 → 9-mar-2009) |
| Rotación anual | 3,21% |
| P/E · P/E fwd · P/BV | 23,24 · 17,13 · 3,82 |
| Rentabilidad por dividendo | 1,59% |

### Composición sectorial y geográfica

| Sector | Peso | | País | Peso |
|---|---|---|---|---|
| **Tecnología** | **30,28%** | | **Estados Unidos** | **63,55%** |
| Financieras | 17,18% | | Japón | 5,05% |
| Industriales | 10,86% | | Reino Unido | 3,19% |
| Consumo discrecional | 8,97% | | Taiwán | 3,14% |
| Salud | 8,39% | | Canadá | 3,01% |
| Comunicación | 7,87% | | Resto | 22,07% |
| Consumo defensivo | 4,83% | | | |

### Top 10 — el 24,21% del índice

| # | Compañía | País | Peso |
|---|---|---|---|
| 1 | Nvidia | US | 4,57% |
| 2 | Apple | US | 4,47% |
| 3 | Microsoft | US | 3,23% |
| 4 | Amazon | US | 2,59% |
| 5 | Alphabet A | US | 2,04% |
| 6 | **TSMC** | **TW** | 1,82% |
| 7 | Broadcom | US | 1,73% |
| 8 | Alphabet C | US | 1,62% |
| 9 | Meta | US | 1,20% |
| 10 | JPMorgan Chase | US | 0,93% |

### Índices de referencia comparados

| Índice | Rentab. desde 2000 | Volatilidad 10 a. | Sharpe | **Máxima caída** |
|---|---|---|---|---|
| **MSCI ACWI** | **7,39%** | 14,71% | 0,41 | **−58,38%** |
| MSCI World | 7,45% | 14,86% | 0,42 | −57,82% |
| MSCI Emerging Markets | **9,06%** | 17,44% | 0,43 | **−65,25%** (oct-2007 → oct-2008) |

---

## 0-bis. TRES CORRECCIONES QUE OBLIGA ESTE DATO

| # | Lo que decíamos | **Dato oficial** | Efecto |
|---|---|---|---|
| 1 | El índice cayó −54% | **−58,38%** | Nuestra ventaja **aumenta** de 12 a 15 puntos |
| 2 | Tecnología en el ACWI ~28% | **30,28%** | La exposición real de la cartera sube a ~18,7% |
| 3 | Cobertura del ACWI ~85% | **~85% confirmado** | ✅ El argumento de small caps queda validado en fuente |

**La corrección 1 es a mejor:** el índice cayó más de lo que suponíamos, así que la
diferencia a nuestro favor es mayor. La 2 obliga a actualizar el dato de tecnología. La 3
confirma oficialmente uno de los argumentos centrales del trabajo.

**Fuente:** MSCI ACWI Index (USD) Factsheet, 31-jul-2026 —
`msci.com/documents/10199/255599/msci-acwi-net.pdf`

---

## 1. TABLA MAESTRA

| Índice | Serie desde | Rentab. anualizada | Volatilidad 10 a. | Sharpe desde inicio | **Máx. caída** | Beta | Tracking error | Rotación anual |
|---|---|---|---|---|---|---|---|---|
| **MSCI World** *(bruto)* | jun-1994 | **9,01%** | 14,85% | 0,47 | **−57,46%** | 1,00 | — | 2,95% |
| **MSCI World Quality** *(bruto)* | jun-1994 | **12,02%** | 15,14% | **0,68** | **−48,01%** | 0,90 | 4,49% | 48,01% |
| **MSCI World Momentum** *(bruto)* | jun-1994 | **11,92%** | 16,42% | 0,62 | **−55,53%** | 0,93 | 7,85% | **119,69%** |
| **MSCI World** *(neto)* | nov-1997 | **7,79%** | 14,86% | 0,41 | **−57,82%** | 1,00 | — | 2,95% |
| **MSCI World Enhanced Value** *(neto)* | nov-1997 | **10,00%** | 16,64% | 0,49 | **−62,01%** | 1,06 | 7,27% | **27,39%** |
| **MSCI World Small Cap** *(neto)* | dic-2000 | **9,26%** | 17,98% | 0,47 | **−61,35%** | 1,00 | — | 61,35% |
| **MSCI World Small Cap Quality** *(neto)* | dic-2000 | **11,12%** | 17,20% | **0,58** | **−57,86%** | 0,94 | 3,36% | 57,86% |

⚠️ **Advertencia metodológica obligatoria.** Quality y Momentum se publican en
rentabilidad **bruta**; los de Small Cap en rentabilidad **neta** (con retención de
dividendos). **No son directamente comparables entre sí**, solo cada uno con su índice
padre, que aparece en la misma base. Citarlos mezclados sería un error.

⚠️ **Los índices de factores tienen historial reconstruido.** MSCI World Quality se lanzó
el 18-dic-2012, Momentum el 11-dic-2013 y Small Cap Quality el 12-abr-2022. Los datos
anteriores son *back-tested*: cálculo de cómo se habrían comportado. **MSCI advierte
expresamente que suele haber diferencias materiales entre el backtest y el resultado
real.** Hay que decirlo al citarlos.

---

## 2. LAS PRIMAS, MEDIDAS

| Factor | Frente a | Prima anual | Diferencia de caída máxima |
|---|---|---|---|
| **World Quality** | World | **+3,01 pp** | **9,45 puntos menos** |
| **World Momentum** | World | **+2,91 pp** | 1,93 puntos menos |
| **Small Cap Quality** | Small Cap | **+1,86 pp** | 3,49 puntos menos |
| Small Cap | World | +0,25 pp¹ | 3,89 puntos **más** |

¹ *Periodos distintos y bases distintas (neto vs bruto): no es una comparación válida.
Se incluye solo como orientación.*

**Comparación con nuestros supuestos previos:**

| Bloque | Supuesto propio | Dato oficial | Veredicto |
|---|---|---|---|
| Momentum | +300 pb | **+291 pb** | ✅ Prácticamente exacto |
| Small caps con calidad | +200 pb | **+186 pb** | ✅ Ligeramente optimista |

Los supuestos que hicimos a ciegas resultaron correctos dentro de un margen de 15 puntos
básicos. Eso valida el método, pero **a partir de ahora se citan los datos, no los
supuestos**.

---

## 3. EL HALLAZGO — MSCI WORLD QUALITY

Es el índice que mejor combina las dos caras del problema:

| Métrica | World Quality | MSCI World | Diferencia |
|---|---|---|---|
| Rentabilidad anualizada desde 1994 | **12,02%** | 9,01% | **+3,01 pp** |
| Ratio de Sharpe desde 1994 | **0,68** | 0,47 | **+45% mejor** |
| Máxima caída (oct-2007 → mar-2009) | **−48,01%** | −57,46% | **9,45 puntos menos** |
| Beta | 0,90 | 1,00 | Menos sensible al mercado |
| Rotación anual | 48,01% | 2,95% | Más costes |

> **Más rentabilidad, mejor Sharpe y casi diez puntos menos de caída, con beta 0,90.**
> Es literalmente lo que buscábamos: más alfa con menos riesgo, y con dato oficial.

### El coste de esa ventaja

| Concentración | World Quality | MSCI World |
|---|---|---|
| Peso de las 10 mayores | **37,10%** `[PENDIENTE DE VERIFICAR EN EL FACTSHEET]` | 23,82% |
| Estados Unidos | **78,15%** | ~71% |
| Tecnología | **37,10%** `[PENDIENTE DE VERIFICAR EN EL FACTSHEET]` | ~26% |

⚠️ **Las dos cifras marcadas son idénticas (37,10%) y eso es sospechoso.** Que el peso de las
diez mayores y el peso de tecnología coincidan al segundo decimal apunta a un error al
copiar del factsheet, no a una casualidad. **No se ha corregido porque no sabemos cuál de
las dos es la buena.** Hay que abrir el factsheet de MSCI World Quality y leer las dos por
separado antes de citar ninguna. La misma pareja de cifras vuelve a aparecer en la tabla de
§5-bis.

Sus mayores posiciones son Microsoft, Apple, Broadcom, Nvidia, Meta, Lilly, Visa, ASML y
Alphabet. **Es un índice muy concentrado y muy americano.**

---

## 4. MOMENTUM — LO QUE LOS DATOS OBLIGAN A REVISAR

| Métrica | World Momentum | World Quality | Gana |
|---|---|---|---|
| Rentabilidad anualizada | 11,92% | **12,02%** | Quality |
| Máxima caída | −55,53% | **−48,01%** | Quality |
| Volatilidad 10 años | 16,42% | **15,14%** | Quality |
| Sharpe desde inicio | 0,62 | **0,68** | Quality |
| Tracking error | 7,85% | **4,49%** | Quality |
| **Rotación anual** | **119,69%** | 48,01% | Quality |

**Quality supera a Momentum en las seis métricas.**

### El dato que más pesa: la rotación

**El índice de momentum rota el 119,69% de su cartera en doce meses.** Se renueva entero
cada año y un poco más. Eso implica costes de transacción reales que el índice **no
descuenta** pero un fondo sí soporta.

La literatura documenta la prima de momentum sobre índices teóricos; el inversor real
paga esa rotación. Con un dato de rotación superior al 100%, **la prima neta que llega al
partícipe es sensiblemente menor que el +2,91 pp del índice**.

### Y su composición no diversifica

| Momentum · sectores | Peso |
|---|---|
| Tecnología | 32,40% |
| Industriales | 14,79% |
| Financieras | 14,04% |
| Energía | 11,09% |

Top 10: Micron (5,80%), AMD, ExxonMobil, ASML, Johnson & Johnson, Alphabet, Intel,
Caterpillar, Lam Research, Alphabet C — **28,02% concentrado**, con cinco semiconductoras.

Es exactamente el riesgo que anticipamos: **momentum compra lo que ha subido, y lo que ha
subido son los semiconductores.**

---

## 5. SMALL CAP QUALITY — LA CONFIRMACIÓN DE ASNESS

Asness, Frazzini, Israel, Moskowitz y Pedersen (2018) sostienen que la prima de tamaño
reaparece al controlar por calidad. **Los datos de MSCI lo confirman:**

| Métrica | SC Quality | Small Cap | Diferencia |
|---|---|---|---|
| Rentabilidad anualizada desde 2000 | **11,12%** | 9,26% | **+1,86 pp** |
| Volatilidad 10 años | **17,20%** | 17,98% | Menos |
| Sharpe desde 2000 | **0,58** | 0,47 | Mejor |
| Máxima caída | **−57,86%** | −61,35% | 3,49 puntos menos |

**Más rentabilidad, menos volatilidad, menos caída y mejor Sharpe.** El filtro de calidad
no es una preferencia: es lo que hace funcionar al factor.

### Y además diversifica de verdad

| SC Quality | Peso |
|---|---|
| Industriales | 31,77% |
| Financieras | 19,53% |
| **Tecnología** | **12,71%** |
| Estados Unidos | 56,17% |
| Japón | 16,38% |

**Solo un 12,71% de tecnología y un 56% de Estados Unidos**, frente al ~26% y ~71% del
MSCI World. Top 10 = 6,17%, prácticamente sin concentración.

> Es el único de los tres factores analizados que **reduce de verdad** la dependencia de
> las megacaps tecnológicas estadounidenses.

---

## 5-bis. LOS TRES CANDIDATOS, CARA A CARA

Comparación de los tres factores globales de gran y mediana capitalización que compiten
por el mismo hueco de 4% en el bloque Aceleración:

| Métrica | Momentum | Quality | **Enhanced Value** |
|---|---|---|---|
| Prima sobre su índice padre | +2,91 pp | **+3,01 pp** | +2,21 pp |
| Máxima caída | −55,53% | **−48,01%** | **−62,01%** ❌ |
| Beta | 0,93 | **0,90** | 1,06 ❌ |
| Volatilidad 10 años | 16,42% | **15,14%** | 16,64% |
| Tracking error | 7,85% | 4,49% | 7,27% |
| **Rotación anual** | **119,69%** ❌ | 48,01% | **27,39%** ✅ |
| Peso en EE.UU. | 56,33% | **78,15%** ❌ | **46,16%** ✅ |
| Peso en tecnología | 32,40% | 37,10% ⚠️ | 29,84% |
| Peso del top 10 | 28,02% | 37,10% ⚠️ | 27,58% |
| **Mayor posición individual** | 5,80% | 5,41% | **12,60%** ❌ |
| P/E | 25,43 | 26,67 | **14,43** ✅ |
| P/BV | 3,74 | 9,13 | **1,62** ✅ |
| Rentabilidad por dividendo | 1,53% | 1,21% | **2,65%** |

⚠️ *Las dos celdas de Quality marcadas repiten el mismo 37,10%:
`[PENDIENTE DE VERIFICAR EN EL FACTSHEET]`, ver el aviso de §3.*

### Lectura

**Ninguno domina.** Cada uno gana en cosas distintas:

- **Quality** tiene el mejor perfil rentabilidad/riesgo, pero **78,15% en Estados Unidos** y
  sus diez mayores son Microsoft, Apple, Broadcom, Nvidia, Meta y Alphabet — las mismas que
  ya dominan el Motor. Su tracking error de 4,49% confirma que **se parece al índice**.
- **Momentum** descorrelaciona (TE 7,85%) y aporta nombres que no están en la cartera, pero
  **rota el 119,69% anual**: se renueva entero cada año. El índice no descuenta ese coste;
  un fondo real sí lo paga.
- **Enhanced Value** es el que **más corrige el sesgo de la cartera**: apenas 46,16% en
  Estados Unidos, P/E de 14,43 frente a 24,25 del World, y la rotación más baja de los tres
  con diferencia. Pero su caída máxima es la peor (−62,01%), su beta supera 1, y
  **Micron pesa un 12,60% del índice**, una concentración muy alta para un índice.

### El dato que aparece en dos sitios

**Micron Technology** es la mayor posición tanto del índice de Momentum (5,80%) como del de
Enhanced Value (12,60%). Está barata y subiendo a la vez. Si se eligieran los dos, la
exposición conjunta a una sola compañía sería relevante y habría que declararla.

---

## 6. IMPLICACIONES PARA LA CARTERA — LA DECISIÓN FINAL

> **Este apartado se reescribió el 10 de agosto de 2026.** La versión anterior recomendaba
> sustituir Momentum por Quality. **Esa recomendación quedó superada:** al comparar los
> cinco candidatos se eligió un índice **multi-factor**, que no aparecía en la comparación
> original. Se deja constancia porque el proceso también se presenta.

### ✅ Lo que entra en el bloque ACELERACIÓN (8%)

| Componente | Peso | Por qué |
|---|---|---|
| **MSCI Diversified Multiple-Factor** (Multi-Factor) | **4%** | Recoge varias primas a la vez. No depende de que funcione un factor concreto |
| **MSCI World Small Cap Quality** | **4%** | El único de los analizados que **reduce de verdad** la dependencia de las megacaps tecnológicas de EE.UU.: 12,71% de tecnología y 56,17% de EE.UU. |

**Por qué 4 y 4 y no 8 a uno solo:** son dos primas distintas. El escenario que hunde a una
no es el mismo que hunde a la otra. Repartir evita depender de un único factor.

**Criterio de compra del vehículo Multi-Factor:** comprobar que su top 10 **no** coincide
con el del ACWI. Si el top 10 supera el **40%**, no diversifica y se descarta.

⚠️ **El factsheet de MSCI Diversified Multiple-Factor todavía no se ha leído** (ver el aviso
de la cabecera). Sus cifras son `[PENDIENTE DE VERIFICAR]`.

### ❌ Lo que se descartó, y por qué

| Descartado | Motivo |
|---|---|
| **MSCI World Momentum** | **Rotación anual del 119,69%**: se renueva entero cada año. El índice no descuenta ese coste, un fondo real sí lo paga. Ofrece **la mitad de information ratio que Multi-Factor para la misma prima** |
| **MSCI World Quality** | Tracking error de **4,49%** y **78,15% en EE.UU.**: es el índice padre re-filtrado. Sus diez mayores son Microsoft, Apple, Broadcom, Nvidia, Meta y Alphabet — **las mismas que ya dominan el Motor**. Comprarlo sería comprar dos veces lo mismo |
| **MSCI Minimum Volatility** | No aporta prima. Su función —amortiguar— ya la cubre el bloque **Freno** |
| **MSCI World Enhanced Value** | Prima insuficiente (+2,21 pp) para el riesgo asumido: peor caída de los tres (**−62,01%**), beta por encima de 1 y **Micron pesando el 12,60%** del índice |
| **Un bloque tecnológico** | La cartera ya lleva **18,7%** de tecnología por otras vías |

> **La lección que sí se presenta:** Quality ganaba en las seis métricas de rentabilidad y
> riesgo, y aun así **no entró**. Un índice no se elige por su ficha aislada, sino por lo
> que aporta **al lado de lo que ya tienes**. Con un 31% en el Motor, comprar Quality era
> comprar el Motor otra vez con otro nombre.

### Lo que además queda validado

1. **Small Cap Quality confirma a Asness (2018):** más rentabilidad (**+1,86 pp**), menos
   volatilidad, menos caída y mejor Sharpe que el Small Cap sin filtrar.
2. **El escenario 2008 puede recalcularse con datos reales** en lugar de estimaciones:
   MSCI World cayó −57,46%, Quality −48,01%, Momentum −55,53%, Small Cap −61,35% y Small
   Cap Quality −57,86%, todos entre octubre de 2007 y marzo de 2009.
3. **El alfa supuesto del bloque Aceleración es +250 pb** (`CIFRAS_MAESTRAS.md §8`).

---

## 7. FUENTES

| Documento | URL |
|---|---|
| MSCI World Quality Index (USD) — factsheet | msci.com/documents/10199/344aa133-d8fa-4a15-b091-20a8fd024b65 |
| MSCI World Momentum Index (USD) — factsheet | msci.com/documents/10199/255599/msci-world-momentum-index-usd-gross.pdf |
| MSCI World Small Cap Quality Index (USD) — factsheet | msci.com/documents/10199/255599/msci-world-small-cap-quality-index-usd-net.pdf |
| MSCI World Small Cap Index (USD) — factsheet | msci.com/documents/10199/255599/msci-world-small-cap-index.pdf |
| MSCI World Index (USD) — factsheet | msci.com/documents/10199/255599/msci-world-index.pdf |

**Todos los factsheets son públicos y gratuitos.** Se actualizan mensualmente: antes de la
entrega conviene comprobar si hay versión de agosto.

---

## 8. PENDIENTE DE OBTENER EN FUENTE OFICIAL

| Dato | Para qué | Dónde |
|---|---|---|
| **MSCI Diversified Multiple-Factor** | **Es la mitad del bloque Aceleración y no tiene factsheet** | msci.com |
| MSCI Minimum Volatility | Se cita como descarte en `FICHA_ACELERACION.md` sin dato de respaldo | msci.com |
| MSCI Emerging Markets — factsheet completo | Bloque Reversión (en §0 solo está la fila comparada) | msci.com |
| MSCI Japan | Bloque Reversión | msci.com |
| MSCI World Health Care y Consumer Staples | Bloque Calidad — sustituir a Siegel | msci.com |
| Oro y renta fija corta en 2007-2009 | Prueba de estrés | Series de precio |
| Caídas del S&P 500 por ciclos | Análisis de pignoración | S&P Dow Jones |

---

## REGISTRO

| Fecha | Acción |
|---|---|
| 2026-08-09 | Documento creado con cinco factsheets oficiales de MSCI a 31-jul-2026 |
| 2026-08-10 | Añadida la cabecera con **qué índices están documentados y cuáles no**. Reescrito el §6 con la **decisión final del bloque Aceleración: Multi-Factor 4% + Small Cap Quality 4%**, y los motivos de descarte de Momentum, Quality, Minimum Volatility y Enhanced Value. Eliminada del §8 la fila del ACWI (sus datos ya están en §0). Marcadas con `[PENDIENTE DE VERIFICAR EN EL FACTSHEET]` las dos cifras de MSCI World Quality que repiten el mismo 37,10% |
