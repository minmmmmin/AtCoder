N = int(input())

A = [1]
for i in range(1, N + 1):
    total = 0
    for j in range(i):
        s = 0
        for d in str(A[j]):
            s += int(d)
        total += s
    A.append(total)

print(A[N])
