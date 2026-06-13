T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2

    min_r = abs(r1 - r2)
    max_r = r1 + r2

    if min_r**2 <= d2 <= max_r**2:
        print("Yes")
    else:
        print("No")
