n = int(input())
h = list(map(int, input().split()))

ans = 1
for step in range(1, n):
    for start in range(n):
        cur = -1
        cnt = 0
        for k in range(start, n, step):
            if h[k] != cur:
                cur = h[k]
                cnt = 1
            else:
                cnt += 1
            ans = max(ans, cnt)

print(ans)