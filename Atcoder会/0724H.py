n, x = map(int, input().split())
x += 1
T = list(map(int, input().split()))
MOD = 998244353

DP = [0] * (x)


def prob(bunshi, bunbo):
    return (bunshi * pow(bunbo, -1, MOD)) % MOD


DP[0] = prob(1, 1)

for time in range(x):
    for i in range(n):
        t = T[i]
        if time + t < x:
            DP[time + t] = (DP[time + t] + prob(DP[time], n)) % MOD

ans = 0
for i in range(max(0, x - T[0]), x):
    ans = (ans + prob(DP[i], n)) % MOD
print(ans)
