from collections import deque
def solve():
    N=int(input())
    words=[input().strip() for _ in range(N)]
    adj={}
    indeg={}
    all=set()
    for i in words:
        for j in i:
            all.add(j)
            if j not in adj:
                adj[j]=set()
            if j not in indeg:
                indeg[j]=0
    for i in range(N-1):
        word1=words[i]
        word2=words[i+1]
        found=False
        for c1,c2 in zip(word1,word2):
            if c1 != c2:
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    indeg[c2] += 1
                found = True
                break
        if not found and len(word1)>len(word2):
            print(-1)
            return 
    heap = []
    for c in all:
        if indeg[c] == 0:
            heap.append(c)
    heap.sort()
    
    result = []
    while heap:
        c = heap.pop(0)
        result.append(c)
        for neighbor in adj[c]:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                heap.append(neighbor)
        heap.sort()
    
    if len(result) != len(all):
        print(-1)
    else:
        print(''.join(result))
solve()