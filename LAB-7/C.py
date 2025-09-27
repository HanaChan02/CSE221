import math
import heapq
N,M=map(int,input().split())
adj=[[] for i in range(N+1)]
for i in range(M):
    u,v,w=map(int,input().split())
    adj[u].append((v,w))
    adj[v].append((u,w))
dis=[math.inf]*(N+1)
dis[1]=0
q=[(0,1)]
while q:
    curr,node=heapq.heappop(q)
    if curr!=dis[node]:
        continue
    for nei,wei in adj[node]:
        high=max(curr,wei)
        if high<dis[nei]:
            dis[nei]=high
            heapq.heappush(q,(high,nei))
out=[]
for i in range(1,N+1):
    if dis[i]==math.inf:
        out.append(-1)
    else:
        out.append(str(dis[i]))
print(*out)