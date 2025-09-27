#E
N,M=map(int, input().split())
indeg=[0]*(N+1)
outdeg=[0]*(N+1)
u=list(map(int, input().split()))
v=list(map(int, input().split()))

for i in range(M):
  indeg[v[i]]+=1
  outdeg[u[i]]+=1

ans=[]
for i in range(1,N+1):
  ans.append(str(indeg[i]-outdeg[i]))
print(" ".join(ans))
