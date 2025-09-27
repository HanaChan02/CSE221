#C
N=int(input())
matrix=[]
for i in range(N):
  matrix.append([0]*N)
  row=list(map(int,input().split()))
  j=row[0]
  for k in range(1,j+1):
    node=row[k]
    matrix[i][node]=1
for row in matrix:
  print(*row)
