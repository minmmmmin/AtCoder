t = int(input())
ans = []

for i in range(t):
    n = int(input())
    s = input().strip()

    m = 0
    c = 0
    total = s.count("1")

    for ch in s:
        if ch == "1":
            c += 1
            m = max(m, c)
        else:
            c = 0

    ans.append(str(total - m))

print("\n".join(ans))
