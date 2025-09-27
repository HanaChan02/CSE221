#G
N=int(input())
Si=list(map(int,input().split()))
Sm=list(map(int,input().split()))
student=[]
for i in range(N):
  student.append([i,Si[i],Sm[i]])
for i in range(N-1):
  for j in range(i+1,N):
    if student[i][2]<student[j][2] or (student[i][2]==student[j][2] and student[i][1]>student[j][1]):
      student[i], student[j]=student[j], student[i]
pos=[0] * N
visited=[False] * N
swap=0
for i in range(N):
  og=student[i][0]
  pos[og]=i
for i in range(N):
  if not visited[i] and pos[i]!=i:
    size=0
    j=i
    while not visited[j]:
      size+=1
      visited[j]=True
      j=pos[j]
    if size>0:
      swap+=(size-1)
print(f"Minimum swaps: {swap}")
for x in student:
  print(f"ID: {x[1]} Mark: {x[2]}")
