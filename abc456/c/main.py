MOD = 998244353

S = input().strip()

ans = 0
cnt = 0

for i in range(len(S)):
    if i == 0 or S[i] != S[i - 1]:
        cnt += 1
    else:
        cnt = 1

    ans += cnt
    ans %= MOD

print(ans)