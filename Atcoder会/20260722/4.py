n, m = map(int, input().split())

ans = [-1] * n

for _ in range(m):
    s, c = map(int, input().split())
    s -= 1

    # すでに別の数字が指定されてる
    if ans[s] != -1 and ans[s] != c:
        print(-1)
        exit()

    ans[s] = c

# 2桁以上なのに先頭が0
if n >= 2 and ans[0] == 0:
    print(-1)
    exit()

# きまってないとこはminにする
for i in range(n):
    if ans[i] == -1:
        if i == 0 and n >= 2:
            ans[i] = 1
        else:
            ans[i] = 0

print("".join(map(str, ans)))
