from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = deque()
q.append([0,0])

while (q):
    x, y = q.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        if graph[nx][ny] == 1:
            q.append([nx, ny])
            graph[nx][ny] = graph[x][y] + 1

print(graph[n-1][m-1])


