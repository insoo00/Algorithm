from collections import defaultdict

N, d, k, c = map(int, input().split())
plate = [int(input()) for _ in range(N)]
plate.extend(plate) 

left, right = 0, 0
window = defaultdict(int)
window[c] += 1
while right < k:
    window[plate[right]] += 1
    right += 1

result = len(window)
for _ in range(N-1):
    window[plate[right]] += 1
    window[plate[left]] -= 1
    if window[plate[left]] == 0:
        window.pop(plate[left])
    right += 1
    left += 1
    result = max(len(window), result)

print(result)