s = input()
ans = ""
for i in reversed(s):
    if i == ".":
        break
    ans = i + ans
print(ans)
