import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
M = max(A)
TOT = sum(A)

freq = [0] * (M + 1)
for a in A:
    freq[a] += 1

C = [0] * (M + 1)
P = [0] * (M + 1)
run_c = 0
run_p = 0

for k in range(1, M + 1):
    run_c += freq[k]
    run_p += freq[k] * k
    C[k] = run_c
    P[k] = run_p

out = []

for _ in range(Q):
    b = int(input())
    t = b - 1
    if t >= M:
        out.append("-1")
        continue

    Sb = P[t] + t * (N - C[t])

    if Sb >= TOT:
        out.append("-1")
    else:
        x = Sb + 1
        out.append(str(x))

print("\n".join(out))
