n, m = map(int, input().split())
chords = []

# 各直線を格納
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a  # aがbより大きければ入れ替え
    chords.append((a, b))

# 交差するペアをカウント
cross_count = 0

# 全てのペア (i, j) をチェック
for i in range(m):
    for j in range(i + 1, m):
        a1, b1 = chords[i]
        a2, b2 = chords[j]

        # 交差の条件をチェック
        if (a1 < a2 < b1 < b2) or (a2 < a1 < b2 < b1):
            cross_count += 1

print(cross_count)
