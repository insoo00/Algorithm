N = int(input())
street = []
for _ in range(N):
    street.append(list(map(int, input().split())))

for i in range(1, N):
    street[i][0] = street[i][0] + min(street[i-1][1], street[i-1][2])
    street[i][1] = street[i][1] + min(street[i-1][0], street[i-1][2])
    street[i][2] = street[i][2] + min(street[i-1][0], street[i-1][1])

result = min(street[-1])
print(result)
