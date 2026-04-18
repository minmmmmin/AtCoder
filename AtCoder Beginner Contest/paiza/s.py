N, m, M, T = map(int, input().split())
a = list(map(int, input().split()))

s = [0] * (N + 1)
for i in range(N):
    s[i + 1] = s[i] + a[i]

ans = 0

for l in range(N):
    for k in range(m, M + 1):
        r = l + k
        if r > N:
            break
        total = s[r] - s[l]
        if total >= T * k:
            ans += 1

print(ans)
