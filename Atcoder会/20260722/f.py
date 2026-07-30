n = int(input())
towns = []

aoki = 0

for _ in range(n):
    a, b = map(int, input().split())

    aoki += a
    towns.append(2 * a + b)

towns.sort(reverse=True)

diff = 0

for i, effect in enumerate(towns):
    diff += effect

    if diff > aoki:
        print(i + 1)
        break
