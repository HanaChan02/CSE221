import math
import heapq
N,M,S,T=map(int,input().split())
adj=[[] for i in range(N+1)]
rev_adj=[[] for i in range(N+1)]
for i in range(M):
    u,v,w=map(int,input().split())
    adj[u].append((v,w))
    rev_adj[v].append((u,w))
def solve(s,g):
    dis=[math.inf]*(N+1)
    dis[s]=0
    q=[(0,s)]
    while q:
        d,node=heapq.heappop(q)
        if d!=dis[node]:
            continue
        for nei,wei in adj[node]:
            if d+wei<dis[nei]:
                dis[nei]=d+wei
                heapq.heappush(q,(dis[nei],nei))
    return dis
disA=solve(S,adj)
disB=solve(T,adj)
time=math.inf
destination=-1
for i in range(1,N+1):
    if disA[i]==math.inf or disB[i]==math.inf:
        continue
    curr=max(disA[i],disB[i])
    if curr<time or (curr==time and i<destination):
        time=curr
        destination=i
if destination==-1:
    print(-1)
else:
    print(time,destination)