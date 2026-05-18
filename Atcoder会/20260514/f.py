mod = 998244353
N = int(input())

answer = 0
pow = 0

# 桁数を知りたい
while N >= 10 ** pow:
    pow += 1
pow -= 1

# 一番上の桁
a = N - (10 ** pow) + 1

# 桁ごとに見る
for i in range(pow, 0, -1):
    n = 10 ** i - (10 ** (i - 1))
    answer += ((1 + n) * n) // 2
    answer %= mod

# 最後に最上位桁を足す
answer += ((1 + a) * a) // 2
answer %= mod

print(answer)