import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
button = set(str(num) for num in range(0, 10))

if M:
    disable_button = set(input().split())
    button = button - disable_button

result = abs(100-N)
for num in range(1000001):
    num = str(num)
    num_length = len(num)
    for n in range(num_length):
        if num[n] not in button:
            break
        if n == num_length-1:
            result = min(result, abs(N-int(num))+num_length)
print(result)
