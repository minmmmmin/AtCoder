n = int(input())
a = list(map(int, input().split()))
m = 10**8

a = sorted(a, reverse=True)

r = n

cnt = 0
for i in range(n):
    r = max(r, i + 1)
    while r - 1 > i and a[r - 1] + a[i] >= 100000000:
        r -= 1
    cnt += n - r

print(sum(a) * (n - 1) - cnt*m)
