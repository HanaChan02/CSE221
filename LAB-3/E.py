#E
def expo(a,b,m):
  mult=1
  a%=m
  while b:
    if b%2==1:
      mult=(mult*a)%m
    a=(a**2)%m
    b//=2
  return mult

T=int(input())
for i in range(T):
  a,n,m=map(int,input().split())
  if a==1:
    print(n%m)
  else:
    mod=m*(a-1)
    aN=expo(a,n,mod)
    total=(a*((aN-1)%mod))//(a-1)
    print(total%m)
