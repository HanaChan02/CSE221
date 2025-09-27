import heapq
import math
N,M=map(int,input().split())
adj=[[] for i in range(N+1)]
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
for i in range(M):
    adj[u[i]].append((v[i],w[i]))
disE=[math.inf]*(N+1)
disO=[math.inf]*(N+1)
q=[(0,1,-1)]
disE[1]=0
disO[1]=0
while q:
    d,node,last=heapq.heappop(q)
    if last==-1:
        if d!=0:
            continue
    else:
        if last==0 and d!=disE[node]:
            continue
        if last==1 and d!=disO[node]:
            continue
    for nei,wei in adj[node]:
        p=wei%2
        curr_cost=d+wei
        if last!=-1 and p==last:
            continue
        if p==0 and curr_cost<disE[nei]:
            disE[nei]=curr_cost
            heapq.heappush(q, (curr_cost, nei, 0))
        elif p==1 and curr_cost<disO[nei]:
            disO[nei]=curr_cost
            heapq.heappush(q, (curr_cost, nei, 1))
ans=min(disE[N],disO[N])
print(-1 if ans==math.inf else ans)