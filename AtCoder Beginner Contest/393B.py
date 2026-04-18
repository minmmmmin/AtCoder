S = input().strip()
ans = 0
n = len(S)

for i in range(n):
    if S[i] == "A":
        for j in range(i + 1, n):
            if S[j] == "B":
                diff = j - i
                k = j + diff
                if k < n and S[k] == "C":
                    ans += 1

print(ans)
