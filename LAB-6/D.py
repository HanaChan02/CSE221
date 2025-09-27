from collections import deque
N=int(input())
adj=[[] for _ in range(N+1)]
for i in range(N-1):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
def diameter(s,e,adj):
    vis=[-1]*(N+1)
    q=deque()
    q.append(s)
    vis[s]=0
    far=s
    maxD=0
    while q:
        u=q.popleft()
        for v in adj[u]:
            if vis[v]==-1:
                vis[v]=vis[u]+1
                q.append(v)
                if vis[v]>maxD:
                    maxD=vis[v]
                    far=v
    return far,maxD
node,D=diameter(1,N,adj)
node1,D1=diameter(node,N,adj)
print(D1)
print(node, node1)