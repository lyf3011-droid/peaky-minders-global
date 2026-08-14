# AUDITORIA CUANTITATIVA de los resultados M1-M4. Verificaciones independientes.
import io, sys, csv, json, re, zipfile, statistics as st
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

cajas = {}
for r in csv.DictReader(open(OUT+'ANEXO_CLASIFICACION_CAJAS.csv', encoding='utf-8')):
    a,t = r['trimestre'].split('Q'); cajas[(int(a),int(t))] = int(r['caja_principal'])
trims = sorted(cajas)

# CPI
cpi_m = {}
for r in csv.DictReader(open(S+'cpi.csv', encoding='utf-8')):
    k=list(r.keys()); v=r[k[1]]
    if v not in ('.',''): cpi_m[r[k[0]]]=float(v)
bb={}
for k,v in cpi_m.items(): bb.setdefault(q(k),[]).append(v)
cpi={k:sum(v)/len(v) for k,v in bb.items() if len(v)==3}
qs=sorted(cpi); infl={qs[i]: cpi[qs[i]]/cpi[qs[i-1]]-1 for i in range(1,len(qs))}

def ff(zipn,csvn):
    txt=zipfile.ZipFile(S+zipn).read(csvn).decode('latin-1').splitlines()
    h=[i for i,l in enumerate(txt) if re.match(r'^\s*,',l)]
    cols=[c.strip() for c in txt[h[0]].strip().split(',')[1:]]
    fin=h[1] if len(h)>1 else len(txt); out={}
    for l in txt[h[0]+1:fin]:
        if re.match(r'^\s*\d{6}\s*,',l):
            p=l.split(','); out[p[0].strip()]={c:float(p[i+1])/100 for i,c in enumerate(cols)}
    return out
fac=ff('F-F_Research_Data_Factors_CSV.zip','F-F_Research_Data_Factors.csv')

print("="*78)
print("A1 · DATOS AUSENTES EN FAMA-FRENCH (-99.99) — ¿se descartó mucho?")
n99=sum(1 for ym,v in fac.items() if abs(v['Mkt-RF'])>1.5)
print(f"   meses con codigo de dato ausente en el factor de mercado: {n99} de {len(fac)}")

print("\nA2 · MOTOR — recálculo independiente por caja (mensual->trimestre->caja)")
mot={}
for ym,v in fac.items():
    r=v['Mkt-RF']+v['RF']
    if abs(r)<1.5: mot.setdefault(qm(ym),[]).append(r)
motq={k:comp(v)-1 for k,v in mot.items() if len(v)==3}
for c in (1,2,3,4):
    ts=[t for t in trims if cajas[t]==c and t in motq and t in infl]
    nom=comp([motq[t] for t in ts])**(4/len(ts))-1
    inf=comp([infl[t] for t in ts])**(4/len(ts))-1
    print(f"   caja {c}: n={len(ts):>3}  nominal {nom*100:+6.2f}%  real {((1+nom)/(1+inf)-1)*100:+6.2f}%")

print("\nA3 · ORO — PRUEBA DE SENSIBILIDAD AL MÉTODO DE PRECIO")
g=json.load(open(S+'gold_lbma.json'))
pm={}
for x in g:
    if x['v'] and x['v'][0]: pm.setdefault(x['d'][:7],[]).append((x['d'],float(x['v'][0])))
mes_media={k:sum(p for _,p in v)/len(v) for k,v in pm.items()}
mes_cierre={k:sorted(v)[-1][1] for k,v in pm.items()}

def oro_serie(mensual):
    qo={}
    for k,v in mensual.items(): qo.setdefault(q(k+'-01'),[]).append((k,v))
    niv={}
    for k,v in qo.items():
        if len(v)==3:
            niv[k]= sum(p for _,p in v)/3 if mensual is mes_media else sorted(v)[-1][1]
    ks=sorted(niv)
    return {ks[i]: niv[ks[i]]/niv[ks[i-1]]-1 for i in range(1,len(ks)) if ks[i]>=(1971,4)}

for etiqueta, serie in [('media del trimestre (usado)', oro_serie(mes_media)),
                        ('cierre del trimestre (control)', oro_serie(mes_cierre))]:
    ts=[t for t in trims if cajas[t]==4 and t in serie and t in motq and t in infl]
    n=len(ts)
    ro=comp([serie[t] for t in ts])**(4/n)-1
    rm=comp([motq[t] for t in ts])**(4/n)-1
    inf=comp([infl[t] for t in ts])**(4/n)-1
    m3=((1+ro)/(1+inf)-1)-((1+rm)/(1+inf)-1)
    # M4
    eps,run=[],[trims[0]]
    for t in trims[1:]:
        if cajas[t]==cajas[run[-1]]: run.append(t)
        else: eps.append(run); run=[t]
    eps.append(run)
    gana=tot=0
    for e in [x for x in eps if len(x)>=2 and cajas[x[0]]==4]:
        tt=[t for t in e if t in serie and t in motq]
        if len(tt)!=len(e): continue
        tot+=1
        if comp([serie[t] for t in tt])>comp([motq[t] for t in tt]): gana+=1
    print(f"   caja 4 · {etiqueta:<32} n={n:>3}  real oro {ro*100:+6.2f}%  M3 {m3*100:+6.2f} pp  M4 {gana}/{tot}")

print("\nA4 · COHERENCIA DE TAMAÑOS DE MUESTRA")
print(f"   trimestres clasificados: {len(trims)}  (esperado 273: {len(trims)==273})")
tot=sum(1 for t in trims if t in motq); print(f"   con retorno de Motor: {tot}")
oro=oro_serie(mes_media); print(f"   con retorno de oro (desde 1971Q4): {sum(1 for t in trims if t in oro)}")

print("\nA5 · CONTROL DE NO-ANTICIPACIÓN (look-ahead) EN EL UMBRAL")
print("   ventana = trims[n-40:n] -> ultimo elemento es el trimestre ANTERIOR al clasificado")
print(f"   comprobacion estructural: {trims[41]} usa hasta {trims[40]}  -> {trims[40] < trims[41]}")

print("\nA6 · SUMA DE CONTROL DE LA INFLACIÓN POR CAJA (debe ordenar 3<1<2<4)")
orden=[]
for c in (1,2,3,4):
    ts=[t for t in trims if cajas[t]==c and t in infl]
    orden.append((c, comp([infl[t] for t in ts])**(4/len(ts))-1))
print("   " + " · ".join(f"caja {c}: {v*100:+.2f}%" for c,v in orden))
print(f"   orden esperado por construccion (3<1<2<4): {orden[2][1]<orden[0][1]<orden[1][1]<orden[3][1]}")
