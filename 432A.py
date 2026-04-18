a, b, c = map(int, input().split())

ans = []

ans.append(a)
ans.append(b)
ans.append(c)

ans = sorted(ans, reverse=True)

for i in ans:
    print(i, end="")
