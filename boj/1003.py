# 1003
# https://dduniverse.tistory.com/entry/%EB%B0%B1%EC%A4%80-1003-DP-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%ED%95%A8%EC%88%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
dp = [-1 for _ in range(41)]
dp[0] = 0
dp[1] = 1

def fibonacci(n):
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibonacci(n-1) + fibonacci(n-2)
    return dp[n]

T = int(input())
for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
    else:
        print(fibonacci(N-1), fibonacci(N))
