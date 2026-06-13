# x * (10^k - 1) ≡ 0 (mod M)になる？？
# yはぶっちゃけなんでもいい！！！
import math

MOD = 998244353

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    ans = 0
    max_k = len(str(N))

    for k in range(1, max_k + 1):
        left = 10 ** (k - 1)
        right = min(N, 10**k - 1)

        if left > right:
            continue

        cnt_y = right - left + 1

        # x * (10^k - 1) ≡ 0 mod M
        a = (pow(10, k, M) - 1) % M

        g = math.gcd(M, a)

        need = M // g
        cnt_x = N // need

        ans += (cnt_x % MOD) * (cnt_y % MOD)
        ans %= MOD

    print(ans)
