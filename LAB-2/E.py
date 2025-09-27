#E
N,K=map(int, input().split())
arr=list(map(int, input().split()))
max_len=0
sum_list=[0]* (N+1)
for i in range(N):
  sum_list[i+1]=arr[i]+sum_list[i]
for i in range(N):
  l,r=i,N
  while l<r:
    mid=(l+r+1)//2
    if sum_list[mid]-sum_list[i]<=K:
      l=mid
    else:
      r=mid-1
  max_len=max(max_len, l-i)
print(max_len)
