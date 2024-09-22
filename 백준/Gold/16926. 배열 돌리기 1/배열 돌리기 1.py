from collections import deque

n, m, r = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(n)]
result = [[0 for _ in range(m)] for _ in range(n)]

q = deque()
left_top = [0,0]
right_top = [0, m-1]
left_bottom = [n-1, 0]
right_bottom = [n-1, m-1]

for _ in range(min(n,m)//2):
    q.clear()
    q.extend(nums[left_top[0]][left_top[1]:right_top[1]])
    q.extend([col[right_top[1]] for col in nums[right_top[0]:right_bottom[0]]])
    q.extend(nums[right_bottom[0]][right_bottom[1]:left_bottom[1]:-1])
    q.extend([col[left_bottom[1]] for col in nums[left_bottom[0]:left_top[0]:-1]])
    q.rotate(-r)

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
