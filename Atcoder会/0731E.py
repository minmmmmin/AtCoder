n, m = map(int, input().split())

s = [list(input()) for i in range(n)]

ans = float("inf")

# 行くか行かないかの二択だよねって話
for i in range(2**n):
    pop = [0] * m
    stores = []

    # bit全探索ってやつ学ぼう
    # どのお店を選ぶか
    for j in range(n):
        if i >> j & 1:
            stores.append(1)
        else:
            stores.append(0)

    # お店ごとのポップコーンの在庫
    for k in range(n):
        if stores[k] == 1:
            for l in range(m):
                if s[k][l] == "o":
                    pop[l] = 1

    if sum(pop) == m:
        ans = min(ans, sum(stores))

print(ans)
