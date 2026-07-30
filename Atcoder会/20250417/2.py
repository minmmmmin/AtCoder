n = int(input())
ans = 0
for i in range(1, n + 1):
    j = str(i)
    if len(j) % 2 == 1:
        ans += 1
print(ans)
