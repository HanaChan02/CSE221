N,K= map(int, input().split())
par=list(range(N+1))
size=[1]*(N+1)
def find(x):
    while par[x] != x:
        par[x]=par[par[x]]
        x=par[x]
    return x
for _ in range(K):
    a, b = map(int, input().split())
    ra, rb = find(a), find(b)
    if ra != rb:
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        par[rb] = ra
        size[ra] += size[rb]
    print(size[find(ra)])
