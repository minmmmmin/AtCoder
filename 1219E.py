s = input().strip()

# W*K+A => A*K+Cになるのを使いたい
out = []
for ch in s:
    if ch == "A":
        k = 0
        while out and out[-1] == "W":
            out.pop()
            k += 1
        out.append("A")
        out.extend("C" * k)
    else:
        out.append(ch)

print("".join(out))
