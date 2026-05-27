N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = 0
for i in range(N):
    if A[i] < B[i]:
        S += A[i]
    else:
        S += B[i]

for _ in range(Q):
    c, x, v = input().split()
    x = int(x) - 1
    v = int(v)

    if A[x] < B[x]:
        old = A[x]
    else:
        old = B[x]

    if c == "A":
        A[x] = v
    else:
        B[x] = v

    if A[x] < B[x]:
        new = A[x]
    else:
        new = B[x]

    S += new - old
    print(S)
