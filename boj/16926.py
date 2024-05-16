from collections import deque

N, M, R = map(int, input().split())
nums = list()
for _ in range(N):
    nums.append(list(map(int, input().split())))

result = [[0 for _ in range(M)] for _ in range(N)]

q = deque()
left_top = [0,0]
right_top = [0, M-1]
left_bottom = [N-1, 0]
right_bottom = [N-1, M-1]

for _ in range(min(N,M)//2):
    q.clear()
    q.extend(nums[left_top[0]][left_top[1]:right_top[1]])
    q.extend([col[right_top[1]] for col in nums[right_top[0]:right_bottom[0]]])
    q.extend(nums[right_bottom[0]][right_bottom[1]:left_bottom[1]:-1])
    q.extend([col[left_bottom[1]] for col in nums[left_bottom[0]:left_top[0]:-1]])

    q.rotate(-R)

    for i in range(left_top[1], right_top[1]):
        result[left_top[0]][i] = q.popleft()
    for i in range(right_top[0], right_bottom[0]):
        result[i][right_top[1]] = q.popleft()
    for i in range(right_bottom[1], left_bottom[1], -1):
        result[right_bottom[0]][i] = q.popleft()
    for i in range(left_bottom[0], left_top[0], -1):
        result[i][left_bottom[1]] = q.popleft()

    left_top = [left_top[0]+1, left_top[1]+1]
    right_top = [right_top[0]+1, right_top[1]-1]
    left_bottom = [left_bottom[0]-1, left_bottom[1]+1]
    right_bottom = [right_bottom[0]-1, right_bottom[1]-1]

for res in result:
    print(*res)
