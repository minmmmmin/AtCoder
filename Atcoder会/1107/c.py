n = int(input())
a = list(map(int, input().split()))
ans = 0

while 1:
    a.sort()
    a[-1] -= 1
    a[-2] -= 1
    ans += 1
    cnt = 0
    for i in a:
        if i <= 0:
            cnt += 1
    if cnt >= n - 1:
        break

print(ans)
