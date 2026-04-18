import sys

sys.setrecursionlimit(2 * 10**5 + 50)

n, m = map(int, input().split())

parent = list(range(n))
size = [1] * n
edge_count = [0] * n


# Union Findってのがあるらしい
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    x = a
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    root_a = x

    x = b
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    root_b = x

    if root_a == root_b:
        edge_count[root_a] += 1
    else:
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        size[root_a] += size[root_b]
        edge_count[root_a] += edge_count[root_b] + 1

seen = [False] * n
ans = 0

for i in range(n):
    x = i
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    root = x

    if not seen[root]:
        seen[root] = True
        ans += edge_count[root] - (size[root] - 1)

print(ans)
