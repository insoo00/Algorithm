from collections import deque

s, t = map(int, input().split())

if s == t:
    print(0)
else:
    visited = {}  # visited는 딕셔너리로 변경
    move = {}  # move도 딕셔너리로 변경
    visited[s] = 'start'
    move[s] = None  # 시작 값을 None으로 설정

    q = deque([s])

    while q:
        cur = q.popleft()

        for next_op in ['*', '+', '-', '/']:
            if next_op == '*':
                val = cur ** 2
            elif next_op == '+':
                val = cur * 2
            elif next_op == '-':
                val = 0
            elif next_op == '/':
                if cur != 0:
                    val = 1
                else:
                    continue  # 0으로 나누는 경우는 생략

            if val > 10**9 or val < 0:  # 값이 10^9을 초과하거나 음수인 경우 제외
                continue

            if val not in visited:  # 아직 방문하지 않은 값만 처리
                visited[val] = next_op
                move[val] = cur
                q.append(val)

    if t not in visited:
        print(-1)
    else:
        result = []
        while move[t] is not None:  # 역추적
            result.append(visited[t])
            t = move[t]

        print(''.join(result[::-1]))  # 역순으로 연산 출력
