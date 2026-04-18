N, D = map(int, input().split())

t = []
l = []

for _ in range(N):
    T, L = map(int, input().split())
    t.append(T)
    l.append(L)

for k in range(1, D + 1):
    ans = 0
    for i in range(N):
        w = t[i] * (l[i] + k)
        ans = max(ans, w)
    print(ans)
