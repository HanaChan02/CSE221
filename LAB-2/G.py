#G
N,Q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for i in range(Q):
  x, y = map(int, input().split())
  l=0
  r=N
  while l<r:
    mid=(l+r)//2
    if a[mid]<x:
      l=mid+1
    else:
      r=mid
  lower=l
  l=0
  r=N
  while l<r:
    mid = (l+r)//2
    if a[mid]<=y:
      l=mid + 1
    else:
      r=mid
  upper=l
  print(upper-lower)
