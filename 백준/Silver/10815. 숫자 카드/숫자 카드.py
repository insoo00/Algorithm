n = int(input())
n_list = sorted(list(map(int, input().split())))

m = int(input())
m_list = list(map(int, input().split()))

result = []

for idx in range(m):
    target = m_list[idx]
    left = 0
    right = n-1
    flag = False

    while left <= right:
        mid = (left+right)//2
        # print(f'left: {left} \t right: {right} \t mid: {mid}')

        if n_list[mid] == target:
            flag = True
            break

        if n_list[mid] < target:
            left = mid+1
        else:
            right = mid-1
        
    if flag:
        result.append(1)
    else:
        result.append(0)

print(*result)