n = int(input())
a = set()
point = 0
ans = 0


for i in range(n):
    s, t = input().split()
    t = int(t)
    if s not in a:
        a.add(s)
        if point < t:
            point = t
            ans = i + 1

print(ans)
