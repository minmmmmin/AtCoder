import sys

input = sys.stdin.readline
N, M, L = map(int, input().split())
A = list(map(int, input().split()))

e = [(M - (a % M)) % M for a in A]
C0 = sum(e)

costs = []
for c in range(L):
    cnt = [0] * M
    s = c + 1
    while s <= N:
        cnt[e[s - 1]] += 1
        s += L
    m = sum(cnt)
    suff = [0] * (M + 1)
    for t in range(M - 1, -1, -1):
        suff[t] = suff[t + 1] + cnt[t]
    cost = [0] * M
    for d in range(M):
        cost[d] = m * d - M * suff[M - d]
    costs.append(cost)

INF = 10**18
dp = [INF] * M
dp[0] = 0
for cost in costs:
    new = [INF] * M
    for s in range(M):
        base = dp[s]
        if base == INF:
            continue
        for d in range(M):
            t = (s + d) % M
            v = base + cost[d]
            if v < new[t]:
                new[t] = v
    dp = new

ans = dp[0] + C0
if ans == 0:
    print("O")
else:
    print(ans)
