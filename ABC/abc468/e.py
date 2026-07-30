# MODの問題きたよ
MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

# おなじまい
inv = [0] * (N + 1)
inv[1] = 1

for i in range(2, N + 1):
    inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

h = [0] * (N + 1)

for i in range(1, N + 1):
    h[i] = (h[i - 1] + inv[i]) % MOD

x = h[N]
ans = 0

for i in range(N):
    ans = (ans + A[i] * x) % MOD

    if i < N - 1:
        x += h[N - i - 1] - h[i + 1]
        x %= MOD

print(ans)
