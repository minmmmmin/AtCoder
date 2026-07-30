# めも
n, k = map(int, input().split())
A = list(map(int, input().split()))

KA = [[] for i in range(k)]

for i in range(n):
  KA[i%k].append(A[i])

for ka in KA:
  ka.sort()

B = []
for i in range(n):
  B.append(KA[i%k][i//k])
  

# print(B)
ans = True
for i in range(1,n):
  if B[i-1] > B[i]:
    ans = False
print("Yes" if ans else "No")
