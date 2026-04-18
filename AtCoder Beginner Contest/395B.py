N = int(input())

# いったん全部.で初期化してみる。
grid = [["."] * N for _ in range(N)]

for i in range(1, N + 1):
    j = N + 1 - i
    if i > j:
        continue

    if i % 2 == 1:
        color = "#"
    else:
        color = "."

    for r in range(i - 1, j):
        for c in range(i - 1, j):
            grid[r][c] = color

# gridの各行rowを"".join(row)で文字列にして出力する
for row in grid:
    print("".join(row))
