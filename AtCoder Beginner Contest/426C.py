N, Q = map(int, input().split())

count = [1] * (N + 2)
parent = list(range(N + 2))

for _ in range(Q):
    X, Y = map(int, input().split())
    s = 0
    v = 1

    while parent[v] != v:
        parent[v] = parent[parent[v]]
        v = parent[v]

    while v <= X:
        s += count[v]
        count[v] = 0
        parent[v] = v + 1

        nv = v + 1
        while parent[nv] != nv:
            parent[nv] = parent[parent[nv]]
            nv = parent[nv]
        v = nv

    count[Y] += s
    print(s)
