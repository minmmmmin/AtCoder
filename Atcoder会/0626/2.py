s = list(input())
ans = True

if s[0] != "<":
    ans = False

if s[-1] != ">":
    ans = False

for i in range(1, len(s) - 1):
    if s[i] != "=":
        ans = False
print("Yes" if ans else "No")
