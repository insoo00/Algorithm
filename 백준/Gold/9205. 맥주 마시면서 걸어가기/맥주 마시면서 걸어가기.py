from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    departure = list(map(int, input().split()))
    convenience_store = list()
    for _ in range(N):
        convenience_store.append(list(map(int, input().split())))
    arrival = list(map(int, input().split()))
    visited = [False for _ in range(N+1)]

    q = deque()
    q.append(departure)
    flag = False

    while q:
        x, y = q.popleft()
        
        if abs(x-arrival[0]) + abs(y-arrival[1]) <= 1000:
            flag = True
            break
        
        for i in range(N):
            if not visited[i]:
                next_x, next_y = convenience_store[i]
                if abs(x-next_x) + abs(y-next_y) <= 1000:
                    visited[i] = True
                    q.append([next_x, next_y])

    if flag == True:
        print("happy")
    else:
        print("sad")
        




