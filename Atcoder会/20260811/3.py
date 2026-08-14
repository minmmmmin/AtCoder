# 脳筋全探索なのでは？
n = int(input())
a = list(map(int, input().split()))

answer = 10**18

for x in range(-100, 101):
    cost = 0

    for i in range(n):
        cost += (a[i] - x) ** 2

    answer = min(answer, cost)

print(answer)
