from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

boxes = defaultdict(list)
for i in range(N):
  boxes[A[i]].append(W[i])

ans = 0
for i in boxes.keys():
  boxes[i].sort()
  if len(boxes[i]) >= 2:
    ans += sum(boxes[i]) - boxes[i][-1]

print(ans)