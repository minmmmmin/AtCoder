# 脳筋ですかこれは
T = int(input())

for _ in range(T):
    Px, Py, Qx, Qy, Rx, Ry, Sx, Sy = map(int, input().split())

    a1 = 2 * (Qx - Px)
    b1 = 2 * (Qy - Py)
    c1 = Qx * Qx + Qy * Qy - Px * Px - Py * Py

    a2 = 2 * (Sx - Rx)
    b2 = 2 * (Sy - Ry)
    c2 = Sx * Sx + Sy * Sy - Rx * Rx - Ry * Ry

    cross = a1 * b2 - a2 * b1

    if cross != 0:
        print("Yes")
    else:
        if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
            print("Yes")
        else:
            print("No")
