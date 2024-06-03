import sys
sys.stdin = open("2072/input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    res = 0
    nums = map(int, input().split())
    for num in nums:
        if num % 2 == 1:
            res += num

    print(f"#{test_case} {res}")
