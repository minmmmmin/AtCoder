from collections import deque

n, m = map(int, input().split())
h = [input().split() for _ in range(m)]

# print(h)

dist = [[0] * n for _ in range(m)]
visit = [[False] * n for _ in range(m)]
queue = deque()

sx = 0
sy = 0
gx = 0
gy = 0

# スタートとゴールを見つける
for y in range(m):
    for x in range(n):
        if h[y][x] == "s":
            sx, sy = x, y
        if h[y][x] == "g":
            gx, gy = x, y

# print(sx, sy)

queue.append([sx, sy])
visit[sy][sx] = True

# print(queue)

while len(queue) != 0:
    node = queue.popleft()
    x, y = node[0], node[1]

    # 下 (y+1)
    if y + 1 < m and h[y + 1][x] != "1" and not visit[y + 1][x]:
        queue.append([x, y + 1])
        dist[y + 1][x] = dist[y][x] + 1
        visit[y + 1][x] = True

    # 右 (x+1)
    if x + 1 < n and h[y][x + 1] != "1" and not visit[y][x + 1]:
        queue.append([x + 1, y])
        dist[y][x + 1] = dist[y][x] + 1
        visit[y][x + 1] = True

    # 上 (y-1)
    if y - 1 >= 0 and h[y - 1][x] != "1" and not visit[y - 1][x]:
        queue.append([x, y - 1])
        dist[y - 1][x] = dist[y][x] + 1
        visit[y - 1][x] = True

    # 左 (x-1)
    if x - 1 >= 0 and h[y][x - 1] != "1" and not visit[y][x - 1]:
        queue.append([x - 1, y])
        dist[y][x - 1] = dist[y][x] + 1
        visit[y][x - 1] = True

# print(dist)

if visit[gy][gx]:
    print(dist[gy][gx])
else:
    print("Fail")
