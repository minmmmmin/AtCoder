n = int(input())

ans = 0
pi = []
for _ in range(n):
    pi.append(int(input()))

max_p = max(pi)

t = True
for i in range(n):
    if max_p == pi[i] and t:
        ans += pi[i]//2
        t = False
    else:
        ans += pi[i]

print(ans)