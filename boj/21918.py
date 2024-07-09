def toggle(operand1, operand2):
    global lights
    for i in range(operand1-1, operand2):
        if lights[i] == 0:
            lights[i] = 1
        else:
            lights[i] = 0

def turn_off(operand1, operand2):
    global lights
    for i in range(operand1-1, operand2):
        lights[i] = 0

def turn_on(operand1, operand2):
    global lights
    for i in range(operand1-1, operand2):
        lights[i] = 1

N, M = map(int, input().split())
lights = list(map(int, input().split()))
for _ in range(M):
    opcode, operand1, operand2 = map(int, input().split())
    
    if opcode == 1:
        lights[operand1-1] = operand2
    elif opcode == 2:
        toggle(operand1, operand2)
    elif opcode == 3:
        turn_off(operand1, operand2)
    else:
        turn_on(operand1, operand2)

print(*lights)
