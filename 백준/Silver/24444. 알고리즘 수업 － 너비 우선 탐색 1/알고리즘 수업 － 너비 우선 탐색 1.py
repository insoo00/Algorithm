import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
answer = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

count = 1
q = deque()
q.append(R)
visited[R] = True
answer[R] = count
count += 1

while q:
    cur = q.popleft()

    for next in graph[cur]:
        if not visited[next]:
            q.append(next)
            visited[next] = True
            answer[next] = count
            count += 1

for i in range(1, N+1):
    print(answer[i])
