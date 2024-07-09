from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def count_virus():
    q = deque()
    tmp_field = copy.deepcopy(field)
    for i in range(N):
        for j in range(M):
            if tmp_field[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0<=nx<N) and (0<=ny<M):
                if tmp_field[nx][ny] == 0:
                    tmp_field[nx][ny] = 2
                    q.append((nx, ny))

    global result
    cnt = 0
    for i in range(N):
        for k in range(M):
            if tmp_field[i][k] == 0:
                cnt += 1
    result = max(result, cnt)


def select_wall(cnt):
    if cnt == 3:
        count_virus()
        return 
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                field[i][j] = 1
                select_wall(cnt+1)
                field[i][j] = 0

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

result = 0
select_wall(0)

print(result)

