s = input()
t = input()

ok = True
for i in range(1, len(s)):
    if s[i].isupper():
        if s[i - 1] not in t:
            ok = False
            break

print("Yes" if ok else "No")
