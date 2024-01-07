import sys 
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())

graph = [[] for _ in range(101)]

for _ in range(M):
    a, b  = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    global cnt
    q = deque([x])
    visited[x] = True
    while q:
        current = q.popleft()
        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1

cnt = 0
visited = [False for _ in range(101)]
bfs(1)
print(cnt)