# 2775
T = int(input())
apartment = []
apartment.append([_ for _ in range(1, 15)])
for i in range(1, 15):
    floor = [1]
    for j in range(1, 14):
        unit = floor[j-1] + apartment[i-1][j]
        floor.append(unit)
    apartment.append(floor)
for _ in range(T):
    K = int(input())
    N = int(input())
    print(apartment[K][N-1])
