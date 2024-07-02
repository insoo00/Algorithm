import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

pokemon_dick= dict()

for index in range(1, N+1):
    name = input()
    pokemon_dick[index] = name
    pokemon_dick[name] = index

for _ in range(M):
    input_string = input()
    if input_string.isdigit():
        print(pokemon_dick[int(input_string)])
    else:
        print(pokemon_dick[input_string])