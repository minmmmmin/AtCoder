from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [input().strip() for _ in range(R)]

# 距離
dist = [[0] * C for _ in range(R)]

# 訪れたかどうか
visit = [[False] * C for _ in range(R)]
queue = deque()

sx -= 1
sy -= 1

queue.append([sx, sy])
visit[sy][sx] = True

# print(queue)

# 4方向を配列で回すと短く書ける
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while queue:
    y, x = queue.popleft()
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and c[ny][nx] != "#" and not visit[ny][nx]:
            visit[ny][nx] = True
            dist[ny][nx] = dist[y][x] + 1
            queue.append((ny, nx))

    # print(queue)

# print(dist)

print(dist[gy - 1][gx - 1])
