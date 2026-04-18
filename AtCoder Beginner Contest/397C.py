# カウンターをつかってみる
from collections import Counter

n = int(input())
A = list(map(int, input().split()))

left_set = set()
right_counter = Counter(A)

max_value = 0

for i in range(n - 1):
    left_set.add(A[i])

    right_counter[A[i]] -= 1
    if right_counter[A[i]] == 0:
        del right_counter[A[i]]

    max_value = max(max_value, len(left_set) + len(right_counter))

print(max_value)
