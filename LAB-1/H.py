#H
N=int(input())
train=[]
for i in range(N):
  T=list(map(str,input().split()))
  t_name=T[0]
  time=T[len(T)-1]
  H = int(time[:2])
  M = int(time[3:])
  t_minutes = H * 60 + M
  full_line = " ".join(T)
  train.append([t_name, t_minutes, i, full_line])
for i in range(N-1):
  for j in range(i+1,N):
    if train[i][0]>train[j][0]:
      train[i],train[j] = train[j], train[i]
    elif train[i][0]==train[j][0]:
      if train[i][1]<train[j][1]:
        train[i],train[j] = train[j], train[i]
      elif train[i][1]==train[j][1]:
        if train[i][2]>train[j][2]:
          train[i],train[j] = train[j], train[i]
for i in range(N):
  print(train[i][3])
