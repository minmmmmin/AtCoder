N = int(input())
S = input()

# 1の位置をリストに格納
ones_indices = []
for i in range(N):
    if S[i] == "1":
        ones_indices.append(i)

# 中心を取ってその周りに1を集めてみる
median_index = len(ones_indices) // 2
median_position = ones_indices[median_index]

# 操作回数の計算
ans = 0
for i in range(len(ones_indices)):
    index = ones_indices[i]
    # 集まってほしいところ
    target_position = median_position - (median_index - i)
    ans += abs(index - target_position)

print(ans)
