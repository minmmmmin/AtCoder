x, k = map(int, input().split())

ans = 0

for i in range(k):
    ans = (x + 5 * 10**i) // 10 ** (i + 1) * 10 ** (i + 1)
    x = ans

print(x)
