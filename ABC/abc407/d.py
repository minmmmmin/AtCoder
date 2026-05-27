from collections import deque

H, W = map(int, input().split())
A = []
for _ in range(H):
    A.extend(map(int, input().split()))

pairs = []
for i in range(H):
    for j in range(W):
        if j + 1 < W:
            pairs.append((i * W + j, i * W + j + 1))
        if i + 1 < H:
            pairs.append((i * W + j, (i + 1) * W + j))

visited = set()
queue = deque()

full_xor = 0
for val in A:
    full_xor ^= val

queue.append((0, full_xor))
visited.add(0)

ans = full_xor

while queue:
    mask, xor_val = queue.popleft()
    if xor_val > ans:
        ans = xor_val
    for u, v in pairs:
        if (mask & (1 << u)) == 0 and (mask & (1 << v)) == 0:
            new_mask = mask | (1 << u) | (1 << v)
            if new_mask not in visited:
                visited.add(new_mask)
                new_xor_val = xor_val ^ A[u] ^ A[v]
                queue.append((new_mask, new_xor_val))

print(ans)
