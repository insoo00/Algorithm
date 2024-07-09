import math

A, B, V = map(int, input().split())

hight = V-B
hight_per_day = A-B

days = hight / hight_per_day
print(math.ceil(days))