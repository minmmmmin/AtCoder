n = int(input())
a = list(map(int, input().split()))

A = set()

for i in range(n):
    A.add(a[i])

A = sorted(A, reverse=True)

print(A[1])
