H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            cnt = 0
            for d in dirs:
                di = d[0]
                dj = d[1]
                ni = i + di
                nj = j + dj
                if 0 <= ni < H and 0 <= nj < W:
                    if grid[ni][nj] == "#":
                        cnt += 1
            if cnt not in (2, 4):
                print("No")
                exit()

print("Yes")
