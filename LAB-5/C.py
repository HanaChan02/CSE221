#C
from collections import deque
N,M,S,D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
for x,y in zip(u,v):
  adj[x].append(y)
  adj[y].append(x)
for i in range(N+1):
  adj[i].sort()
q=deque([S])
d,parent=[-1]*(N + 1), [-1]*(N + 1)
d[S]=0
while q:
  node=q.popleft()
  for i in adj[node]:
    if d[i]==-1:
      d[i],parent[i]=d[node]+1, node
      q.append(i)
if d[D]==-1:
  print(-1)
else:
  print(d[D])
  road=[]
  while D!=-1:
    road.append(D)
    D=parent[D]
  print(*road[::-1])
