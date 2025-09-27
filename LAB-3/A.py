#A
def merge(a, b):
  merged_arr=[]
  count=0
  i=j=0
  while i<len(a) and j<len(b):
    if a[i]<=b[j]:
      merged_arr.append(a[i])
      i+=1
    else:
      merged_arr.append(b[j])
      j+=1
      count+=len(a)-i
  merged_arr.extend(a[i:])
  merged_arr.extend(b[j:])
  return merged_arr,count

def mergeSort(arr):
  if len(arr) <= 1:
    return arr, 0
  else:
    mid = len(arr)//2
    a1,count_l=mergeSort(arr[:mid])
    a2,count_r=mergeSort(arr[mid:])
    merged_arr, count_m = merge(a1, a2)
    total=count_l+count_r+count_m
    return merged_arr, total

N=int(input())
a=list(map(int,input().split()))
sorted_arr, inversions=mergeSort(a)
print(inversions)
print(" ".join(map(str, sorted_arr)))
