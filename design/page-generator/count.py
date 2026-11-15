import re,glob,itertools,sys
D={}
for f in sorted(glob.glob('/home/user/seamens-enterprises-website/products/*/*.html')):
    t=open(f).read()
    m=t[t.index('<main>'):t.index('</main>')]
    m=re.sub(r'<script.*?</script>','',m,flags=re.S)
    D[f.split('products/')[1]]=re.sub(r'<[^>]+>',' ',m).lower().split()
W=sorted((len(v),k) for k,v in D.items())
print('min/avg',W[0][0],sum(w for w,_ in W)//len(W),'under1000',sum(w<1000 for w,_ in W))
print(' '.join(f'{k.split("/")[1][:-5]}:{w}' for w,k in W if w<1000))
G={k:set(zip(*[v[i:] for i in range(5)])) for k,v in D.items()}
print('maxJ',max((len(G[a]&G[b])/len(G[a]|G[b]),a,b) for a,b in itertools.combinations(G,2)))
