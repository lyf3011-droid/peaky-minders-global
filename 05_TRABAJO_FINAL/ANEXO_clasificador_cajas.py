# CLASIFICADOR DE CUATRO CAJAS — implementa R1-R8 del dossier v2
# Sin librerias externas. Fuentes: FRED (GDPC1 = BEA PIB real; CPIAUCSL = BLS IPC).
import io, sys, csv, statistics as st
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
S = "C:/Users/fgonz/AppData/Local/Temp/claude/C--Users-fgonz-Desktop-claude-tradingview/6e19bdff-01a2-4f07-b218-a69f858695bb/scratchpad/"
OUT = "C:/Users/fgonz/Desktop/claude-apps/claude-cartera-antonio/05_TRABAJO_FINAL/"
FECHA_DESCARGA = "2026-08-14"

def leer(f):
    d = {}
    for r in csv.DictReader(open(S + f, encoding='utf-8')):
        k = list(r.keys()); v = r[k[1]]
        if v not in ('.', '', None):
            d[r[k[0]]] = float(v)
    return d

def q(fecha):           # 'YYYY-MM-DD' -> (anio, trimestre)
    a, m, _ = fecha.split('-')
    return (int(a), (int(m) - 1) // 3 + 1)

# --- R2: PIB real trimestral -> variacion interanual ---
gdp = {q(k): v for k, v in leer('gdpc1.csv').items()}
# --- R3 + cierre 2.4: IPC mensual -> media del trimestre -> interanual ---
cpi_m = leer('cpi.csv')
buckets = {}
for k, v in cpi_m.items():
    buckets.setdefault(q(k), []).append(v)
cpi = {k: sum(v) / len(v) for k, v in buckets.items() if len(v) == 3}  # trimestres completos

def yoy(serie):
    out = {}
    for (a, t), v in serie.items():
        prev = serie.get((a - 1, t))
        if prev:
            out[(a, t)] = (v / prev - 1) * 100
    return out

g, i = yoy(gdp), yoy(cpi)
trims = sorted(set(g) & set(i))
print(f"Trimestres con ambas variables: {len(trims)}  [{trims[0]} .. {trims[-1]}]")

VENT = 40
def clasificar(func_umbral):
    filas = []
    for n, t in enumerate(trims):
        if n < VENT:                      # cierre 2.2: sin ventana completa, no se clasifica
            continue
        prev = trims[n - VENT:n]          # R4: 40 anteriores, EXCLUYENDO el clasificado
        hg = [g[p] for p in prev]; hi = [i[p] for p in prev]
        ug, ui = func_umbral(hg), func_umbral(hi)
        alto_g = g[t] >= ug               # cierre 2.3: empate = alto
        alto_i = i[t] >= ui
        caja = 1 if (alto_g and not alto_i) else 2 if (alto_g and alto_i) else 3 if (not alto_g and not alto_i) else 4
        # R6: marca informativa, NO altera la caja
        cerca = (abs(g[t] - ug) < 0.20 * st.pstdev(hg)) or (abs(i[t] - ui) < 0.20 * st.pstdev(hi))
        filas.append({'t': t, 'g': g[t], 'i': i[t], 'ug': ug, 'ui': ui, 'caja': caja, 'cerca': cerca})
    return filas

principal = clasificar(st.median)   # R4 principal: MEDIANA movil de 40
alterna  = clasificar(lambda x: sum(x) / len(x))  # robustez: MEDIA movil de 10 anios

NOM = {1: 'Expansión desinflacionaria', 2: 'Recalentamiento',
       3: 'Recesión desinflacionaria', 4: 'Estanflación'}
n = len(principal)
print(f"Clasificados: {n}  desde {principal[0]['t']} hasta {principal[-1]['t']}")

# --- reparto por caja ---
rep = {}
for f in principal:
    rep[f['caja']] = rep.get(f['caja'], 0) + 1
print("\nREPARTO PRINCIPAL (mediana 40T)")
for c in (1, 2, 3, 4):
    print(f"  Caja {c} {NOM[c]:<28} {rep.get(c,0):>4} trim  {rep.get(c,0)/n*100:>5.1f}%")

# --- desacuerdo ---
dif = [(a['t'], a['caja'], b['caja']) for a, b in zip(principal, alterna) if a['caja'] != b['caja']]
print(f"\nDESACUERDO principal vs alternativa: {len(dif)} de {n} = {len(dif)/n*100:.1f}%")
rep2 = {}
for f in alterna:
    rep2[f['caja']] = rep2.get(f['caja'], 0) + 1
for c in (1, 2, 3, 4):
    print(f"  Caja {c}: principal {rep.get(c,0):>3}  alternativa {rep2.get(c,0):>3}")

cerca_n = sum(1 for f in principal if f['cerca'])
print(f"\nMarca de proximidad (informativa): {cerca_n} trim = {cerca_n/n*100:.1f}%")

# --- R5: episodios (>=2 trimestres consecutivos) ---
eps, run = [], [principal[0]]
for f in principal[1:]:
    if f['caja'] == run[-1]['caja']:
        run.append(f)
    else:
        eps.append(run); run = [f]
eps.append(run)
episodios = [e for e in eps if len(e) >= 2]
aislados  = [e[0] for e in eps if len(e) == 1]
print(f"\nEpisodios (>=2T): {len(episodios)}   Trimestres aislados: {len(aislados)}")
for c in (1, 2, 3, 4):
    print(f"  Caja {c}: {sum(1 for e in episodios if e[0]['caja']==c)} episodios")

def et(t): return f"{t[0]}Q{t[1]}"
print("\nEPISODIOS DE CAJA 4 (estanflación):")
for e in episodios:
    if e[0]['caja'] == 4:
        print(f"  {et(e[0]['t'])}–{et(e[-1]['t'])}  ({len(e)}T)")

print("\nPRUEBA EXTERNA — trimestres 1973Q1..1975Q4:")
for f in principal:
    if (1973, 1) <= f['t'] <= (1975, 4):
        alt = next(b['caja'] for b in alterna if b['t'] == f['t'])
        print(f"  {et(f['t'])}  PIB {f['g']:+6.2f} (umb {f['ug']:+5.2f})  IPC {f['i']:+6.2f} (umb {f['ui']:+5.2f})  -> caja {f['caja']} [alt {alt}]{'  ~cerca' if f['cerca'] else ''}")

print("\nOTROS EPISODIOS CANDIDATOS DEL DOSSIER:")
for lab, a, b in [('1979-1982 Volcker',(1979,1),(1982,4)), ('1990-91',(1990,1),(1991,4)),
                  ('1995-99',(1995,1),(1999,4)), ('2000-02 puntocom',(2000,1),(2002,4)),
                  ('2007-09 financiera',(2007,1),(2009,4)), ('2010-19',(2010,1),(2019,4)),
                  ('2020 covid',(2020,1),(2020,4)), ('2021-23 post-covid',(2021,1),(2023,4)),
                  ('2024-26 reciente',(2024,1),(2026,4))]:
    sub = [f for f in principal if a <= f['t'] <= b]
    seq = ' '.join(f"{et(f['t'])}:{f['caja']}" for f in sub)
    print(f"  {lab:<20} {seq}")

# --- verificaciones de integridad (auditoría §4) ---
print("\nINTEGRIDAD")
print(f"  suma cajas == clasificados: {sum(rep.values()) == n}")
print(f"  ventanas solo pasado: True (por construccion trims[n-40:n])")
print(f"  misma funcion para ambas clasificaciones: True")

# --- volcado CSV completo ---
with open(OUT + 'ANEXO_CLASIFICACION_CAJAS.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['trimestre','pib_real_yoy','umbral_pib_mediana40','ipc_yoy','umbral_ipc_mediana40',
                'caja_principal','caja_alternativa_media40','cerca_umbral'])
    for a, b in zip(principal, alterna):
        w.writerow([et(a['t']), f"{a['g']:.3f}", f"{a['ug']:.3f}", f"{a['i']:.3f}", f"{a['ui']:.3f}",
                    a['caja'], b['caja'], int(a['cerca'])])
print(f"\nCSV escrito: ANEXO_CLASIFICACION_CAJAS.csv ({n} filas)  descarga {FECHA_DESCARGA}")
