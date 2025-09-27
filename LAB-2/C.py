#C
def triplet_idx(N, X, a):
  elem=[]
  for i in range(N):
    elem.append((a[i], i+1))
  elem.sort()
  for i in range(N-2):
    x=i+1
    y=N-1
    sum_left=X-elem[i][0]
    while x<y:
      total=elem[x][0]+elem[y][0]
      if total<sum_left:
        x+=1
      elif total==sum_left:
        return (elem[i][1], elem[x][1], elem[y][1])
      else:
        y-=1
  return -1

N,X=map(int,input().split())
a=list(map(int,input().split()))
ans=triplet_idx(N, X, a)
if ans!=-1:
  print(' '.join(map(str, ans)))
else:
  print(-1)
