n = int(input())
a = []
b = []
for i in range(n):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

suma = sum(a)

ans = 0
for i in range(n):
    ans = max(ans, suma - a[i] + b[i])

print(ans)
