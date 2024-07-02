import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

field = list()
for _ in range(N):
    colors = input()
    colors_list = list()
    for color in colors:
        colors_list.append(color)
    field.append(colors_list)

def get_cnt():
    row_cnt, col_cnt = 1, 1
    
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if field[i][j] == field[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            row_cnt = max(row_cnt, cnt)

        cnt = 1
        for j in range(N-1):
            if field[j][i] == field[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            col_cnt = max(col_cnt, cnt)

    return max(row_cnt, col_cnt)


result = 0
for i in range(N):
    for j in range(N-1):
        if j+1 < N and field[i][j] != field[i][j+1]:
            field[i][j], field[i][j+1] = field[i][j+1], field[i][j]
            result = max(result, get_cnt())
            field[i][j], field[i][j+1] = field[i][j+1], field[i][j]
        if i+1 < N and field[i][j] != field[i+1][j]:
            field[i][j], field[i+1][j] = field[i+1][j], field[i][j]
            result = max(result, get_cnt())
            field[i][j], field[i+1][j] = field[i+1][j], field[i][j]

print(result)


