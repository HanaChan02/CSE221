N,M=map(int, input().split())
edges=[tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
par=list(range(N+1))
size=[1]*(N+1)
def find(x):
    while par[x]!=x:
        par[x]=par[par[x]]
        x = par[x]
    return x
cost, used = 0, 0
for u,v,w in edges:
    au,av=find(u),find(v)
    if au!=av:
        if size[au]<size[av]:
            au,av=av,au
        par[av]=au
        size[au]+=size[av]
        cost += w
        used += 1
        if used == N-1: break
print(cost)