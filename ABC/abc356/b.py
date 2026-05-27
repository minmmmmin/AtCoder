N, M = map(int, input().split())

A = list(map(int,input().split()))
X = [list(map(int,input().split())) for _ in range(N)]

for j in range(M):
  s = 0
  for i in range(N):
    s += X[i][j]
  if s < A[j]:
    print("No")
    exit()
print("Yes")
#これが二次元配列らしい。