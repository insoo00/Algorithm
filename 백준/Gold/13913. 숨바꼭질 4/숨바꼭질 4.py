from collections import deque

N, K = map(int, input().split())

field = [-1 for _ in range(10**5+1)]
field[N] = 0
answer = []

q = deque()
q.append(N)

while q:
    cur = q.popleft()

    if cur == K:
        while cur != N:
            answer.append(cur)
            cur = field[cur]
        answer.append(N)
        break

    for next in [cur-1, cur+1, cur*2]:
        if next<0 or next>10**5:
            continue
        if field[next] == -1:
            field[next] = cur
            q.append(next)

print(len(answer)-1)
print(*answer[::-1])