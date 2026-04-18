n = int(input())
a = list(map(int, input().split()))

b = 0

for i in range(1, n):
    b ^= a[i]

ans = [b]

for i in range(n - 1):
    b ^= a[i]
    b ^= a[i + 1]
    ans.append(b)

print(*ans)
