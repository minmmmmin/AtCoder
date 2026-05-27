# おなじまい
import sys

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
# それはそう
if m != n:
    print("No")
    exit()

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# for i in range(n):
#     print(f"{i + 1}: {graph[i]}")


for i in range(n):
    if len(graph[i]) != 2:
        print("No")
        exit()

visited = [False] * n


def dfs(v):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u)


dfs(0)

if all(visited):
    print("Yes")
else:
    print("No")
