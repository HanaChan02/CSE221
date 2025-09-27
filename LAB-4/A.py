#A
N,M=map(int,input().split())
ans=[]
for i in range(N):
  ans.append([0]*N)
for i in range(M):
  u,v,w=map(int,input().split())
  ans[u-1][v-1]=w
for row in ans:
  print(*row)
