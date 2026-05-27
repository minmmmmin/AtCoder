n = int(input())
s = [input() for _ in range(n)]

is_logged_in = False
ans = 0

for i in s:
    if i == "login":
        is_logged_in = True
    elif i == "logout":
        is_logged_in = False
    elif i == "private":
        if not is_logged_in:
            ans += 1

print(ans)
