H, W = map(int, input().split())
C = [input() for _ in range(H)]

top = H
bottom = -1
left = W
right = -1

for i in range(H):
    for j in range(W):
        if C[i][j] == "#":
            top = min(top, i)
            bottom = max(bottom, i)
            left = min(left, j)
            right = max(right, j)

for i in range(top, bottom + 1):
    print(C[i][left : right + 1])
