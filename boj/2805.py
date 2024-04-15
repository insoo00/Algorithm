#1
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

#2
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

while start <= end:
    mid = (start+end)//2
    # print(f'start: {start}, end: {end}, mid: {mid}')

    sum = 0
    for tree in trees:
        if tree>mid:
            sum += tree-mid

    # print(f'sum: {sum}')
    if sum >= M:
        start = mid+1
    else:
        end = mid-1

print(end)