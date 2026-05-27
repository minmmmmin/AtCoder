n, h, m = map(int, input().split())
monsters = [tuple(map(int, input().split())) for _ in range(n)]

dp = {}
dp[(h, m)] = 0

for a, b in monsters:
    next_dp = {}
    for (cur_h, cur_m), count in dp.items():
        # スキップ（何もしない）
        key = (cur_h, cur_m)
        if key in next_dp:
            next_dp[key] = max(next_dp[key], count)
        else:
            next_dp[key] = count

        # 体力で戦う
        if cur_h >= a:
            key = (cur_h - a, cur_m)
            if key in next_dp:
                next_dp[key] = max(next_dp[key], count + 1)
            else:
                next_dp[key] = count + 1

        # 魔力で戦う
        if cur_m >= b:
            key = (cur_h, cur_m - b)
            if key in next_dp:
                next_dp[key] = max(next_dp[key], count + 1)
            else:
                next_dp[key] = count + 1

    dp = next_dp

print(max(dp.values()))
