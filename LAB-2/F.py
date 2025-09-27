#F
N,K=map(int, input().split())
arr=list(map(int, input().split()))
max_len=0
l=0
freq={}
for i in range(N):
  if arr[i] in freq:
    freq[arr[i]] += 1
  else:
    freq[arr[i]] = 1
  while len(freq)>K:
    freq[arr[l]]-=1
    if freq[arr[l]]==0:
      del freq[arr[l]]
    l+=1
  c_len=i-l+1
  if c_len>max_len:
    max_len=c_len

print(max_len)
