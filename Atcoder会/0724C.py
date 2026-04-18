n = int(input())
S = input()

D = [(1, 0), (0, -1), (-1, 0), (0, 1)]
d = 0

x, y = 0, 0

for s in S:
    if s == "S":
        di, dj = D[d]
        x, y = x + di, y + dj

    if s == "R":
        d = (d + 1) % 4
print(x, y)
