import sys
from collections import deque

def solve():
    n,m=map(int,input().split())
    edges = []
    index = 2
    for i in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges_sorted = sorted(edges, key=lambda x: x[0])
    parent = list(range(n+1))
    rank = [0] * (n+1)
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1
        return True
    mst_edges = []
    mst_set = set()
    mst_total = 0
    count = 0
    for w, u, v in edges_sorted:
        if union(u, v):
            mst_edges.append((u, v, w))
            mst_set.add((u, v, w))
            mst_total += w
            count += 1
            if count == n-1:
                break
    if count != n-1:
        print(-1)
        return
    graph = [[] for _ in range(n+1)]
    for u, v, w in mst_edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    max_edge = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        visited = [False] * (n+1)
        queue = deque()
        queue.append(i)
        visited[i] = True
        while queue:
            current = queue.popleft()
            for neighbor, weight in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    max_edge[i][neighbor] = max(max_edge[i][current], weight)
                    queue.append(neighbor)
    second_best = float('inf')
    for w, u, v in edges:
        if (u, v, w) not in mst_set:
            candidate = mst_total + w - max_edge[u][v]
            if candidate > mst_total:
                second_best = min(second_best, candidate)
    if second_best == float('inf'):
        print(-1)
    else:
        print(second_best)
solve()