#B
N,M=map(int,input().split())
u=list(map(int,input().split()))
v=list(map(int,input().split()))
w=list(map(int,input().split()))
ans=[]
for i in range(N+1):
  ans.append([])
for j in range(M):
  ans[u[j]].append((v[j],w[j]))
for x in range(1,N+1):
  edge=ans[x]
  if edge:
    print(f"{x}:",end=" ")
    for d,w in edge:
      print(f"({d},{w})",end=" ")
    print()
  else:
    print(f"{x}:")
