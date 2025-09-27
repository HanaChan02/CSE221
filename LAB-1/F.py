#F
def ancient_sort():
    N=int(input())
    array=list(map(int,input().split()))
    while True:
      swap=False
      for i in range(N-1):
        if array[i]>array[i+1] and array[i]%2==array[i+1]%2:
          array[i],array[i+1]=array[i+1],array[i]
          swap=True
      if not swap:
        break
    print(' '.join(map(str,array)))

ancient_sort()
