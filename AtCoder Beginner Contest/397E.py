from collections import defaultdict, deque

# 入力の受け取り
N, K = map(int, input().split())
graph = defaultdict(list)

# 辺の情報を受け取り、グラフを構築
for _ in range(N * K - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 次数が1の頂点を探す
leaf_nodes = [node for node, adj in graph.items() if len(adj) == 1]

# 次数が1の頂点が2 * N個でなければ分解できない
if len(leaf_nodes) != 2 * N:
    print("No")
    exit()

# パスの始点・終点を順に処理していく
visited = [False] * (N * K + 1)
paths = []

# 幅優先探索でパスを構成する
def bfs(start):
    path = []
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        path.append(node)
        if len(path) == K:
            break

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return path

# 各パスを構成
for leaf in leaf_nodes:
    if not visited[leaf]:
        path = bfs(leaf)
        if len(path) == K:
            paths.append(path)

# パスが N 本生成できた場合
if len(paths) == N:
    print("Yes")
else:
    print("No")
