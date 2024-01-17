import sys
input = lambda: sys.stdin.readline().rstrip()

a, b = map(int, input().split())
big, small = max(a, b), min(a, b)

def gcd(big, small):
    while small > 0:
        big, small = small, big % small
    return big

def lcm(big, small):
    return big * small // gcd(big, small)

print(gcd(big, small))
print(lcm(big, small))