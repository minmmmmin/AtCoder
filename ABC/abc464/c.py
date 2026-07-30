# piyo
N, M = map(int, input().split())

events = [[] for _ in range(M + 1)]
cnt = [0] * (N + 1)

for _ in range(N):
    A, D, B = map(int, input().split())

    cnt[A] += 1

    events[D].append((A, B))

kind = 0
for c in range(1, N + 1):
    if cnt[c] > 0:
        kind += 1

for day in range(1, M + 1):
    for A, B in events[day]:
        if A == B:
            continue

        cnt[A] -= 1
        if cnt[A] == 0:
            kind -= 1

        if cnt[B] == 0:
            kind += 1
        cnt[B] += 1

    print(kind)
