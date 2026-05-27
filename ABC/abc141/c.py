N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

score = [K] * (N+1)

for i in range(Q):
    score[A[i]] += 1

for i in range(1, N+1):
    if score[i] > Q:
        print('Yes')
    else:
        print('No')