from collections import deque
def knight():
    N=int(input())
    x1,y1,x2,y2=map(int, input().split())
    moves=[(-1,-2),(-1,+2),(-2,-1),(-2,+1),(+1,-2),(+1,+2),(+2,-1),(+2,+1)]
    vs=[bytearray(N+1) for _ in range(N+1)]
    q=deque()
    q.append((x1,y1,0))
    vs[x1][y1]=1
    while q:
        x,y,steps=q.popleft()
        if x==x2 and y==y2:
            print(steps)
            return
        for sx,sy in moves:
            n1,n2=x+sx,y+sy
            if 1<=n1<=N and 1<=n2<=N and vs[n1][n2]==0:
                vs[n1][n2]=1
                q.append((n1,n2,steps+1))
    print(-1)
knight()