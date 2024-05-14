def binary_search(idx, ink):
    if idx == N-1:
        return 0

    left = idx+1
    right = N-1
    if viscosities[left] > ink:
        return 0

    else:
        while left <= right:
            mid = (left+right)//2

            if viscosities[mid] > ink:
                right = mid-1
            else:
                left = mid+1

        return (left-1)-idx

N = int(input())
inks = list(map(int, input().split()))
viscosities = list(map(int, input().split()))

result = list()
for idx, ink  in enumerate(inks):
    cnt = binary_search(idx, ink)
    result.append(cnt)

print(*result)
