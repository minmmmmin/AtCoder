import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

L = [0] * N
R = [0] * N

# 左側境界
stack = []
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        stack.pop()
    L[i] = stack[-1] if stack else -1
    stack.append(i)

# 右側境界
stack = []
for i in reversed(range(N)):
    while stack and A[stack[-1]] <= A[i]:
        stack.pop()
    R[i] = stack[-1] if stack else N
    stack.append(i)

res = [0] * (N + 1)

for i in range(N):
    length = R[i] - L[i] - 1  # この長さの区間に最大値として貢献
    res[length] += A[i]

# res[k] は長さ k の区間に対する「最大値候補の和」なので、
# これより短い区間にも含まれるので下から累積していく
for i in range(N - 1, 0, -1):
    res[i] += res[i + 1]

for i in range(1, N + 1):
    print(res[i])
