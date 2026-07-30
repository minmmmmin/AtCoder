n, d, p = map(int, input().split())
f = list(map(int, input().split()))

f.sort(reverse=True)

# 最小コストの初期化
ans = 0

# 各d日ごとにパスを使用するか通常料金を払うかを判断
for i in range(0, n, d):
    # d日間の通常料金合計
    cost = sum(f[i:i+d])
    # パスと通常料金のうち、安い方を選択
    ans += min(cost, p)

print(ans)
