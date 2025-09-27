#D
N,M=map(int, input().split())
u=list(map(int, input().split()))
v=list(map(int, input().split()))

if M==0:
  print("YES" if N == 1 else "NO")
  exit()

deg = [0] * (N + 1)
for x, y in zip(u, v):
  if x == y:
    deg[x]+=2
  else:
    deg[x]+=1
    deg[y]+=1

odd=sum(1 for d in deg if d % 2 == 1)
if odd in (0, 2):
  print("YES")
else:
  print("NO")
