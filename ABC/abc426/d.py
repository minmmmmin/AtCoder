import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()

    if all(c == "0" for c in S) or all(c == "1" for c in S):
        print(0)
        continue

    total_zeros = S.count("0")
    total_ones = N - total_zeros

    max0 = max(len(seg) for seg in S.split("1"))
    max1 = max(len(seg) for seg in S.split("0"))

    cost0 = total_ones + 2 * (total_zeros - max0)
    cost1 = total_zeros + 2 * (total_ones - max1)

    print(min(cost0, cost1))
