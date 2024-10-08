# import sys
# sys.stdin = open("input.txt", "r")
 
T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
     
    big = list()
    small = list()
     
    if len(a) > len(b):
        big = a
        small = b
    else: 
        big = b
        small = a
 
    cnt = len(big)-len(small)+1
    result = -1e9
    small += [0]*(len(big)-len(small))
    for _ in range(cnt):
        tmp = 0
        for i in range(len(big)):
            tmp += big[i]*small[i]
        # print(f'big: {big}, small: {small}, tmp: {tmp}')
        result = max(result, tmp)
        small_last = small[-1]
        for j in range(len(small)-1, 0, -1):
            small[j] = small[j-1]
        small[0] = small_last
 
    print(f'#{test_case} {result}')
             