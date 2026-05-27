t = int(input())
out = []

# すべてのパワー >= 乗ってるトナカイの重さとパワーになればいい

for _ in range(t):
    n = int(input())
    costs = []
    total_p = 0

    for _ in range(n):
        w, p = map(int, input().split())
        total_p += p
        costs.append(w + p)

    costs.sort()

    s = 0
    k = 0
    for c in costs:
        if s + c > total_p:
            break
        s += c
        k += 1

    out.append(str(k))

print("\n".join(out))
