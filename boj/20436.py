keyboard = {
    "q": [0, 2],
    "w": [1, 2],
    "e": [2, 2],
    "r": [3, 2],
    "t": [4, 2],
    "y": [5, 2],
    "u": [6, 2],
    "i": [7, 2],
    "o": [8, 2],
    "p": [9, 2],
    "a": [0, 1], 
    "s": [1, 1],
    "d": [2, 1],
    "f": [3, 1],
    "g": [4, 1],
    "h": [5, 1],
    "j": [6, 1],
    "k": [7, 1],
    "l": [8, 1],
    "z": [0,0],
    "x": [1,0],
    "c": [2,0],
    "v": [3,0],
    "b": [4,0],
    "n": [5,0],
    "m": [6,0]
}

left = set(["q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v"])

L, R = input().split()
data = input()
result = 0

for alpha in data:
    result += 1
    if alpha in left:
        result += abs(keyboard[L][1] - keyboard[alpha][1]) + abs(keyboard[L][0] - keyboard[alpha][0])
        L = alpha
    else:
        result += abs(keyboard[R][1] - keyboard[alpha][1]) + abs(keyboard[R][0] - keyboard[alpha][0])
        R = alpha

print(result)
