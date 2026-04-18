# 連続部分列ってなんだよしらねーよのきもち
N = int(input())
A = list(map(int, input().split()))

# 要素の最後の出現位置を記録する辞書
last_seen = {}

# 最小長さを初期化（とりあえず最長の長さより大きいのにする）
min_length = N + 1

for i in range(N):
    if A[i] in last_seen:
        # 同じ要素がすでに出現していれば、長さを計算
        length = i - last_seen[A[i]] + 1
        min_length = min(min_length, length)
    last_seen[A[i]] = i

if min_length == N + 1:
    print(-1)
else:
    print(min_length)
