from collections import deque

n, m, t = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
sword = []
for i in range(n):
    for j in range(m):
        if table[i][j] == 2:
            sword = [i, j]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

q = deque()
q.append((0, 0))
while q:
    curX, curY = q.popleft()

    for i in range(4):
        nextX = curX + dx[i]
        nextY = curY + dy[i]

        if nextX < 0 or nextX >= n or nextY < 0 or nextY >= m:
            continue
        if visited[nextX][nextY] == 0:
            if table[nextX][nextY] != 1:
                visited[nextX][nextY] = visited[curX][curY] + 1
                q.append((nextX, nextY))

if visited[sword[0]][sword[1]] != 0:
    if visited[n-1][m-1] == 0:
        visited[n-1][m-1] = visited[sword[0]][sword[1]] + (n-sword[0]-1) + (m-sword[1]-1)
    else:
        visited[n-1][m-1] = min(visited[n-1][m-1], visited[sword[0]][sword[1]] + (n-sword[0]-1) + (m-sword[1]-1))

if visited[n-1][m-1] == 0 or visited[n-1][m-1] > t:
    print("Fail")
else:
    print(visited[n-1][m-1])
