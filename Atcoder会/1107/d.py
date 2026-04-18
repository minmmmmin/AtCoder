q = int(input())

ans = list()

for i in range(q):
    a, b = map(int, input().split())

    if a == 1:
        ans.append(b)

    if a == 2:
        print(ans[-(b)])
