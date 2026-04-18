N, K = map(int, input().split())

length = 2 ** N

q = K // length
amari = K % length

B = [q] * length

for i in range(amari):
    pos = (i * length) // amari
    B[pos] += 1

printB = B[:]

X = 0
for _ in range(N):
    X = max(X, max(B) - min(B))
    B = [B[i] + B[i + 1] for i in range(0, len(B), 2)]

print(X)
print(*printB)
