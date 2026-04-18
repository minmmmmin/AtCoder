N = int(input())
# ここにプログラムを追記

A = list(map(int, input().split()))

total = 0

for i in range(N):
    total += A[i]

mean = total // N

for i in range(N):
    print(abs(A[i] - mean))