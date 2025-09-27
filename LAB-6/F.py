from collections import deque
N,M,S,Q=map(int,input().split())
adj=[[] for i in range(N+1)]
for i in range(M):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
s=list(map(int,input().split()))
d=list(map(int,input().split()))
dist=[-1]*(N+1)
q=deque()
for i in s:
    dist[i]=0
    q.append(i)
while q:
    u=q.popleft()
    for v in adj[u]:
        if dist[v]==-1:
            dist[v]=dist[u]+1
            q.append(v)
ans=[]
for i in d:
    ans.append(str(dist[i]))
print(*ans)