N, X = map(int, input().split())
A = list(map(int, input().split()))

seen = set()
seen.add(X)

while True:
    nxt = A[X - 1]
    if nxt not in seen:
        seen.add(nxt)
        X = nxt
    else:
        break

print(len(seen))
