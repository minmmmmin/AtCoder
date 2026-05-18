# kがどこのA_iに入るのか考えれば良さそう
n, k = map(int, input().split())

a = []
lengths = []

for _ in range(n):
    row = list(map(int, input().split()))
    l = row[0]
    a.append(row[1:])
    lengths.append(l)

c = list(map(int, input().split()))

for i in range(n):
    block_len = lengths[i] * c[i]

    # kの場所を特定する
    if k > block_len:
        k -= block_len
    else:
        idx = (k - 1) % lengths[i]
        print(a[i][idx])
        break