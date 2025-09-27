#H
N=int(input())
inO=list(map(int,input().split()))
postO=list(map(int,input().split()))
stk=[(inO,postO)]
ans=[]
while stk:
  in_O,post_O=stk.pop()
  if not post_O:
    continue
  root=post_O[-1]
  ans.append(root)
  root_idx=in_O.index(root)

  left_in=in_O[:root_idx]
  right_in=in_O[root_idx+1:]

  left_post=post_O[:len(left_in)]
  right_post=post_O[len(left_in):-1]

  stk.append((right_in,right_post))
  stk.append((left_in,left_post))

print(*ans[::])
