# C8 — ORO CON CIERRE DE TRIMESTRE (canonico) vs MEDIA (sensibilidad)
# Cuatro cajas · ambos clasificadores · M1 M2 M3 M4 · episodios
import io, sys, csv, json, re, zipfile
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
S = "C:/Users/fgonz/AppData/Local/Temp/claude/C--Users-fgonz-Desktop-claude-tradingview/6e19bdff-01a2-4f07-b218-a69f858695bb/scratchpad/"
OUT = "C:/Users/fgonz/Desktop/claude-apps/claude-cartera-antonio/05_TRABAJO_FINAL/"

def q(f):
    a, m, _ = f.split('-'); return (int(a), (int(m)-1)//3+1)
def qm(ym): return (int(ym[:4]), (int(ym[4:])-1)//3+1)
def comp(rs):
    x = 1.0
    for r in rs: x *= (1+r)
    return x
def et(t): return "%dQ%d" % t

# --- clasificaciones: principal (mediana) y alternativa (media) ---
CP, CA = {}, {}
for r in csv.DictReader(open(OUT+'ANEXO_CLASIFICACION_CAJAS.csv', encoding='utf-8')):
    a,t = r['trimestre'].split('Q'); k=(int(a),int(t))
    CP[k] = int(r['caja_principal']); CA[k] = int(r['caja_alternativa_media40'])
trims = sorted(CP)

# --- inflacion ---
cpi_m = {}
for r in csv.DictReader(open(S+'cpi.csv', encoding='utf-8')):
    k=list(r.keys()); v=r[k[1]]
    if v not in ('.',''): cpi_m[r[k[0]]]=float(v)
bb={}
for k,v in cpi_m.items(): bb.setdefault(q(k),[]).append(v)
cpi={k:sum(v)/len(v) for k,v in bb.items() if len(v)==3}
qs=sorted(cpi); infl={qs[i]: cpi[qs[i]]/cpi[qs[i-1]]-1 for i in range(1,len(qs))}

# --- Motor ---
txt=zipfile.ZipFile(S+'F-F_Research_Data_Factors_CSV.zip').read('F-F_Research_Data_Factors.csv').decode('latin-1').splitlines()
h=[i for i,l in enumerate(txt) if re.match(r'^\s*,',l)]
mot={}
for l in txt[h[0]+1:h[1]]:
    if re.match(r'^\s*\d{6}\s*,',l):
        p=l.split(','); ym=p[0].strip(); r=(float(p[1])+float(p[4]))/100
        if abs(r)<1.5: mot.setdefault(qm(ym),[]).append(r)
motq={k:comp(v)-1 for k,v in mot.items() if len(v)==3}

# --- oro: dos series ---
g=json.load(open(S+'gold_lbma.json'))
por_mes={}
for x in g:
    if x['v'] and x['v'][0]: por_mes.setdefault(x['d'][:7],[]).append((x['d'], float(x['v'][0])))

def serie_oro(modo):
    nivel={}
    porq={}
    for mes, obs in por_mes.items():
        porq.setdefault(q(mes+'-01'), []).extend(obs)
    for k, obs in porq.items():
        obs=sorted(obs)
        meses=set(d[:7] for d,_ in obs)
        if len(meses)!=3: continue
        if modo=='cierre':
            nivel[k]=obs[-1][1]                       # ultima observacion del trimestre
        else:
            mm={}
            for d,p in obs: mm.setdefault(d[:7],[]).append(p)
            medias=[sum(v)/len(v) for v in mm.values()]
            nivel[k]=sum(medias)/len(medias)          # media de medias mensuales
    ks=sorted(nivel)
    return {ks[i]: nivel[ks[i]]/nivel[ks[i-1]]-1 for i in range(1,len(ks)) if ks[i]>=(1971,4)}

ORO={'cierre': serie_oro('cierre'), 'media': serie_oro('media')}

def episodios(cl):
    eps, run = [], [trims[0]]
    for t in trims[1:]:
        if cl[t]==cl[run[-1]]: run.append(t)
        else: eps.append(run); run=[t]
    eps.append(run)
    return [e for e in eps if len(e)>=2]

def analiza(cl, oro):
    out={}
    eps=episodios(cl)
    for c in (1,2,3,4):
        ts=[t for t in trims if cl[t]==c and t in oro and t in motq and t in infl]
        n=len(ts)
        ro=comp([oro[t] for t in ts])**(4/n)-1
        rm=comp([motq[t] for t in ts])**(4/n)-1
        inf=comp([infl[t] for t in ts])**(4/n)-1
        real_o=(1+ro)/(1+inf)-1; real_m=(1+rm)/(1+inf)-1
        gana=tot=0; det=[]
        for e in eps:
            if cl[e[0]]!=c: continue
            tt=[t for t in e if t in oro and t in motq]
            if len(tt)!=len(e): continue
            tot+=1
            win = comp([oro[t] for t in tt])>comp([motq[t] for t in tt])
            gana+=win
            det.append((et(e[0])+'-'+et(e[-1]), win))
        out[c]={'n':n,'nom':ro,'real':real_o,'m3':real_o-real_m,'gana':gana,'tot':tot,'det':det}
    return out

R={}
for nombre, cl in [('PRINCIPAL (mediana 40T)', CP), ('ALTERNATIVA (media 10a)', CA)]:
    for modo in ('cierre','media'):
        R[(nombre,modo)] = analiza(cl, ORO[modo])

for nombre in ('PRINCIPAL (mediana 40T)','ALTERNATIVA (media 10a)'):
    print("="*86)
    print("CLASIFICADOR " + nombre)
    print("%-8s %-9s %5s %10s %10s %10s %9s" % ('caja','precio','n','M1 nom','M2 real','M3 pp','M4'))
    for c in (1,2,3,4):
        for modo in ('cierre','media'):
            d=R[(nombre,modo)][c]
            marca = ' <= CANONICO' if modo=='cierre' else ''
            print("%-8s %-9s %5d %9.2f%% %9.2f%% %+9.2f %5d/%-3d%s" % (
                c, modo, d['n'], d['nom']*100, d['real']*100, d['m3']*100, d['gana'], d['tot'], marca))

print("\n" + "="*86)
print("EPISODIOS DE CAJA 4 — detalle (clasificador principal)")
for modo in ('cierre','media'):
    d=R[('PRINCIPAL (mediana 40T)',modo)][4]
    print(" %s: %d/%d" % (modo, d['gana'], d['tot']))
    for nom, win in d['det']:
        print("    %-16s %s" % (nom, 'GANA' if win else 'pierde'))

print("\nCOMPROBACIONES DE SIGNO (M3) — cierre vs media")
for nombre in ('PRINCIPAL (mediana 40T)','ALTERNATIVA (media 10a)'):
    for c in (1,2,3,4):
        a=R[(nombre,'cierre')][c]['m3']; b=R[(nombre,'media')][c]['m3']
        cambia = (a>0)!=(b>0)
        print("  %-24s caja %d: cierre %+7.2f  media %+7.2f  cambia signo: %s" % (nombre,c,a*100,b*100,cambia))

# CSV canonico
with open(OUT+'ANEXO_ORO_C8_CIERRE.csv','w',newline='',encoding='utf-8') as fh:
    w=csv.writer(fh)
    w.writerow(['clasificador','metodo_precio','caja','trimestres','M1_nominal','M2_real','M3_pp_vs_motor','M4_gana','M4_total'])
    for (nombre,modo),v in R.items():
        for c in (1,2,3,4):
            d=v[c]
            w.writerow([nombre,modo,c,d['n'],"%.5f"%d['nom'],"%.5f"%d['real'],"%.3f"%(d['m3']*100),d['gana'],d['tot']])
print("\nCSV: ANEXO_ORO_C8_CIERRE.csv")
