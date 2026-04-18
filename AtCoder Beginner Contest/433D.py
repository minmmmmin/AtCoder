from collections import defaultdict

n, M = map(int, input().split())
A = list(map(int, input().split()))


def digits(x):
    return len(str(x))


pow10 = [1] * 11
for d in range(1, 11):
    pow10[d] = (pow10[d - 1] * 10) % M

bucket = [defaultdict(int) for _ in range(11)]

for x in A:
    d = digits(x)
    r = x % M
    bucket[d][r] += 1

ans = 0

for y in A:
    dy = digits(y)
    y_mod = y % M

    for d in range(1, 11):
        need = (-y_mod) % M
        for r, cnt in bucket[d].items():
            if (r * pow10[dy] + y_mod) % M == 0:
                ans += cnt
print(ans)
