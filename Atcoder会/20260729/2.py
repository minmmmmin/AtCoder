N = int(input())

P = []
for i in range(N):
    p = int(input())
    P.append(p)

P = sorted(P)

P[-1] /= 2

print(int(sum(P)))
