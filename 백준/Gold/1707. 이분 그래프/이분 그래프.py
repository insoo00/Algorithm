import sys
from collections import deque

input = sys.stdin.readline

def bfs(i):
    q= deque()
    q.append(i)
    visited[i] = 0

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if visited[next] == -1:
                visited[next] = (visited[cur]+1)%2
                q.append(next)
            elif visited[next] == visited[cur]:  # 같은 색이라면 이분 그래프가 아님
                return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [-1 for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    answer = True
    for i in range(1, V+1):
        if visited[i] == -1:
            if not bfs(i):
                answer = False
                break

    if answer == True:
        print('YES')
    else:
        print('NO')
