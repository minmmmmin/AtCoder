import math
n = int(input())
x = list(map(int, input().split()))

ans_man = 0
ans_you = 0
ans_che = 0
for i in range(n):
    ans_man += abs(x[i])
    ans_you += abs(x[i] ** 2)
    ans_che = max(ans_che, abs(x[i]))
print(ans_man)
print(math.sqrt(ans_you))
print(ans_che)
