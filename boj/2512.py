import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
val = list(map(int, input().split()))
budget = int(input())

def find_number(start, end):
    while start <= end:
        cur = 0
        mid = (start + end) // 2
        for v in val:
            if v > mid:
                cur += mid
            else:
                cur += v
        if cur <= budget:
            start = mid+1
        else:
            end = mid-1
    return end

print(find_number(0, max(val)))