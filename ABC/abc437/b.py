h, w, n = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(h)]

Bs = []
while len(Bs) < n:
    Bs.extend(map(int, input().split()))
Bset = set(Bs[:n])

ans = 0
for row in A:
    cnt = 0
    for x in row:
        if x in Bset:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
