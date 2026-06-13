# さっきのDPか？？？って思ったけど違いそう
H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)

A = [[int(x) for x in row] for row in S]
# print(A)

ans = 0

# 上固定
for top in range(H):
    col_sum = [0] * W

    # 下固定
    for bottom in range(top, H):
        for c in range(W):
            col_sum[c] += A[bottom][c]

        cnt = {0: 1}

        s = 0
        for x in col_sum:
            s += x
            ans += cnt.get(s - K, 0)
            cnt[s] = cnt.get(s, 0) + 1

        # print(col_sum)

print(ans)
