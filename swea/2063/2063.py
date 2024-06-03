import sys
sys.stdin = open("input.txt", "r")

N = int(input())
nums = sorted(list(map(int, input().split())))

print(nums[N//2])

