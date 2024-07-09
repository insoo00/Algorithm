# two pointer
N = int(input())
liquids = list(map(int, input().split()))

left_idx = 0
right_idx = N-1

sum_min = float('INF')
result = [0, 0]
while left_idx < right_idx:
    sum_tmp = liquids[left_idx] + liquids[right_idx]

    if abs(sum_tmp) < sum_min:
        sum_min = abs(sum_tmp)
        result[0] = liquids[left_idx]
        result[1] = liquids[right_idx]

        if sum_min == 0:
            break

    if sum_tmp > 0:
        right_idx -= 1
    else:
        left_idx += 1

print(*result)


# binary_search
N = int(input())
liquids = list(map(int, input().split()))

sum_min = float('INF')
result = [0, 0]

for i in range(N-1):
    current = liquids[i]

    left = i+1
    right = N-1

    while left <= right:
        mid = (left+right)//2
        sum_tmp = current+liquids[mid]

        if abs(sum_tmp) < sum_min:
            sum_min = abs(sum_tmp)
            result[0] = current
            result[1] = liquids[mid]

            if sum_min == 0:
                break
            
        if sum_tmp < 0:
            left = mid+1
        else:
            right = mid-1


print(*result)

