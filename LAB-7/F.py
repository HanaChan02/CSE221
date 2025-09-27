import heapq
import math
N,M,S,D=map(int,input().split())
adj=[[] for i in range(N+1)]
for i in range(M):
    u,v,w=map(int,input().split())
    adj[u].append((v,w))
    adj[v].append((u,w))
dis1=[math.inf]*(N+1)
dis2=[math.inf]*(N+1)
q=[(0,S)]
dis1[S]=0
while q:
    d,node=heapq.heappop(q)
    if d>dis2[node]:
        continue
    for nei,wei in adj[node]:
        new=d+wei
        if new<dis1[nei]:
            dis2[nei] = dis1[nei]
            dis1[nei] = new
            heapq.heappush(q, (new, nei))
            heapq.heappush(q, (dis2[nei], nei))
        elif dis1[nei] < new < dis2[nei]:
            dis2[nei] = new
            heapq.heappush(q, (new, nei))
if dis2[D]==math.inf:
    print(-1)
else:
    print(dis2[D])