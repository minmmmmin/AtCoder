s = input()
n = len(s)
ans = -1
for i in range(n - 1, -1, -1):
    if s[i] == "a":
        ans = i + 1
        break

print(ans)
