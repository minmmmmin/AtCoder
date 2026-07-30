n, q = map(int, input().split())

L, R = 1, 2

ans = 0

for i in range(q):
    h, t = input().split()
    t = int(t)

    if h == "L":
        go = (t - L) % n
        ng = (R - L) % n
        if ng < go:
            ans += n - go
        else:
            ans += go
        L = t

    if h == "R":
        go = (t - R) % n
        ng = (L - R) % n
        if ng < go:
            ans += n - go
        else:
            ans += go
        R = t

print(ans)
