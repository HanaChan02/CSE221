#G
def knights():
  N,M,K=map(int, input().split())
  knight=set()
  for i in range(K):
    x,y=map(int, input().split())
    knight.add((x,y))
  for (x,y) in knight:
    moves=[(x-1,y-2),(x-1,y+2),(x-2,y-1),(x-2,y+1),(x+1,y-2),(x+1,y+2),(x+2,y-1),(x+2,y+1)]
    for a,b in moves:
      if (a, b) in knight:
        print("YES")
        return
  print("NO")
knights()
