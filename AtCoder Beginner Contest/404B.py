n = int(input())
S = [input() for _ in range(n)]
T = [input() for _ in range(n)]

ans = float("inf")

for rot in range(4):
    diff = 0
    for i in range(n):
        for j in range(n):
            if S[i][j] != T[i][j]:
                diff += 1
    total_ops = rot + diff
    if total_ops < ans:
        ans = total_ops

    new_S = []
    for i in range(n):
        row = ""
        for j in range(n):
            row += S[n - j - 1][i]
        new_S.append(row)
    S = new_S

print(ans)
