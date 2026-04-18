n = int(input())
a = list(map(int, input().split()))

visited = set()
path = []
current = 0  # 別にどこでもいい

# DFSとかBFSとか分かんねえよ
while current not in visited:
    visited.add(current)
    path.append(current)
    current = a[current] - 1  # パスにしたいので

    # print(path)
    # print(current)


# pathからcurrentが最初に出てきた位置を探して、そこから末尾までが閉路
start = path.index(current)
cycle = path[start:]

# print(cycle)

print(len(cycle))
print(*[x + 1 for x in cycle])  # さいごに+1すれば数はそろうか
