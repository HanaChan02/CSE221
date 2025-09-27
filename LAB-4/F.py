#F
N=int(input())
x,y=map(int, input().split())
moves=[(x-1,y-1),(x,y-1),(x-1,y),(x+1,y+1),(x+1,y),(x,y+1),(x+1,y-1),(x-1,y+1)]
valid=[]
for a,b in moves:
  if 1<=a<=N and 1<=b<=N:
    valid.append((a,b))
valid.sort()
print(len(valid))
for c,d in valid:
  print(c, d)
