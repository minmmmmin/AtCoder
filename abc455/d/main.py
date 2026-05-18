import sys
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())

parent = [0] * (N + 1)

for _ in range(Q):
    C, P = map(int, input().split())
    parent[C] = P

def find(x):
    if parent[x] == 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

ans = [0] * (N + 1)

for i in range(1, N + 1):
    root = find(i)
    ans[root] += 1

print(*ans[1:])