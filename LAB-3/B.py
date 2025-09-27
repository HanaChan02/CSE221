#B
def merge_sort(arr):
  if len(arr)<=1:
    return arr
  mid=len(arr) // 2
  l=merge_sort(arr[:mid])
  r=merge_sort(arr[mid:])
  return merge_arr(l,r)

def merge_arr(a, b):
  ans = []
  i=j=0
  while i<len(a) and j<len(b):
    if a[i]<=b[j]:
      ans.append(a[i])
      i += 1
    else:
      ans.append(b[j])
      j += 1
  ans.extend(a[i:])
  ans.extend(b[j:])
  return ans

def CountPairs(arr):
  if len(arr) <= 1:
    return arr, 0
  else:
    mid = len(arr)//2
    a1,count_l=CountPairs(arr[:mid])
    a2,count_r=CountPairs(arr[mid:])
    merged_arr, count_m = merge(a1, a2)
    total=count_l+count_r+count_m
    return merged_arr, total

def merge(a,b):
  merged_arr=[]
  count=0
  rightx2=[]
  for j in b:
    rightx2.append(j*j)
  rightx2 = merge_sort(rightx2)
  x=0
  for i in a:
    while x<len(rightx2) and rightx2[x]<i:
      x+=1
    count+=x
  i=j=0
  while i<len(a) and j<len(b):
    if a[i]<=b[j]:
      merged_arr.append(a[i])
      i+=1
    else:
      merged_arr.append(b[j])
      j+=1
  merged_arr.extend(a[i:])
  merged_arr.extend(b[j:])
  return merged_arr,count

N=int(input())
a=list(map(int,input().split()))
arr,pairs=CountPairs(a)
print(pairs)
