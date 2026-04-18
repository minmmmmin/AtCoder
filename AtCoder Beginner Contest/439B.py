n = int(input())

seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    s = 0
    for ch in str(n):
        d = int(ch)
        s += d * d
    n = s

print("Yes" if n == 1 else "No")
