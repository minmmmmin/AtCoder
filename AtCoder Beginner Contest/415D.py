import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = []

for _ in range(m):
    a, b = map(int, input().split())
    d.append((a - b, a))

d.sort()

ans = 0

for di, ai in d:
    if n < ai:
        continue
    x = (n - ai) // di + 1
    ans += x
    n -= di * x
print(ans)
