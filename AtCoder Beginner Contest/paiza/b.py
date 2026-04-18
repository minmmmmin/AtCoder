n, h, w = map(int, input().split())

sy, sx = map(int, input().split())
sy -= 1
sx -= 1

s = input()
grid = [list(map(int, input().split())) for _ in range(h)]

move = {
    "R": (0, 1),
    "L": (0, -1),
    "F": (-1, 0),
    "B": (1, 0),
}

for c in s:
    dy, dx = move[c]
    sy += dy
    sx += dx
    print(grid[sy][sx])
