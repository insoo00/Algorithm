import sys
sys.stdin = open("sample_input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    builds = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        max_build = max(builds[i-1], builds[i-2], builds[i+1], builds[i+2])
        tmp_result = builds[i] - max_build
        if tmp_result > 0:
            result += tmp_result
    print(f'#{test_case} {result}')
