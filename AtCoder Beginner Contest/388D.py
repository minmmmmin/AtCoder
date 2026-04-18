from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            sy, sx = i, j
        if S[i][j] == "G":
            gy, gx = i, j

dist = [[[-1] * 4 for _ in range(W)] for _ in range(H)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

Q = deque()
for d in range(4):
    dist[sy][sx][d] = 0
    Q.append((sy, sx, d))

while Q:
    y, x, d = Q.popleft()
    for new_d, (dy, dx) in enumerate(directions):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if S[ny][nx] == "#":
            continue
        if dist[ny][nx][new_d] == -1:
            dist[ny][nx][new_d] = dist[y][x][d] + (1 if d != new_d else 0)
            Q.append((ny, nx, new_d))

min_distance = -1
for d in range(4):
    if dist[gy][gx][d] != -1:
        if min_distance == -1 or dist[gy][gx][d] < min_distance:
            min_distance = dist[gy][gx][d]

print(min_distance)