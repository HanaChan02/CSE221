#A
from collections import deque
N,M=map(int,input().split())
adj=[]
for i in range(N+1):
  adj.append([])
for i in range(M):
  u,v=map(int,input().split())
  adj[u].append(v)
  adj[v].append(u)
visited=[0]*(N+1)
q=deque()
q.append(1)
visited[1]=1
ans=[]
while q:
  u=q.popleft()
  ans.append(str(u)) 
  for i in adj[u]:
    if visited[i]==0:
      visited[i]=1
      q.append(i)
print(" ".join(ans))
