expression = input()

def exec_add(exp):
    num = 0
    for e in exp.split('+'):
        num += int(e)
    return num

result = 0
for idx, exp in enumerate(expression.split('-')):
    tmp = exec_add(exp)
    if idx == 0:
        result += tmp
    else:
        result -= tmp

print(result)
