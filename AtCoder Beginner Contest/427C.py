N, M = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split())))

ans = M
for i in range(1 << N):
    bad = 0
    for u, v in edges:
        if ((i >> (u - 1)) & 1) == ((i >> (v - 1)) & 1):
            bad += 1
    if bad < ans:
        ans = bad

print(ans)
