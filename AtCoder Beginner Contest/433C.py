S = input().strip()
N = len(S)

runs = []
cur = S[0]
cnt = 1

for i in range(1, N):
    if S[i] == cur:
        cnt += 1
    else:
        runs.append((int(cur), cnt))
        cur = S[i]
        cnt = 1
runs.append((int(cur), cnt))

ans = 0
for i in range(len(runs) - 1):
    d1, c1 = runs[i]
    d2, c2 = runs[i + 1]
    if d1 + 1 == d2:
        ans += min(c1, c2)

print(ans)
