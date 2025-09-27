from collections import deque
N,M=map(int,input().split())
adj=[[] for i in range(N+1)]
for i in range(M):
    u,v=map(int,input().split())
    adj[u].append(v)
vis=[0]*(N+1)
topo=[]
cycle=[False]
def dfs(u):
    vis[u]=1
    if cycle[0]:
        return
    for v in adj[u]:
        if not vis[v]:
            dfs(v)
            if cycle[0]:
                return
        elif vis[v]==1:
            cycle[0]=True
            return
    vis[u]=2
    topo.append(u)
for i in range(1,N+1):
    if not vis[i]:
        dfs(i)
        if cycle[0]:
            print(-1)
            exit()
topo.reverse()
print(" ".join(map(str, topo)))