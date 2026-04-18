MOD = 1000000007

N = int(input().strip())

# 包除原理を考える
ans = (pow(10, N, MOD) - 2 * pow(9, N, MOD) + pow(8, N, MOD)) % MOD
print(ans)
