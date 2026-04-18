n = int(input())
departments = list(map(int, input().split()))

total_sum = sum(departments)
half_sum = total_sum // 2

dp = [False] * (half_sum + 1)
dp[0] = True

for department in departments:
    for j in range(half_sum, department - 1, -1):
        dp[j] = dp[j] or dp[j - department]

for i in range(half_sum, -1, -1):
    if dp[i]:
        result = max(i, total_sum - i)
        print(result)
        break
