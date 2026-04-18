h, w, x, y = map(int, input().split())
S = []
for i in range(h):
    s = list(input())
    S.append(s)

r = x - 1
c = y - 1
ans = 1
i = r - 1
while i >= 0 and S[i][c] == ".":
    ans += 1
    i -= 1
i = r + 1
while i < h and S[i][c] == ".":
    ans += 1
    i += 1
j = c - 1
while j >= 0 and S[r][j] == ".":
    ans += 1
    j -= 1
j = c + 1
while j < w and S[r][j] == ".":
    ans += 1
    j += 1

print(ans)
