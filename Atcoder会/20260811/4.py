# 全探索なのでは
t = int(input())

target = "atcoder"

for _ in range(t):
    s = input()

    if s > target:
        print(0)
        continue

    ans = 10**9

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            tmp = list(s)
            c = tmp.pop(j)
            tmp.insert(i, c)
            tmp = "".join(tmp)

            if tmp > target:
                ans = min(ans, j - i)

    if ans == 10**9:
        print(-1)
    else:
        print(ans)
