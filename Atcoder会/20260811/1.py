a, b, c, d = map(int, input().split())

ans = [a, b, c, d]

ans.sort()

if ans[3] == ans[0] + ans[1] + ans[2]:
    print("Yes")
elif ans[0] + ans[3] == ans[1] + ans[2]:
    print("Yes")
else:
    print("No")
