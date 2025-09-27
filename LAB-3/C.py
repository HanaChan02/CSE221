#C
a,b=map(int, input().split())
m=107
ans=1
a=a%m
while b>0:
  if b%2!=0:
    ans=(ans*a)%m
  a=(a**2)%m
  b=b//2
print(ans)
