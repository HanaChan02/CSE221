#D
N=int(input())
a1=list(map(int, input().split()))
M=int(input())
a2=list(map(int, input().split()))
result=[]
i=j=0
for x in range(N+M):
  if i<N and (j>=M or a1[i]<=a2[j]):
    result.append(str(a1[i]))
    i+=1
  else:
    result.append(str(a2[j]))
    j+=1
print(" ".join(result))
