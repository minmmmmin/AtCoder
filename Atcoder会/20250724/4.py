x, k = map(int, input().split())

for i in range(k):
    p = 10**i
    if x % (p * 10) >= 5 * p:
        x = (x // (p * 10) + 1) * (p * 10)
    else:
        x = (x // (p * 10)) * (p * 10)

print(x)
