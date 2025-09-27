from collections import deque
N,M=map(int,input().split())
adj=[[] for i in range(N+1)]
for i in range(M):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
vis=[-1]*(N+1)
maxG=0
for i in range(1,N+1):
    if vis[i]==-1:
        q=deque()
        q.append(i)
        vis[i]=0
        count=[0,0]
        count[0]+=1
        is_bipar=True
        while q and is_bipar:
            u=q.popleft()
            for v in adj[u]:
                if vis[v]==-1:
                    vis[v]=vis[u]^1
                    count[vis[v]]+=1
                    q.append(v)
                elif vis[v]==vis[u]:
                    is_bipar=False
                    break
        if not is_bipar:
            print(N)
            exit(0)
        else:
            maxG+=max(count)
print(maxG)                
