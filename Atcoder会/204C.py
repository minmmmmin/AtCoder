# おまじない
import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

G = [[] for i in range(N)]
# G[i] は都市iから道路で直接繋がっている都市のリスト

for i in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)

print(G)
