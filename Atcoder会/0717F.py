from itertools import combinations

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

total = n * (n - 1) * (n - 2) // 6
z = 0

for a, b, c in combinations(points, 3):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
        z += 1

print(total - z)
