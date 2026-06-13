n, d = map(int, input().split())

diff = [0] * (10**6 + 5)

for _ in range(n):
    s, t = map(int, input().split())

    left = s
    right = t - d

    if left <= right:
        diff[left] += 1
        diff[right + 1] -= 1

active = 0
ans = 0

for x in range(10**6 + 1):
    active += diff[x]
    ans += active * (active - 1) // 2

print(ans)

# 累積話たのしいかも
