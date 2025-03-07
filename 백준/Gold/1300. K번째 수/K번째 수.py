N = int(input())
K = int(input())

start = 1
end = N * N
result = -1

while start <= end:
    mid = (start+end)//2
    total = 0

    for row in range(1, N+1):
        total += min((mid//row), N)

    if total >= K:
        result = mid
        end = mid-1
    else:
        start = mid+1
    

print(result)
