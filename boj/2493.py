from collections import deque

N = int(input())
towers = list(map(int, input().split()))

stack = deque()
answer = [0]*N

for idx in range(N):
    while stack:
        if stack[-1][1] < towers[idx]: 
            stack.pop()
        else:
            answer[idx] = stack[-1][0]+1
            break
    stack.append((idx, towers[idx]))

print(*answer)
