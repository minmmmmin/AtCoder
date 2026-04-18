N, M = map(int, input().split())
S = input().strip()
T = input().strip()

ans = float("inf")

for i in range(N - M + 1):
    cost = 0
    for j in range(M):
        a = int(T[j])
        b = int(S[i + j])
        cost += (b - a + 10) % 10
    ans = min(ans, cost)

print(ans)
