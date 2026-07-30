t = int(input())

for i in range(t):
    n = int(input())
    test = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if test[i] % 2 == 1:
            ans += 1

    print(ans)
