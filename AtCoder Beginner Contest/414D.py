import sys

sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

if m >= n:
    print(0)
    exit()

distances = []
for i in range(1, n):
    distances.append(x[i] - x[i - 1])

distances.sort(reverse=True)

total_span = x[-1] - x[0]
sum_of_cut_gaps = sum(distances[: m - 1])

result = total_span - sum_of_cut_gaps

print(result)
