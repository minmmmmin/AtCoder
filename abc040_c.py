n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

dp[1] = abs(a[1] - a[0])

# i-2 からジャンプか i-1 からジャンプの小さいほうを採用
for i in range(2, n):
    dp[i] = min(dp[i - 2] + abs(a[i] - a[i - 2]), dp[i - 1] + abs(a[i] - a[i - 1]))

print(dp[n - 1])
