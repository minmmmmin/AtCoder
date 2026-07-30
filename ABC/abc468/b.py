M, D = map(int, input().split())
S = input()

ans = 0

for x in range(M):
    watched = False

    for i in range(max(0, x - D), min(M, x + D + 1)):
        if S[i] == "G":
            watched = True
            break

    if not watched:
        ans += 1

print(ans)
