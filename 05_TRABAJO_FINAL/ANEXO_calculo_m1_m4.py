# M1-M4 segun criterio congelado (R1-R8 + C1-C7). Sin librerias externas.
import io, sys, csv, json, re, zipfile, statistics as st
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
S = "C:/Users/fgonz/AppData/Local/Temp/claude/C--Users-fgonz-Desktop-claude-tradingview/6e19bdff-01a2-4f07-b218-a69f858695bb/scratchpad/"
OUT = "C:/Users/fgonz/Desktop/claude-apps/claude-cartera-antonio/05_TRABAJO_FINAL/"

def q(f):
    a, m, _ = f.split('-'); return (int(a), (int(m) - 1) // 3 + 1)
def qm(ym):                      # 'YYYYMM'
    a, m = int(ym[:4]), int(ym[4:]); return (a, (m - 1) // 3 + 1)

# ---------- clasificacion ya calculada ----------
cajas, cerca = {}, {}
for r in csv.DictReader(open(OUT + 'ANEXO_CLASIFICACION_CAJAS.csv', encoding='utf-8')):
    a, t = r['trimestre'].split('Q'); k = (int(a), int(t))
    cajas[k] = int(r['caja_principal'])
trims = sorted(cajas)

# ---------- inflacion trimestral (CPI) ----------
cpi_m = {}
for r in csv.DictReader(open(S + 'cpi.csv', encoding='utf-8')):
    k = list(r.keys()); v = r[k[1]]
    if v not in ('.', ''): cpi_m[r[k[0]]] = float(v)
b = {}
for k, v in cpi_m.items(): b.setdefault(q(k), []).append(v)
cpi = {k: sum(v)/len(v) for k, v in b.items() if len(v) == 3}
infl_q = {}                                   # inflacion del trimestre
qs = sorted(cpi)
for i in range(1, len(qs)):
    infl_q[qs[i]] = cpi[qs[i]] / cpi[qs[i-1]] - 1

# ---------- Fama-French ----------
def ff(zipn, csvn):
    txt = zipfile.ZipFile(S + zipn).read(csvn).decode('latin-1').splitlines()
    h = [i for i, l in enumerate(txt) if re.match(r'^\s*,', l)]
    cols = [c.strip() for c in txt[h[0]].strip().split(',')[1:]]
    fin = h[1] if len(h) > 1 else len(txt)
    out = {}
    for l in txt[h[0]+1:fin]:
        if re.match(r'^\s*\d{6}\s*,', l):
            p = l.split(','); ym = p[0].strip()
            out[ym] = {c: float(p[i+1]) / 100 for i, c in enumerate(cols)}
    return out

fac = ff('F-F_Research_Data_Factors_CSV.zip', 'F-F_Research_Data_Factors.csv')
ind = ff('12_Industry_Portfolios_CSV.zip', '12_Industry_Portfolios.csv')
p6  = ff('6_Portfolios_2x3_CSV.zip', '6_Portfolios_2x3.csv')

def mens(nombre):
    """retorno mensual del activo -> dict ym: r"""
    o = {}
    for ym in fac:
        try:
            if nombre == 'Motor':      r = fac[ym]['Mkt-RF'] + fac[ym]['RF']
            elif nombre == 'Monetario':r = fac[ym]['RF']
            elif nombre == 'Consumo':  r = ind[ym]['NoDur']
            elif nombre == 'Salud':    r = ind[ym]['Hlth']
            elif nombre == 'SmallCap': r = (p6[ym]['SMALL LoBM'] + p6[ym]['ME1 BM2'] + p6[ym]['SMALL HiBM']) / 3
            elif nombre == 'Valor':    r = (p6[ym]['SMALL HiBM'] + p6[ym]['BIG HiBM']) / 2
            else: continue
            if abs(r) < 1.5: o[ym] = r     # descarta -99.99 (dato ausente FF)
        except KeyError: pass
    return o

ACT = ['Motor', 'Consumo', 'Salud', 'SmallCap', 'Valor', 'Monetario']
mensual = {a: mens(a) for a in ACT}

def a_trim(m):
    agg = {}
    for ym, r in m.items():
        agg.setdefault(qm(ym), []).append(r)
    out = {}
    for k, v in agg.items():
        if len(v) == 3:
            x = 1.0
            for r in v: x *= (1 + r)
            out[k] = x - 1
    return out
trimes = {a: a_trim(m) for a, m in mensual.items()}

# ---------- oro LBMA -> trimestral, desde 1971Q4 ----------
g = json.load(open(S + 'gold_lbma.json'))
pm = {}
for x in g:
    if x['v'] and x['v'][0]:
        pm.setdefault(x['d'][:7], []).append(float(x['v'][0]))
mes_oro = {k: sum(v)/len(v) for k, v in pm.items()}       # media mensual
qo = {}
for k, v in mes_oro.items():
    qo.setdefault(q(k + '-01'), []).append(v)
nivel = {k: sum(v)/len(v) for k, v in qo.items() if len(v) == 3}
ks = sorted(nivel); oro = {}
for i in range(1, len(ks)):
    if ks[i] >= (1971, 4):                                 # exclusion patron oro
        oro[ks[i]] = nivel[ks[i]] / nivel[ks[i-1]] - 1
trimes['Oro'] = oro
ACT.append('Oro')

# ---------- M1/M2 por caja ----------
def compuesto(rs):
    x = 1.0
    for r in rs: x *= (1 + r)
    return x

NOM = {1: 'Crec. fuerte + infl. baja', 2: 'Crec. fuerte + infl. alta',
       3: 'Crec. débil + infl. baja',  4: 'Crec. débil + infl. alta'}
res = {}
for a in ACT:
    for c in (1, 2, 3, 4):
        ts = [t for t in trims if cajas[t] == c and t in trimes[a] and t in infl_q]
        if len(ts) < 4: continue
        n = len(ts)
        nom = compuesto([trimes[a][t] for t in ts]) ** (4/n) - 1
        inf = compuesto([infl_q[t] for t in ts]) ** (4/n) - 1
        real = (1 + nom) / (1 + inf) - 1
        res[(a, c)] = {'n': n, 'nom': nom, 'real': real, 'infl': inf}

print("M1/M2 — RENTABILIDAD ANUALIZADA POR CAJA (USD, 1958Q1-2026Q2; oro desde 1971Q4)\n")
print(f"{'Activo':<11}" + ''.join(f"{'caja '+str(c):>26}" for c in (1,2,3,4)))
print(f"{'':<11}" + ''.join(f"{'nominal / real':>26}" for c in (1,2,3,4)))
for a in ACT:
    fila = f"{a:<11}"
    for c in (1,2,3,4):
        r = res.get((a,c))
        fila += f"{(f'{r[chr(110)+chr(111)+chr(109)]*100:+7.2f}% / {r[chr(114)+chr(101)+chr(97)+chr(108)]*100:+7.2f}%' if r else '—'):>26}"
    print(fila)
print("\nTrimestres por caja:", {c: res[('Motor',c)]['n'] for c in (1,2,3,4)})
print("Inflación anualizada por caja:", {c: f"{res[('Motor',c)]['infl']*100:+.2f}%" for c in (1,2,3,4)})
print("Trimestres oro:", {c: res[('Oro',c)]['n'] for c in (1,2,3,4) if ('Oro',c) in res})

# ---------- M3 ----------
print("\nM3 — DIFERENCIA DE RENTABILIDAD REAL FRENTE AL MOTOR (puntos porcentuales anuales)")
print(f"{'Activo':<11}" + ''.join(f"{'caja '+str(c):>12}" for c in (1,2,3,4)))
for a in ACT:
    if a == 'Motor': continue
    fila = f"{a:<11}"
    for c in (1,2,3,4):
        r, m = res.get((a,c)), res.get(('Motor',c))
        # mismo conjunto de trimestres para comparabilidad
        if r and m:
            ts = [t for t in trims if cajas[t]==c and t in trimes[a] and t in trimes['Motor'] and t in infl_q]
            n = len(ts)
            ra = compuesto([trimes[a][t] for t in ts])**(4/n)-1
            rm = compuesto([trimes['Motor'][t] for t in ts])**(4/n)-1
            inf = compuesto([infl_q[t] for t in ts])**(4/n)-1
            d = ((1+ra)/(1+inf)-1) - ((1+rm)/(1+inf)-1)
            fila += f"{d*100:>+11.2f} "
        else: fila += f"{'—':>12}"
    print(fila)

# ---------- M4: episodios ----------
eps, run = [], [trims[0]]
for t in trims[1:]:
    if cajas[t] == cajas[run[-1]]: run.append(t)
    else: eps.append(run); run = [t]
eps.append(run)
episodios = [e for e in eps if len(e) >= 2]

def et(t): return f"{t[0]}Q{t[1]}"
print("\nM4 — CONSISTENCIA: episodios (>=2T) en que el activo supera al Motor en real")
print(f"{'Activo':<11}" + ''.join(f"{'caja '+str(c):>16}" for c in (1,2,3,4)))
m4 = {}
for a in ACT:
    if a == 'Motor': continue
    fila = f"{a:<11}"
    for c in (1,2,3,4):
        gana = tot = 0
        for e in episodios:
            if cajas[e[0]] != c: continue
            ts = [t for t in e if t in trimes[a] and t in trimes['Motor']]
            if len(ts) != len(e): continue
            tot += 1
            if compuesto([trimes[a][t] for t in ts]) > compuesto([trimes['Motor'][t] for t in ts]): gana += 1
        m4[(a,c)] = (gana, tot)
        if tot == 0: v = '—'
        elif tot == 1: v = f"{gana}/1 ilustr."
        elif tot == 2: v = f"{gana}/2 insuf."
        else: v = f"{gana}/{tot} {'SI' if gana/tot > .5 else 'no'}"
        fila += f"{v:>16}"
    print(fila)
print(f"\nEpisodios por caja: " + str({c: sum(1 for e in episodios if cajas[e[0]]==c) for c in (1,2,3,4)}))

# ---------- CSV ----------
with open(OUT + 'ANEXO_M1_M4_POR_CAJA.csv','w',newline='',encoding='utf-8') as fh:
    w = csv.writer(fh); w.writerow(['activo','caja','nombre_caja','trimestres','M1_nominal_anual','M2_real_anual','inflacion_anual','M4_episodios_gana','M4_episodios_total'])
    for a in ACT:
        for c in (1,2,3,4):
            r = res.get((a,c))
            if r:
                g_, t_ = m4.get((a,c),(0,0))
                w.writerow([a,c,NOM[c],r['n'],f"{r['nom']:.5f}",f"{r['real']:.5f}",f"{r['infl']:.5f}",g_,t_])
print("CSV: ANEXO_M1_M4_POR_CAJA.csv")
