from typing import List
import sys
sys.setrecursionlimit(2*10**5)

n = int(input())
C = list(map(int, input().split()))
adj: List[List[int]] = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

visit = [False]*(n+1)
color = [False]*(10**5+100)  # 頂点1からの最短パスにある色があるならTrue
ans: List[int] = []


def dfs(v: int) -> None:

    origin_state: bool = visit[v]
    origin_color: bool = color[C[v]]
    if color[C[v]] == False:
        ans.append(v+1)  # 1-index に戻して入れる
    visit[v] = True
    color[C[v]] = True
    # 子の頂点に行く時はvisit の状態はすでに訪れたようにしておく
    for next_v in adj[v]:
        # 親ノードがきたら飛ばす
        if visit[next_v]:
            continue
        dfs(next_v)
    visit[v] = origin_state  # 次の頂点に行く時は元に戻す
    color[C[v]] = origin_color


dfs(0)
ans.sort()
for i in ans:
    print(i)
