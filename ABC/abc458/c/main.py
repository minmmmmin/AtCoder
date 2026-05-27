S = input()
n = len(S)

ans = 0

for i in range(n):
    if S[i] == "C":
        ans += min(i + 1, n - i)
print(ans)
