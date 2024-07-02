from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    road[node] = 0
    while q:
        node = q.popleft()
        dn = [node-1, node+1, node+A, node-A, node+B, node-B, node*A, node*B]
        for n in dn:
            if 0<=n<=100000:
                if road[n] == -1:
                    q.append(n)
                    road[n] = road[node]+1
                    if n == M:
                        return

A, B, N, M = map(int, input().split())
road = [-1]*100001
bfs(N)
print(road[M])