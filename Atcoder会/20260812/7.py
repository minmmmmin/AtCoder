# これはですねグラフの問題です
N, M = map(int, input().split())

G = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)

# 各頂点からDFS
ans = 0

for start in range(N):
    visited = [False] * N
    stack = [start]
    visited[start] = True

    while stack:
        v = stack.pop()

        for nv in G[v]:
            if not visited[nv]:
                visited[nv] = True
                stack.append(nv)

    ans += sum(visited)

print(ans)
