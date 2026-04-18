import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = []
    while len(A) < 2*N:
        A.extend(map(int, input().split()))

    stack = []
    closed_sum = 0
    for i in range(2*N):
        if stack and A[stack[-1]] <= A[i]:
            closed_sum += A[i]
            stack.pop()
        else:
            stack.append(i)

    print(sum(A) - closed_sum)
