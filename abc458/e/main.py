# これ解かないとレート下がる
MOD = 998244353

X1, X2, X3 = map(int, input().split())

# 1と3はダメだから最初に2だけ
m = X2 + 1

MAX = max(X1, X2 + X3 + 5, X2 + 5)

fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD

invfact = [1] * (MAX + 1)
invfact[MAX] = pow(fact[MAX], MOD - 2, MOD)
for i in range(MAX, 0, -1):
    invfact[i - 1] = invfact[i] * i % MOD

ans = 0

# 1を置く場所
for i in range(1, min(X1, m - 1) + 1):
    # 1を入れる隙間の数
    c1 = fact[m] * invfact[i] % MOD * invfact[m - i] % MOD

    # その隙間に1を入れる組み合わせ
    c2 = fact[X1 - 1] * invfact[i - 1] % MOD * invfact[X1 - i] % MOD

    # 残りの3をぶちこむ
    c3 = fact[m - i + X3 - 1] * invfact[m - i - 1] % MOD * invfact[X3] % MOD

    ans += c1 * c2 % MOD * c3 % MOD
    ans %= MOD

print(ans)