from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            sx, sy = i, j
        if grid[i][j] == "G":
            gx, gy = i, j

INF = 10**9
dist = [[[INF] * 2 for _ in range(W)] for _ in range(H)]
dist[sx][sy][0] = 0
q = deque([(sx, sy, 0)])

while q:
    x, y, p = q.popleft()
    d = dist[x][y][p]
    if (x, y) == (gx, gy):
        print(d)
        exit()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        cell = grid[nx][ny]
        np = p
        if cell == "#":
            continue
        if cell == "o" and p == 1:
            continue
        if cell == "x" and p == 0:
            continue
        if cell == "?":
            np = 1 - p
        if dist[nx][ny][np] > d + 1:
            dist[nx][ny][np] = d + 1
            q.append((nx, ny, np))

print(-1)
