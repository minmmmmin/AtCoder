# 私はえらいので理解しようと頑張った。とりあえずb^2は固定でaをこねこね動かして考えてみようかなとすれば行けたのかも。キレそう。

from math import isqrt

n = int(input())

ans = isqrt(n // 4) + isqrt(n // 2)

print(ans)
