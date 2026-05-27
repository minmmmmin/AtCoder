MOD = 998244353

T = int(input())
for _ in range(T):
    N_str, K_str = input().split()
    N = int(N_str)
    K = int(K_str)

    bin_N = bin(N)[2:]
    L = len(bin_N)

    dp = [[[[0, 0] for _ in range(2)] for _ in range(K + 2)] for _ in range(L + 1)]
    dp[0][0][1] = [1, 0]

    for pos in range(L):
        for cnt in range(K + 1):
            for tight in range(2):
                cnt_now, sum_now = dp[pos][cnt][tight]
                if cnt_now == 0:
                    continue

                limit = int(bin_N[pos]) if tight == 1 else 1
                for d in range(0, limit + 1):
                    next_cnt = cnt + d
                    if next_cnt > K:
                        continue
                    next_tight = 1 if (tight == 1 and d == limit) else 0

                    val = d * (1 << (L - pos - 1))
                    dp[pos + 1][next_cnt][next_tight][0] += cnt_now
                    dp[pos + 1][next_cnt][next_tight][1] += sum_now + val * cnt_now

                    dp[pos + 1][next_cnt][next_tight][0] %= MOD
                    dp[pos + 1][next_cnt][next_tight][1] %= MOD

    ans = (dp[L][K][0][1] + dp[L][K][1][1]) % MOD
    print(ans)
