n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 1
limit = 10**k

for num in a:
    ans *= num
    if ans >= limit:
        ans = 1

print(ans)
