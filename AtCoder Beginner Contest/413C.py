import sys

input = sys.stdin.readline

Q = int(input())

A = []
head = 0
res = []

for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        c = int(query[1])
        x = int(query[2])
        A.append([x, c])
    else:
        k = int(query[1])
        total = 0
        while k > 0:
            x, c = A[head]
            if c <= k:
                total += x * c
                head += 1
                k -= c
            else:
                total += x * k
                A[head][1] -= k
                k = 0
        res.append(total)

for r in res:
    print(r)
