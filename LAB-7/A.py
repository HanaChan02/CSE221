import heapq
import math
N,M,S,D=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
adj=[[] for i in range(N+1)]
for i in range(M):
    adj[u[i]].append((v[i],w[i]))
dis=[math.inf]*(N+1)
par=[-1]*(N+1)
dis[S]=0
q=[(0,S)]
while q:
    d,node=heapq.heappop(q)
    if d!=dis[node]:
        continue
    for nei,wei in adj[node]:
        if dis[node]+wei<dis[nei]:
            dis[nei]=dis[node]+wei
            par[nei]=node
            heapq.heappush(q,(dis[nei],nei))
if dis[D]==math.inf:
    print(-1)
else:
    print(dis[D])
    road=[]
    curr=D
    while curr!=-1:
        road.append(curr)
        curr=par[curr]
    print(*reversed(road))