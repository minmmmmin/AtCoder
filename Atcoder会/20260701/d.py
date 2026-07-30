n, k = map(int, input().split())
p = list(map(int, input().split()))

s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + p[i]

ans = max(s[i + k] - s[i] for i in range(n - k + 1))
print(ans)
