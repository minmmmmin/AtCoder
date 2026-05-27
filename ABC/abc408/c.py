N, M = map(int, input().split())
diff = [0] * (N + 2)

for _ in range(M):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

min_cover = float("inf")
cur = 0
for i in range(1, N + 1):
    cur += diff[i]
    min_cover = min(min_cover, cur)

print(min_cover)
