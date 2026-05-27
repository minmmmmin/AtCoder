S = input()

ans = len(S)

i = 0
while i < len(S) - 1:
    if S[i] == '0' and S[i + 1] == '0':
        ans -= 1
        i += 2
    else:
        i += 1

print(ans)
