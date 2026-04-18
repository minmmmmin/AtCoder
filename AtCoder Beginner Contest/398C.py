# 先週使ったやつがたくさん出てきてにこにこ
from collections import Counter

N = int(input())
A = list(map(int, input().split()))

count = Counter(A)

unique_max = -1
for i in count:
    if count[i] == 1:
        unique_max = max(unique_max, i)

if unique_max == -1:
    print(-1)
    exit()

for i in range(N):
    if A[i] == unique_max:
        print(i + 1)
        break
