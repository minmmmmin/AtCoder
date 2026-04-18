# 念のためまじない
import sys

input = sys.stdin.readline

n, q = map(int, input().split())

A = [i + 1 for i in range(n)]
offset = 0

for _ in range(q):
    query = input().split()
    t = int(query[0])

    if t == 1:
        p = int(query[1])
        x = int(query[2])
        real_index = (offset + p - 1) % n
        A[real_index] = x
    elif t == 2:
        p = int(query[1])
        real_index = (offset + p - 1) % n
        print(A[real_index])
    elif t == 3:
        k = int(query[1])
        offset = (offset + k) % n
