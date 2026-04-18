# C問題解けなくてキレそう無理
def dfs(graph, current, end, visited, xor_sum):
    # 現在の頂点が終点に到達した場合
    if current == end:
        return xor_sum

    # 最小のXOR値を保持する変数、めっちゃ小さい。
    min_xor = float("inf")

    for next_node, weight in graph[current]:
        if not visited[next_node]:
            visited[next_node] = True
            min_xor = min(
                min_xor, dfs(graph, next_node, end, visited, xor_sum ^ weight)
            )
            visited[next_node] = False

    return min_xor


n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# DFSってなんだよ無理
visited = [False] * (n + 1)
visited[1] = True

# 頂点1から頂点Nへの最小XOR値を探索
result = dfs(graph, 1, n, visited, 0)

print(result)
