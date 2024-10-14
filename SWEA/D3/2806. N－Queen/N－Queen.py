T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    result = 0
    field = [0 for _ in range(N)]

    def validate(current):
        for before in range(current):
            if((field[before] == field[current]) or (abs(field[before]-field[current])==abs(before-current))):
                return False
        return True

    def dfs(row):
        global result
        if row == N:
            result += 1
        else:
            for i in range(N):
                field[row] = i
                if validate(row):
                    dfs(row+1)

    dfs(0)
    print(f'#{test_case} {result}')