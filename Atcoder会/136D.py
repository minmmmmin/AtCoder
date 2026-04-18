# 頭パンクしそう
S = input()
N = len(S)

ans = [0] * N

# 右側
cnt = 0
for i in range(N):
    if S[i] == "R":
        cnt += 1
    else:
        ans[i] += cnt // 2
        ans[i - 1] += (cnt + 1) // 2
        cnt = 0

cnt = 0
ans = ans[::-1]

# 逆順でも同じことをする
for i in range(N):
    if S[N - 1 - i] == "L":
        cnt += 1
    else:
        ans[i] += cnt // 2
        ans[i - 1] += (cnt + 1) // 2
        cnt = 0

print(*ans[::-1], sep=" ")
