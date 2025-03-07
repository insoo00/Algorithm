import sys

n, m = map(int,sys.stdin.readline().split())
money = []
for i in range(n): #사용 금액 입력 받기
    money.append(int(sys.stdin.readline()))

start, end = max(money), sum(money)

while start <= end: #매개변수 탐색
    mid = (start + end) // 2 #인출 금액
    charge = mid #인출 금액
    count = 1
    for i in money: 
        if charge - i < 0: #부족해서 다시 인출
            count += 1
            charge = mid
        charge -= i #사용한 만큼 차감
    if count > m: #인출 액수 증가 필요
        start = mid + 1
    else: #인출 액수 감소 필요
        end = mid - 1
print(mid)
