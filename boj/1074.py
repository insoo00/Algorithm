# 메모리 초과

# def div_con(start_r, start_c, size):
#     global cnt
#     if size == 2:
#         field[start_r][start_c] = cnt
#         cnt += 1
#         field[start_r][start_c+1] = cnt
#         cnt += 1
#         field[start_r+1][start_c] = cnt
#         cnt += 1
#         field[start_r+1][start_c+1] = cnt
#         cnt += 1
#     else:
#         size //= 2
#         div_con(start_r, start_c, size)
#         div_con(start_r, start_c + size, size) 
#         div_con(start_r + size, start_c, size) 
#         div_con(start_r + size, start_c + size, size) 

# N, r, c = map(int, input().split())
# N = 2 ** N

# field = [[0] * N for _ in range(N)]
# cnt = 0

# div_con(0, 0, N)
# print(field[r][c])


N, r, c = map(int, input().split())
N = 2**N
cnt = 0

while N != 1:
    start = [i * ((N*N)//4) for i in range(4)]
    if r < N//2 and c < N//2:       # 제 1사분면
        cnt = cnt + start[0]
    elif r < N//2 and c >= N//2:    # 제 2사분면
        cnt = cnt + start[1]
        c = c - N//2
    elif r >= N//2 and c < N//2:    # 제 3사분면
        cnt = cnt + start[2]
        r = r- N//2
    else:                           # 제 4사분면
        cnt = cnt + start[3]
        r = r- N//2
        c = c - N//2
    N = N//2

print(cnt)