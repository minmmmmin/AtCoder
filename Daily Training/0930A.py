n, m = map(int, input().split())

S = [list(input()) for a in range(n)]

ans = float('inf')

for i in range(2**n):
    popcorns = [0] * m
    stores = []

    for j in range(n):
        if i >> j & 1:
            stores.append(1)
        else:
            stores.append(0)

    for k in range(n):
        if stores[k] == 1:
            for l in range(m):
                if S[k][l] == 'o':
                    popcorns[l] = 1

    if sum(popcorns) == m:
        ans = min(ans, sum(stores))

print(ans)