n = int(input())
a = list(map(int, input().split()))

mn = float("inf")
for bit in range(1 << (n - 1)):
    parent = []
    children = [a[0]]
    for i in range(1, n):
        if bit & (1 << (i - 1)):
            parent.append(children)
            children = [a[i]]
        else:
            children.append(a[i])
    parent.append(children)

    ors = []
    for group in parent:
        base = 0
        for num in group:
            base |= num
        ors.append(base)

    base = 0
    for e in ors:
        base ^= e

    mn = min(mn, base)

print(mn)
