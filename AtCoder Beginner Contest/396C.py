N, M = map(int, input().split())  # N: 黒色ボールの個数, M: 白色ボールの個数
A = list(map(int, input().split()))  # 黒色ボールの価値
B = list(map(int, input().split()))  # 白色ボールの価値

# AとBを降順にソート
A.sort(reverse=True)
B.sort(reverse=True)

# 累積和の計算
S = [0] * (N + 1)  # 黒色ボールの累積和
T = [0] * (M + 1)  # 白色ボールの累積和
maxT = [0] * (M + 1)  # 白色ボールの累積和の最大値

# 累積和を計算
for i in range(N):
    S[i + 1] = S[i] + A[i]
for i in range(M):
    T[i + 1] = T[i] + B[i]
    maxT[i + 1] = max(maxT[i], T[i + 1])

# 答えを求める
ans = 0
for i in range(N + 1):
    ans = max(ans, S[i] + maxT[min(i, M)])

print(ans)
