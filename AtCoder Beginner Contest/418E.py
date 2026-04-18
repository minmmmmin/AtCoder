import sys
import math

input = sys.stdin.readline


# 平行のペアから平行四辺形引けばよくね

N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

dir_count = {}
mid = {}

for i in range(N):
    x1, y1 = P[i]
    for j in range(i + 1, N):
        x2, y2 = P[j]
        dx, dy = x2 - x1, y2 - y1

        g = math.gcd(dx if dx >= 0 else -dx, dy if dy >= 0 else -dy)
        dx //= g
        dy //= g
        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy
        dir_count[(dx, dy)] = dir_count.get((dx, dy), 0) + 1

        mid[(x1 + x2, y1 + y2)] = mid.get((x1 + x2, y1 + y2), 0) + 1

ans = 0
for v in dir_count.values():
    ans += (v * (v - 1)) // 2
for v in mid.values():
    ans -= (v * (v - 1)) // 2

print(ans)
