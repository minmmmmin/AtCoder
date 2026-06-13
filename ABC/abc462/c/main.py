n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort()

ans = 0
min_y = 10**18

for x, y in points:
    if min_y >= y:
        ans += 1
    min_y = min(min_y, y)

print(ans)
