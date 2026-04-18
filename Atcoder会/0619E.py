N, M = map(int, input().split())

food_cnt = []
used = [[] for _ in range(N + 1)]
for i in range(M):
    K, *A = map(int, input().split())
    A = list(A)
    food_cnt.append(K)
    for j in A:
        used[j].append(i)

B = list(map(int, input().split()))

ans = 0
for i in B:
    for j in used[i]:
        food_cnt[j] -= 1
        if food_cnt[j] == 0:
            ans += 1
    print(ans)
