from collections import deque

T = int(input())

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]
for _ in range(T):
    l = int(input())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    q = deque()
    q.append((startX, startY, 0))
    visited = [[False for _ in range(l)] for _ in range(l)]
    visited[startX][startY] = True
    result = 0
    while q:
        x, y, cnt = q.popleft()

        if x == endX and y == endY:
            result = cnt
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<l and 0<=ny<l:
                if not visited[nx][ny]:
                    q.append([nx, ny, cnt+1])
                    visited[nx][ny] = True

    print(cnt)