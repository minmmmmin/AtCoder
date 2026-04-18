n, k = map(int, input().split())
s = input()

d = {}
for i in range(n - k + 1):
    t = s[i : i + k]
    if t in d:
        d[t] += 1
    else:
        d[t] = 1

x = 0
for v in d.values():
    if v > x:
        x = v

ans = []
for i in d:
    if d[i] == x:
        ans.append(i)

ans.sort()

print(x)
print(" ".join(ans))
