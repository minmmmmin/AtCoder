x, y, z = map(int, input().split())

if z == 1:
    print("Yes" if x == y else "No")
else:
    num = x - z * y
    den = z - 1
    if num % den == 0 and num // den >= 0:
        print("Yes")
    else:
        print("No")
