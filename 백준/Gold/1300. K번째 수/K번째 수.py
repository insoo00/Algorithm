def find_kth_smallest(N, k):
    start, end = 1, N * N  # 배열에 존재할 수 있는 가장 작은 값과 큰 값
    
    while start <= end:
        mid = (start + end) // 2  # 중간값
        total = 0  # mid보다 작거나 같은 값의 개수를 셈
        
        # 각 행에 대해 mid보다 작은 값들의 개수를 계산
        for i in range(1, N + 1):
            total += min(mid // i, N)
        
        # 만약 total이 k 이상이라면, mid는 k번째 값이거나 그보다 크므로 범위를 좁힘
        if total >= k:
            result = mid
            end = mid - 1
        # total이 k 미만이라면, mid는 k번째 값보다 작다는 뜻이므로 범위를 넓힘
        else:
            start = mid + 1
    
    return result

# 입력 처리
N = int(input())
k = int(input())

# 결과 출력
print(find_kth_smallest(N, k))
