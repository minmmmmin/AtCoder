a = int(input())
n = int(input())

total = 0
i = 1

while True:
    s = str(i)
    pal = int(s + s[-2::-1])
    if pal > n:
        break
    x = pal
    sA = ""
    while x > 0:
        sA = str(x % a) + sA
        x //= a
    if sA == sA[::-1]:
        total += pal

    pal = int(s + s[::-1])
    if pal <= n:
        x = pal
        sA = ""
        while x > 0:
            sA = str(x % a) + sA
            x //= a
        if sA == sA[::-1]:
            total += pal

    i += 1

print(total)
