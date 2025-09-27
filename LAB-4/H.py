#H
import math
N,Q=map(int, input().split())
adj=[0]*(N+1)
for i in range(N+1):
  adj[i]=[]
for i in range(1,N+1):
  for j in range(1,N+1):
    if i!=j and math.gcd(i,j)==1:
      adj[i].append(j)
for x in range(1,N+1):
  adj[x].sort()
for a in range(Q):
  X,K=map(int, input().split())
  neigh=adj[X]
  if K<=len(neigh):
    print(neigh[K-1])
  else:
    print(-1)
