n = int(input())

S = [input() for _ in range(n)]

m = max(len(s) for s in S)

t = [["*"] * n for _ in range(m)]
for i in range(n):
    for j in range(len(S[i])):
        t[j][n - i - 1] = S[i][j]

for i in range(m):
    while t[i][-1] == "*":
        t[i].pop()
    print("".join(t[i]))
