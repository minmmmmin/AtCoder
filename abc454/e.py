import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    N, A, B = map(int, input().split())

    if N % 2 == 1 or (A + B) % 2 == 0:
        out.append("No")
        continue

    votqi = []

    r = A if A % 2 == 1 else A - 1

    for i in range(1, r, 2):
        votqi.append("R" * (N - 1))
        votqi.append("D")
        votqi.append("L" * (N - 1))
        votqi.append("D")

    if A == r:
        k = B
        votqi.append("DRUR" * (k // 2 - 1))
        if k == N:
            votqi.append("DR")
        else:
            votqi.append("DRR")
            votqi.append("URDR" * ((N - k) // 2 - 1))
            votqi.append("URD")
    else:
        k = B
        votqi.append("DRUR" * ((k - 1) // 2))
        if k == N - 1:
            votqi.append("RD")
        else:
            votqi.append("R")
            votqi.append("DRUR" * ((N - k - 1) // 2 - 1))
            votqi.append("DRURD")

    for i in range(r + 2, N, 2):
        votqi.append("D")
        votqi.append("L" * (N - 1))
        votqi.append("D")
        votqi.append("R" * (N - 1))

    out.append("Yes")
    out.append("".join(votqi))

print("\n".join(out))