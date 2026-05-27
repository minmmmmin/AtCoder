from itertools import product

# 標準入力からN, K, R1, R2, ..., RNを取得
N, K = map(int, input().split())
R = list(map(int, input().split()))

# 全ての可能な整数列を生成
all_combinations = list(product(*[range(1, r + 1) for r in R]))

# 条件を満たす組み合わせを選別
valid_combinations = [combo for combo in all_combinations if sum(combo) % K == 0]

# 辞書順でソート
valid_combinations.sort()

# 結果を出力
for combo in valid_combinations:
    print(*combo)
