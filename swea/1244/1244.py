import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    nums, cnt = map(int, input().split())
    nums = str(nums)
    nums = list(map(int, nums))
    nums_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for num in nums:
        nums_dict[num] += 1

    for i in range(cnt):
        idx = 0
        max_num = max(nums)
        if nums[idx] != max_num:
            if nums_dict[max_num] > 1:
                continue



