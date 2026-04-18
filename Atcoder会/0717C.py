r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]

p = []
for i in range(r):
    for j in range(c):
        if b[i][j] != "." and b[i][j] != "#":
            p.append((i, j))
            for k in range(r):
                for L in range(c):
                    if abs(i - k) + abs(j - L) <= int(b[i][j]) and b[k][L] == "#":
                        b[k][L] = "."
for i in range(len(p)):
    x, y = p[i]
    b[x][y] = "."

for i in range(r):
    print("".join(b[i]))
