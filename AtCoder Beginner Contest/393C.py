N, M = map(int, input().split())

edges = []
self_loops = 0
edge_count = {}

# 自己ループと多重辺を消去すればいい？？
for i in range(M):
    u, v = map(int, input().split())
    if u == v:  # これは自己ループ
        self_loops += 1
    else:
        # 無向グラフの辺 (u, v) の出現回数をカウントする！！
        edge = tuple(sorted([u, v]))
        if edge not in edge_count:
            edge_count[edge] = 0
        edge_count[edge] += 1

redundant_edges = sum(count - 1 for count in edge_count.values())

print(self_loops + redundant_edges)
