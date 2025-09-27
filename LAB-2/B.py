#B
N,M,K=map(int,input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
j=M-1
i=0
ai=i
aj=j
diff=abs(A[i]+B[j]-K)
while i<N and j>=0:
  total=A[i]+B[j]
  new_diff=abs(total-K)
  if new_diff<diff:
    diff=new_diff
    ai=i
    aj=j
  if total>K:
    j-=1
  else:
    i+=1
print(ai+1, aj+1)
