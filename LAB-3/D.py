#D
m=10**9+7
def mat_mult(a,b):
  ans=[[0,0],[0,0]]
  ans[0][0]=(a[0][0]*b[0][0]+a[0][1]*b[1][0])%m
  ans[0][1]=(a[0][0]*b[0][1]+a[0][1]*b[1][1])%m
  ans[1][0]=(a[1][0]*b[0][0]+a[1][1]*b[1][0])%m
  ans[1][1]=(a[1][0]*b[0][1]+a[1][1]*b[1][1])%m
  return ans

def mat_power(mat,p):
  if p==0:
    return [[1,0],[0,1]]
  elif p==1:
    return mat
  elif p%2==0:
    new_mat=mat_power(mat,p//2)
    return mat_mult(new_mat,new_mat)
  else:
    new_mat=mat_power(mat,(p-1)//2)
    return mat_mult(mat,mat_mult(new_mat,new_mat))

T=int(input())
for i in range(T):
  a11,a12,a21,a22=map(int,input().split())
  X=int(input())
  mat=[[a11,a12],[a21,a22]]
  result=mat_power(mat,X)
  print(f"{result[0][0]} {result[0][1]}")
  print(f"{result[1][0]} {result[1][1]}")
