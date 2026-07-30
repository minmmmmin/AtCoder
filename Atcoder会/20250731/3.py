N, M = map(int, input().split())

X = 0

for i in range(M + 1):
    term = pow(N, i)
    X += term
    if X > 10**9:
        print("inf")
        break
else:
    print(X)
