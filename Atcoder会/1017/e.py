n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# print(a)

# 条件をちゃんと見よう
result = 10**9 + 1
t = n - k - 1
for i in range(n - t):
    result = min(result, a[i + t] - a[i])

print(result)
