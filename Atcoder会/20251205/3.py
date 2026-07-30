s = input()

ans = []
for i in range(len(s)):
    if s[i] == "#":
        ans.append(i + 1)

for i in range(0, len(ans), 2):
    print(f"{ans[i]},{ans[i + 1]}")
