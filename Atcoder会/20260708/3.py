# えこれゴリ押しじゃない？
N = int(input())

intervals = []

for _ in range(N):
    t, l, r = map(int, input().split())



    if t == 2:
        r -= 1
    elif t == 3:
        l += 1
    elif t == 4:
        l += 1
        r -= 1

    intervals.append((l, r))

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        li, ri = intervals[i]
        lj, rj = intervals[j]

        if max(li, lj) <= min(ri, rj):
            ans += 1

print(ans)
