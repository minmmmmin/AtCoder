n = int(input())
ans = []
for i in range(n):
    sub = []
    for j in range(i + 1):
        if j == 0 or j == i:
            sub.append(1)
        else:
            sub.append(ans[-1][j - 1] + ans[-1][j])
    ans.append(sub)

for i in ans:
    print(i)
