# https://school.programmers.co.kr/learn/courses/20848/lessons/255907

from collections import deque

field, visited, result = [], [], []
INF = int(1e9)


def bfs(n, m):
    global field, visited, result, INF
    visited[1][1][False] = True
    result[1][1][0] = 0
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    q.append((1, 1, False))

    while q:
        y, x, jump = q.popleft()
        # print(f'y: {y}, x:{x}, jump: {jump}')
        
        if jump == False:
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]

                if 0<ny<=m and 0<nx<=n:
                    if not visited[ny][nx][False]:
                        if field[ny][nx] != -1:
                            visited[ny][nx][False] = True
                            result[ny][nx][0] = min(result[ny][nx][0], result[y][x][0]+1)
                            q.append((ny, nx, False))

                ny = ny+dy[i]
                nx = nx+dx[i]

                if 0<ny<=m and 0<nx<=n:
                    if not visited[ny][nx][True]:
                        if field[ny][nx] != -1:
                            visited[ny][nx][True] = True
                            result[ny][nx][1] = min(result[ny][nx][1], result[y][x][0]+1)
                            q.append((ny, nx, True))
        else:
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                
                if 0<ny<=m and 0<nx<=n:
                    if not visited[ny][nx][True]:
                        if field[ny][nx] != -1:
                            visited[ny][nx][True] = True
                            result[ny][nx][1] = min(result[ny][nx][1], result[y][x][1]+1)
                            q.append((ny, nx, True))
                            
    if result[m][n][1] != INF:
        return result[m][n][1]
    else:
        return -1
    
def solution(n, m, hole):
    global field, visited, result, INF
    answer = -1
    field = [[0 for _ in range(n+1)] for _ in range(m+1)]
    visited = [[[False for _ in range(2)] for _ in range(n+1)] for _ in range(m+1)]
    result = [[[INF for _ in range(2)] for _ in range(n+1)] for _ in range(m+1)]

    for x, y in hole:
        field[y][x] = -1
        
    answer = bfs(n, m)
    return answer
