n = int(input())

initial_left, initial_mid, initial_right = map(int, input().split())
list_max = [initial_left, initial_mid, initial_right]
list_min = [initial_left, initial_mid, initial_right]

for _ in range(n-1):
    left, mid, right = map(int, input().split())
    list_max = [left+max(list_max[0], list_max[1]), mid+max(list_max), right+max(list_max[1], list_max[2])]
    list_min = [left+min(list_min[0], list_min[1]), mid+min(list_min), right+min(list_min[1], list_min[2])]

print(max(list_max), min(list_min))
