# なんだよこいつ
from collections import defaultdict

n, m = map(int, input().split())

# 材料まとめ
zairyou = defaultdict(list)
unavailable_count = []

for dish_index in range(m):
    data = list(map(int, input().split()))
    k = data[0]
    ingredients = data[1:]
    unavailable_count.append(k)
    for ing in ingredients:
        zairyou[ing].append(dish_index)

B = list(map(int, input().split()))

result = []
available_dishes = 0

visited = [False] * (n + 1)

# 順番に減らしていくよ
for b in B:
    visited[b] = True
    for dish in zairyou[b]:
        unavailable_count[dish] -= 1
        if unavailable_count[dish] == 0:
            available_dishes += 1
    result.append(available_dishes)


for r in result:
    print(r)
