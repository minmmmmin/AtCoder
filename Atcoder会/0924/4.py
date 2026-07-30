xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

ab2 = (xa - xb) ** 2 + (ya - yb) ** 2
bc2 = (xb - xc) ** 2 + (yb - yc) ** 2
ca2 = (xc - xa) ** 2 + (yc - ya) ** 2

sides = sorted([ab2, bc2, ca2])

if sides[0] + sides[1] == sides[2]:
    print("Yes")
else:
    print("No")
