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