n = int(input())
s = [input() for _ in range(n)]

login = False
ans = 0

for i in s:
    if i == "login":
        login = True
    elif i == "logout":
        login = False
    elif i == "private":
        if not login:
            ans += 1

print(ans)
