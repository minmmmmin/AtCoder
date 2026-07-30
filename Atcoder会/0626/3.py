from math import sqrt

n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = []
for _ in range(n):
    xy.append(list(map(int, input().split())))

ans = 0

for i in range(n):
    x, y = xy[i]
    r = float("inf")
    for j in range(k):
        light_person_index = a[j] - 1
        x2, y2 = xy[light_person_index]
        r = min(r, (x - x2) ** 2 + (y - y2) ** 2)
    ans = max(ans, r)

print(sqrt(ans))
