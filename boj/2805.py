import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start+end)//2

    sum = 0
    for tree in trees:
        if tree>mid:
            sum += tree-mid
        
    if sum >= M:
        start = mid+1
    else:
        end = mid-1

print(end)