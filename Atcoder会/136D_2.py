S = input()
N = len(S)

LOG = 60  # 十分大きければOK（最大で10^18ステップまで対応可）

# dp[k][i]: i番目の子が2^kステップ後にどこにいるか
dp = [[0] * N for _ in range(LOG)]

# 初期状態：1ステップ後の位置
for i in range(N):
    if S[i] == "R":
        dp[0][i] = i + 1
    else:
        dp[0][i] = i - 1

# ダブリングのテーブル構築
for k in range(1, LOG):
    for i in range(N):
        dp[k][i] = dp[k - 1][dp[k - 1][i]]

# 全員を2^60ステップ後にジャンプ（十分なステップで最終位置に収束）
final_pos = [0] * N
for i in range(N):
    pos = i
    for k in range(LOG):
        pos = dp[k][pos]
    final_pos[i] = pos

# 各場所に何人いるか数える
ans = [0] * N
for p in final_pos:
    ans[p] += 1

print(*ans)
