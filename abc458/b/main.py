H, W = map(int, input().split())

for i in range(H):
    row = []
    for j in range(W):
        count = 0

        if i > 0:
            count += 1
        if i < H - 1:
            count += 1
        if j > 0:
            count += 1
        if j < W - 1:
            count += 1

        row.append(count)

    print(*row)
