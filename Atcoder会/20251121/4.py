from math import sin, cos, radians

a, b, d = map(int, input().split())
d = radians(d)
print(a * cos(d) - b * sin(d), a * sin(d) + b * cos(d))
