N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

k1_left = max(1 - A, 1 - B)
k1_right = min(N - A, N - B)

k2_left = max(1 - A, B - N)
k2_right = min(N - A, B - 1)


leftup_gyou, leftup_retu = A + k1_left, B + k1_left
rightlow_gyou, rightlow_retu = A + k1_right, B + k1_right
rightup_gyou, rightup_retu = A + k2_left, B - k2_left
leftlow_gyou, leftlow_retu = A + k2_right, B - k2_right

ans = [["."] * (S - R + 1 + 1) for i in range(Q - P + 1 + 1)]

for i in range(P, Q + 1):
    for j in range(R, S + 1):
        if leftup_gyou <= i <= rightlow_gyou and leftup_retu <= j <= rightlow_retu:
            if i - leftup_gyou == j - leftup_retu:
                ans[i - P + 1][j - R + 1] = "#"
        if rightup_gyou <= i <= leftlow_gyou and leftlow_retu <= j <= rightup_retu:
            if leftlow_gyou - i == j - leftlow_retu:
                ans[i - P + 1][j - R + 1] = "#"

for gyou in range(1, Q - P + 1 + 1):
    ans_gyou = ""
    for retu in range(1, S - R + 1 + 1):
        ans_gyou += ans[gyou][retu]
    print(ans_gyou)
