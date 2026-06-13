N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

i = 0
ans = 0

for b in B:
    while i < N and A[i] * 2 < b:
        i += 1

    if i < N:
        ans += 1
        i += 1

print(ans)
