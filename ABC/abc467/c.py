N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = N

# 最初を奇数にするか偶数にするか
for first in [0, 1]:
    current = first
    operations = 0

    if current != A[0]:
        operations += 1

    for i in range(N - 1):
        current = current ^ B[i]

        if current != A[i + 1]:
            operations += 1

    answer = min(answer, operations)

print(answer)
