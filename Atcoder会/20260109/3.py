q = int(input())
A = []
for i in range(q):
    a, x = map(int, input().split())

    if a == 1:
        A.append(x)
    else:
        print(A[-x])
