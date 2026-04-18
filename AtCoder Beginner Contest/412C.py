from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    n = int(input())
    s = list(map(int, input().split()))

    dominos = [(val, idx) for idx, val in enumerate(s)]

    queue = deque()
    visited = [False] * n
    dist = [float("inf")] * n

    queue.append((s[0], 0))
    visited[0] = True
    dist[0] = 1

    sorted_dominos = sorted(dominos, key=lambda x: x[0])

    ptr = 0

    while queue:
        curr_size, curr_idx = queue.popleft()

        while ptr < n and sorted_dominos[ptr][0] <= 2 * curr_size:
            next_size, next_idx = sorted_dominos[ptr]
            if not visited[next_idx]:
                visited[next_idx] = True
                dist[next_idx] = dist[curr_idx] + 1
                queue.append((next_size, next_idx))
            ptr += 1

    if dist[n - 1] == float("inf"):
        results.append(-1)
    else:
        results.append(dist[n - 1])

print("\n".join(map(str, results)))
