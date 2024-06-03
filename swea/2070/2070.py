import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    result = ''
    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    else:
        result = '='
    print(f'#{test_case} {result}')