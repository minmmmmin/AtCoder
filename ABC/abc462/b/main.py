n = int(input())

g = [[] for _ in range(n)]

for i in range(1, n + 1):
    a = list(map(int, input().split()))

    for x in a[1:]:
        g[x - 1].append(i)

for v in g:
    print(len(v), *v)
