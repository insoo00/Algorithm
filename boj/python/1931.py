import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

meetings = list()
for _ in range(n):
    start, end = map(int, input().split())
    meeting = [start, end]
    meetings.append(meeting)
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
time = 0
for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        cnt += 1

print(cnt)