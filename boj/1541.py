#1
import sys
input = lambda: sys.stdin.readline().rstrip()

nums = input().split('-')
nums_eval = list()

for num in nums:
    eval = 0
    for n in num.split('+'):
        eval += int(n)
    nums_eval.append(eval)
    
result = nums_eval[0]
for num_eval in nums_eval[1:]:
    result -= num_eval

print(result)

#2
expression = input()
expression_list = []

number = ''
for idx, item in enumerate(expression):
    if item == '+':
        if number != '':
            expression_list.append(int(number))
            number = ''
        expression_list.append(item)
    elif item == '-':
        if number != '':
            expression_list.append(int(number))
            number = ''
        expression_list.append(item)
    else:
        number += item
        if idx == len(expression)-1:
            expression_list.append(int(number))

result = ''
has_minus = False
for idx, item in enumerate(expression_list):
    if item == '-':
        if has_minus == False:
            result += '-('
            has_minus = True
        else:
            result += ')-('
    elif item == '+':
        result += item
    else:
        result += str(item)
    
    if idx == len(expression_list)-1:
        if has_minus == True:
            result += ')'

print(eval(result))