# わけわかんないよ
from collections import deque

H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]
A, B, C, D = map(int, input().split())

A -= 1
B -= 1
C -= 1
D -= 1

INF = float("inf")
dist = [[INF] * W for _ in range(H)]
dist[A][B] = 0

dq = deque()
dq.append((A, B))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while dq:
    x, y = dq.popleft()

    # 通常移動
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] == "." and dist[nx][ny] > dist[x][y]:
                dist[nx][ny] = dist[x][y]
                dq.appendleft((nx, ny))

    # 前蹴り
    for i in range(4):
        for step in range(1, 3):
            nx = x + dx[i] * step
            ny = y + dy[i] * step
            if 0 <= nx < H and 0 <= ny < W:
                if grid[nx][ny] == "#" and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    dq.append((nx, ny))  # 壁を壊したあと、壊した場所にも立てるとする

print(dist[C][D])
