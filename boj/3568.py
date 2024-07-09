import sys
input = lambda: sys.stdin.readline().rstrip()

text = input().split()

basic = text[0]
text = text[1:]

if not text:
    print(basic)

for t in text:
    t = t[:-1]
    result = basic
    alphabet = ''
    while len(t) >= 1:
        if t[-1].isalpha():
            alphabet += t[-1]
            t = t[:-1]
        elif t[-1] == ']':
            result += t[-2] + t[-1]
            t = t[:-2]
        else:
            result += t[-1]
            t = t[:-1]

    result += ' ' + alphabet[::-1] +';'
    print(result)