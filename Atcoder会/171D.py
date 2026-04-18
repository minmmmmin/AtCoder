# おなじまいたち
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = 2**63 - 1
LIMIT = 10**5 + 7

A_NUM = [0] * LIMIT

N = int(input())
A = list(map(int, input().split()))

A_SUM = 0
for a in A:
    A_NUM[a] += 1
    A_SUM += a

Q = int(input())
for i in range(Q):
    B, C = map(int, input().split())
    A_SUM += (C - B) * A_NUM[B]
    A_NUM[C] += A_NUM[B]
    A_NUM[B] = 0
    print(A_SUM)
