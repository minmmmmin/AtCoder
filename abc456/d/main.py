# cはわかったけどこれはわからんて
# 部分列？？？？？DPとかいうやつですか
# ケツにこの文字が入れる時を考えればいいのかな

MOD = 998244353

S = input().strip()

dp = {'a': 0, 'b': 0, 'c': 0}

for ch in S:
    if ch == 'a':
        new = 1 + dp['b'] + dp['c']
    elif ch == 'b':
        new = 1 + dp['a'] + dp['c']
    else:
        new = 1 + dp['a'] + dp['b']

    dp[ch] = (dp[ch] + new) % MOD

ans = (dp['a'] + dp['b'] + dp['c']) % MOD
print(ans)