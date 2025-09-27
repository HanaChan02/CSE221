#D
from collections import deque
def solve():
  N, M, S, D, K = map(int, input().split())
  adj = [[] for _ in range(N + 1)]
  for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)

  def bfs(start, end):
    dist = [-1] * (N + 1)
    parent = [-1] * (N + 1)
    q = deque([start])
    dist[start] = 0
    while q:
      curr = q.popleft()
      for nxt in adj[curr]:
        if dist[nxt] == -1:
          dist[nxt] = dist[curr] + 1
          parent[nxt] = curr
          q.append(nxt)
          if nxt == end:
            return dist, parent
    return dist, parent

  dist_S, parent_S = bfs(S, K)
  if dist_S[K] == -1: return print(-1)
  dist_K, parent_K = bfs(K, D)
  if dist_K[D] == -1: return print(-1)
  print(dist_S[K] + dist_K[D])
  path = []
  node = K
  while node != -1: path.append(node); node = parent_S[node]
  path.reverse()
  node = D
  while node!= K: path.append(node); node = parent_K[node]
  print(*path)
solve()
