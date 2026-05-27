MOD = 10**9

n, k = map(int, input().split())

A = [1] * (k if n + 1 > k else n + 1)
total = sum(A) % MOD

for i in range(k, n + 1):
    A.append(total)
    total = (total + A[-1] - A[i - k]) % MOD

print(A[n])
