n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

seen = [False] * (n+1)
stack = [1]
seen[1] = True

while stack:
    x = stack.pop()
    for y in graph[x]:
        if not seen[y]:
            seen[y] = True
            stack.append(y)
print(sum(seen))