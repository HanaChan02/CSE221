#E
import sys
from collections import deque

def solve():
  n, r = map(int, input().split())
  g = [[] for _ in range(n+1)]
  for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

  par = [0]*(n+1)
  sz = [0]*(n+1)

  st = [(r, 0, False)]
  while st:
    u, p, done = st.pop()
    if not done:
      par[u] = p
      st.append((u, p, True))
      for v in g[u]:
        if v != p:
          st.append((v, u, False))
    else:
      sz[u] = 1
      for v in g[u]:
        if v != p:
          sz[u] += sz[v]

  q = int(input())
  ans = []
  for _ in range(q):
    x = int(input())
    ans.append(str(sz[x]))

  print('\n'.join(ans))
solve()
