n, m = map(int, input().split())

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())

for _ in range(m):
    m_set.add(input())

n_m_set = n_set & m_set

print(len(n_m_set))
for name in sorted(n_m_set):
    print(name)