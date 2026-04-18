n, q = map(int, input().split())

count = [1] * (n + 2)

parent = list(range(n + 2))


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


for _ in range(q):
    X, Y = map(int, input().split())
    s = 0

    v = find(1)
    while v <= X:
        s += count[v]
        count[v] = 0
        parent[v] = v + 1
        v = find(v + 1)

    count[Y] += s
    print(s)
