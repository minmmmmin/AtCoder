# ヒープを使ってみる
import heapq

X = int(input())
Q = int(input())

# 中央値以下の値を入れる（最大ヒープにしたいのでマイナスで入れる）
left = []
# 中央値より大きい値を入れる（最小ヒープ）
right = []

heapq.heappush(left, -X)

for _ in range(Q):
    A, B = map(int, input().split())

    for v in [A, B]:
        if v <= -left[0]:
            heapq.heappush(left, -v)
        else:
            heapq.heappush(right, v)

    # left の個数が right よりちょうど1個多くなるように調整
    while len(left) < len(right) + 1:
        x = heapq.heappop(right)
        heapq.heappush(left, -x)

    while len(left) > len(right) + 1:
        x = -heapq.heappop(left)
        heapq.heappush(right, x)
    # 中央値はleftの最大値
    print(-left[0])
