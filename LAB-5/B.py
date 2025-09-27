#B
from collections import deque
import sys
sys.setrecursionlimit(2*100000+5)
N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
adj = [[] for _ in range(N + 1)]
for x,y in zip(u,v):
  adj[x].append(y)
  adj[y].append(x)
visited=[0]*(N + 1)
ans=[]
stack=[1]
while stack:
  node = stack.pop()
  if visited[node]:
      continue
  visited[node] = 1
  ans.append(str(node))
  for nei in reversed(adj[node]):
    if not visited[nei]:
      stack.append(nei)
print(" ".join(ans))
