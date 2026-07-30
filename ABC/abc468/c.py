from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

ans = 0

for A in permutations(range(1, N + 1)):
    if P < A < Q:
        ans += 1

print(ans)
