#D
T=int(input())
for x in range(T):
  N=int(input())
  array = list(map(int, input().split()))
  sorted=True
  for i in range(N - 1):
    if array[i] > array[i+1]:
      sorted=False
      break
  if sorted:
    print("YES")
  else:
    print("NO")
