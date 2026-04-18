N, R, C = map(int, input().split())
S = input()

# 煙の発生位置を管理する集合
smoke_positions = set()
smoke_positions.add((0, 0))

# 焚き火の位置（風の逆方向に動かす）
fire_r, fire_c = 0, 0

# 高橋君の初期位置（風の逆方向に動かす）
takahashi_r, takahashi_c = R, C

# 風の逆方向（元の移動と逆にする）
reverse_move = {
    "N": (1, 0),
    "W": (0, 1),
    "S": (-1, 0),
    "E": (0, -1),
}

result = []

for t in range(N):
    # 風の逆方向に焚き火と高橋君を動かす
    dr, dc = reverse_move[S[t]]
    fire_r += dr
    fire_c += dc
    takahashi_r += dr
    takahashi_c += dc

    # 煙の発生位置を記録
    smoke_positions.add((fire_r, fire_c))

    # 高橋君のいる位置に煙があるか判定
    if (takahashi_r, takahashi_c) in smoke_positions:
        result.append("1")
    else:
        result.append("0")

print("".join(result))
