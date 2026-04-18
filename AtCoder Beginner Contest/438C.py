n = int(input())
a = list(map(int, input().split()))

# 消した後の連結を考える

stack = []

for x in a:
    if stack and stack[-1][0] == x:
        val, cnt = stack.pop()
        cnt += 1
        if cnt < 4:
            stack.append((val, cnt))
    else:
        stack.append((x, 1))

ans = sum(cnt for _, cnt in stack)
print(ans)
