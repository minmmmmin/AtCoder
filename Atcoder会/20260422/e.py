N,M = map(int, input().split())
X = list(map(int, input().split()))

# それはそう
if N >= M:
    print(0)
    exit()

X.sort()
# print(X)
diffX = [abs(b - a) for a, b in zip(X, X[1:])]
diffX.sort(reverse=True)
# print(diffX)

answer = sum(diffX[N-1:])
print(answer)