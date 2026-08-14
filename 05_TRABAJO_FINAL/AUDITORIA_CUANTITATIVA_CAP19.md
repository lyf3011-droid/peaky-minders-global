# 🔬 AUDITORÍA CUANTITATIVA — RESULTADOS DEL CAPÍTULO 19

## 14 de agosto de 2026 · verificación independiente de los cálculos

> **Objetivo:** comprobar que los números publicados son correctos, que no hay
> anticipación de información, y que las conclusiones no dependen de detalles de
> implementación no declarados. **Se ejecutó con código independiente del original.**

---

# 1. Comprobaciones superadas

| # | Prueba | Resultado |
|---|---|---|
| **A1** | **Datos ausentes en las series de Fama-French** *(código −99,99)* | ✅ **0 de 1.200 meses**. No se descartó ni un dato: el filtro defensivo del script no llegó a actuar |
| **A2** | **Recálculo independiente del Motor** por caja, rehaciendo la cadena mensual → trimestre → caja | ✅ **Coincidencia exacta** con lo publicado: +12,36/+9,83 · +10,18/+5,54 · +18,04/+15,76 · +6,39/+0,95 |
| **A4** | **Tamaños de muestra** | ✅ 273 trimestres clasificados, 273 con retorno del Motor, **218 con oro** *(coherente con el arranque en 1971Q4)* |
| **A5** | **Control de anticipación** *(look-ahead)* | ✅ La ventana termina **estrictamente en el trimestre anterior** al clasificado. Verificado sobre el dato: 1968Q2 usa hasta 1968Q1 |
| **A6** | **Coherencia interna de la inflación por caja** | ✅ El orden sale **3 < 1 < 2 < 4** *(+1,97% · +2,30% · +4,39% · +5,39%)*, exactamente como exige la construcción de las cajas. Si no saliera así, habría un error de clasificación |

---

# 2. 🔴 HALLAZGO MATERIAL — el oro es sensible al método de cálculo del precio

## 2.1 Qué se ha encontrado

Las series de acciones son **retornos verdaderos compuestos**. El oro, en cambio, se
construyó a partir de **medias de precios** *(media de los precios diarios de cada mes, y
después media de los tres meses del trimestre)*. **Las convenciones C1-C7 no especificaron
qué nivel de precio usar para un activo cotizado — es un hueco del criterio congelado.**

**Prueba de sensibilidad, con el mismo periodo y la misma clasificación:**

| Método de precio | Retorno real del oro en la caja 4 | **M3** | **M4** |
|---|---:|---:|:---:|
| **Media del trimestre** *(el usado y publicado)* | **+16,59%** | **+12,44 pp** | **7/9** |
| **Cierre del trimestre** *(control)* | **+11,19%** | **+7,34 pp** | **7/9** |

## 2.2 Qué significa — y qué no

**La conclusión de H3 no cambia: el oro sigue siendo relativamente favorable en la caja 4
con los dos métodos, y con la misma consistencia entre episodios (7 de 9).** Lo que cambia
es **la magnitud: de +12,44 a +7,34 puntos** — una diferencia importante que **no puede
publicarse sin declarar**.

La causa es conocida: promediar precios **suaviza** la serie y, en un activo con tendencia
fuerte dentro del periodo *(el oro en los años setenta)*, la media del trimestre puede
recoger más subida que la comparación de cierres. **No es un error de cálculo, es una
elección de método que no estaba declarada.**

## 2.3 Qué NO he hecho

**No he sustituido la cifra publicada por la que más me gusta.** Cambiar el método después
de ver los resultados es exactamente lo que R8 prohíbe. Las dos cifras quedan sobre la
mesa y **la decisión es del equipo**:

| Opción | Descripción |
|---|---|
| **A** | **Publicar el cierre de trimestre** como principal *(homogéneo con las series de acciones, que son retornos verdaderos)* y la media como sensibilidad |
| **B** | Mantener la media y publicar el cierre como sensibilidad, declarando el sesgo |
| **C** | Publicar **ambas cifras en el cuerpo del capítulo** siempre que se cite el oro |

> **Recomendación:** la opción **A**, por coherencia con el resto de series — pero
> **cualquiera de las tres es defendible si se declara**. La opción que **no** es
> defendible es publicar solo +12,44 sin mencionar que con cierres sale +7,34.

---

# 3. Efecto sobre las conclusiones ya publicadas

| Conclusión | ¿Afectada? |
|---|---|
| **H3 recibe apoyo** *(oro favorable en caja 4, consistente)* | ✅ **Se mantiene con los dos métodos.** Solo cambia la magnitud |
| **H3 robusta a las dos clasificaciones** | ✅ Sin cambios — la prueba de robustez afecta al umbral macro, no al precio del oro |
| **H1, H4, H5** *(los tres resultados contrarios)* | ✅ **Sin efecto**: no dependen del oro |
| **H7 · cobertura** | ✅ Sin efecto: el oro sigue cubriendo la caja 4 con los dos métodos |
| **M1/M2/M3/M4 de todos los demás activos** | ✅ **Sin efecto**: son retornos verdaderos desde el origen |

---

# 4. Limitaciones que la auditoría confirma pero no puede resolver

1. **Sincronía sin desfases** *(C1)*: mide coincidencia, no causa. Estructural.
2. **Todo en dólares** *(C4)*: un inversor en euros habría obtenido otra cosa.
3. **Proxies académicos sin costes ni impuestos**: los retornos publicados son
   **superiores** a los que habría obtenido un inversor real, en todos los activos por
   igual — el sesgo afecta a los niveles, no tanto a las comparaciones.
4. **Tres módulos sin datos**: Emergentes, Asimetría y la renta fija con duración.

---

# 5. Veredicto

> ### ✅ **Los cálculos publicados son correctos y reproducibles. No hay anticipación de información ni errores de agregación.**
> ### 🔴 **Una cifra —el M3 del oro— depende de una elección de método no declarada, y debe corregirse la declaración antes de redactar el capítulo.**

**Ninguna conclusión cualitativa del capítulo 19 cambia.** La única acción pendiente es
**decidir cuál de las tres opciones del §2.3 se adopta**, y declararla en la matriz de
series junto a C1-C7.
