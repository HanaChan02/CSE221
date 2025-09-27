#E
def canORnot_sort():
    N = int(input())
    array = list(map(int, input().split()))
    even = array[::2]
    odd = array[1::2]
    even.sort()
    odd.sort()
    new_array = []
    even_index = 0
    odd_index = 0
    for i in range(N):
      if i % 2 == 0:
        new_array.append(even[even_index])
        even_index += 1
      else:
        new_array.append(odd[odd_index])
        odd_index += 1
    for i in range(N - 1):
      if new_array[i] > new_array[i + 1]:
        print("NO")
        return
    print("YES")

canORnot_sort()
