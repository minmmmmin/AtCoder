from collections import deque

n, m = map(int, input().split())
# 隣接リスト
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))  # 無向にしてサイクルも考慮

# print(graph)

dist = [-1] * (n + 1)
dist[1] = 0

q = deque()
# print(q)
q.append(1)

basis = []

while q:
    u = q.popleft()
    for v, w in graph[u]:
        if dist[v] == -1:
            dist[v] = dist[u] ^ w
            q.append(v)
            # print(q)
        else:
            x = dist[u] ^ dist[v] ^ w

            for b in basis:
                x = min(x, x ^ b)
            if x != 0:
                basis.append(x)
                basis.sort(reverse=True)

res = dist[n]
if res == -1:
    print(-1)
else:
    for b in basis:
        res = min(res, res ^ b)
    print(res)
