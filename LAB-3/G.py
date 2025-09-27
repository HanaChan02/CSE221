#G
N=int(input())
inO=list(map(int,input().split()))
preO=list(map(int,input().split()))
stk=[(inO,preO)]
ans=[]
while stk:
  in_O,pre_O=stk.pop()
  if not pre_O:
    continue
  root=pre_O[0]
  ans.append(root)
  root_idx=in_O.index(root)

  left_in=in_O[:root_idx]
  right_in=in_O[root_idx+1:]

  left_pre=pre_O[1:1+len(left_in)]
  right_pre=pre_O[len(left_in)+1:]


  stk.append((left_in,left_pre))
  stk.append((right_in,right_pre))

print(*ans[::-1])
