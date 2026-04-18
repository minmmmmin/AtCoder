from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

T = [row[:] for row in S]

dirs = [(-1, 0, "v"), (1, 0, "^"), (0, -1, ">"), (0, 1, "<")]
queue = deque()

visited = [[False] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "E":
            queue.append((i, j))
            visited[i][j] = True

while queue:
    x, y = queue.popleft()
    for dx, dy, arrow in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W:
            if not visited[nx][ny] and S[nx][ny] == ".":
                visited[nx][ny] = True
                T[nx][ny] = arrow
                queue.append((nx, ny))

for row in T:
    print("".join(row))
