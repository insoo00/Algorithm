def is_possible(K, N, M, expenses):
    # K원이 주어졌을 때, M번 이하로 인출이 가능한지 확인하는 함수
    count = 1  # 최소 1번 인출은 해야 하므로 1로 시작
    current_sum = 0
    
    for expense in expenses:
        if current_sum + expense > K:
            # 현재 인출 금액에 추가하면 넘치면 새로운 인출 시작
            count += 1
            current_sum = expense
            if count > M:
                return False
        else:
            current_sum += expense
            
    return True

def find_minimum_K(N, M, expenses):
    low = max(expenses)  # 최소 K는 최대 금액 이상이어야 한다.
    high = sum(expenses)  # 최대 K는 모든 금액을 한 번에 인출하는 금액이다.
    
    while low <= high:
        mid = (low + high) // 2
        
        if is_possible(mid, N, M, expenses):
            high = mid - 1  # K가 가능하면 더 작은 K를 찾아본다.
        else:
            low = mid + 1  # K가 너무 작으면 더 큰 K를 찾아본다.
    
    return low  # low가 최소 K 값

# 입력 받기
N, M = map(int, input().split())
expenses = [int(input()) for _ in range(N)]

# 최소 K 찾기
result = find_minimum_K(N, M, expenses)
print(result)
