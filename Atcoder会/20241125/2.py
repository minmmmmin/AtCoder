n = int(input())
t = list(map(int,input().split()))

a = sorted(t)

ans = 0

for i in range(n, 4*n):
  ans += a[i]
  
print(ans/(3*n))