n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# Cの合計を基準にして考えていく

Apre = [0] * (n + 1)
Bpre = [0] * (n + 1)
Cpre = [0] * (n + 1)

for i in range(n):
    Apre[i + 1] = Apre[i] + A[i]
    Bpre[i + 1] = Bpre[i] + B[i]
    Cpre[i + 1] = Cpre[i] + C[i]

C_total = Cpre[n]

# めっちゃ小さい数
best = -(10**30)
ans = -(10**30)

for y in range(2, n):
    x = y - 1
    best = max(best, Apre[x] - Bpre[x])

    value = best + (Bpre[y] - Cpre[y])
    ans = max(ans, value)

print(ans + C_total)
