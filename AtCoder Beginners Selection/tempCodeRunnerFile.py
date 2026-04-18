import math

n = int(input())
x0, y0 = map(int, input().split())
xm, ym = map(int, input().split())

# とりあえず中心を求めてみよう
xc = (x0 + xm) / 2
yc = (y0 + ym) / 2

# 角度の計算atan2って何やねん…
rag = math.atan2(y0 - yc, x0 - xc) + 2 * math.pi / n

# ベクトルの計算
r = math.sqrt((x0 - xc) ** 2 + (y0 - yc) ** 2)

# 座標はsin,cosで
x1 = xc + r * math.cos(rag)
y1 = yc + r * math.sin(rag)

print(x1, y1)
