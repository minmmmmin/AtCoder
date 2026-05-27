n = int(input())

min_r = 10**18
max_r = -(10**18)
min_c = 10**18
max_c = -(10**18)

for _ in range(n):
    r, c = map(int, input().split())
    if r < min_r:
        min_r = r
    if r > max_r:
        max_r = r
    if c < min_c:
        min_c = c
    if c > max_c:
        max_c = c

width_r = max_r - min_r
width_c = max_c - min_c
ans = max(width_r, width_c)
print((ans + 1) // 2)
