#A
NS=list(map(int,input().split()))
arr=list(map(int,input().split()))
a=""
x=NS[0]-1
y=0
while x>y:
  total=arr[y]+arr[x]
  if total==NS[1]:
    a += f"{y+1} {x+1}"
    print(a.strip())
    break
  elif total < NS[1]:
    y+=1
  else:
    x-=1
if a == "":
  print("-1")
