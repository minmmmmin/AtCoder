import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    size = 1
    while size < (1 << N):
        new_A = []
        for i in range(0, len(A), size * 2):
            left = A[i : i + size]
            right = A[i + size : i + size * 2]
            if left + right <= right + left:
                new_A += left + right
            else:
                new_A += right + left
        A = new_A
        size *= 2
    print(*A)
