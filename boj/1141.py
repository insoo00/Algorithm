N = int(input())
words = list()
for _ in range(N):
    words.append(input())

words = sorted(list(set(words)), key=lambda x:len(x))
cnt = len(words)
res = 0
for i in range(cnt):
    for j in range(i+1, cnt):
        if words[i] == words[j][:len(words[i])]:
            res += 1
            break

print(cnt-res)