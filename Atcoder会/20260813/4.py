from bisect import bisect_right

N = int(input())

H = []
L = []

for _ in range(N):
    h, l = map(int, input().split())
    H.append(h)
    L.append(l)

# i番目以降の身長の最大値
mx = [0] * N
mx[N - 1] = H[N - 1]

for i in range(N - 2, -1, -1):
    mx[i] = max(H[i], mx[i + 1])

Q = int(input())
T = list(map(int, input().split()))

for t in T:
    i = bisect_right(L, t)
    print(mx[i])
