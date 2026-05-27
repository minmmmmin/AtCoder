MOD = 998244353

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

# 絶対値を境界で分けたい

pref = [0] * (m + 1)
for i in range(m):
    pref[i + 1] = pref[i] + b[i]
total_b = pref[m]

ans = 0
k = 0

for x in a:
    while k < m and b[k] <= x:
        k += 1

    sum_left = pref[k]
    sum_right = total_b - sum_left

    ans += x * k - sum_left
    ans += sum_right - x * (m - k)
    ans %= MOD

print(ans)
