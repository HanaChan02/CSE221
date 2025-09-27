#H
T=int(input())
for i in range(T):
  k,x=map(int,input().split())
  if x==1:
    print(k)
  else:
    print(k+(k-1)//(x-1))
