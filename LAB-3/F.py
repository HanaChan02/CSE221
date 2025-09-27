#F
N=int(input())
Arr=list(map(int,input().split()))
stk=[(0,N-1)]
ans=[]
while stk:
  l,r=stk.pop()
  if l<=r:
    mid=(l+r)//2
    ans.append(Arr[mid])
    stk.append((mid+1,r))
    stk.append((l,mid-1))
print(" ".join(map(str,ans)))
