n = int(input())

num = set()
limit = 10**6
for i in range(2, limit):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        num.add(i)

num = list(num)
p = 0
ans = 0

for _ in range(0, len(num) + 1):
    p = min(num[i] - 1, n // (num[i] ** 3))
    if p * num[i] ** 3 == n:
        ans += 1

print(ans)

# 二分探索でいいらしい
