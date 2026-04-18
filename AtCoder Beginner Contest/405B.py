n, m = map(int, input().split())
a = list(map(int, input().split()))

target = set(range(1, m + 1))

for remove in range(n + 1):
    sub = a[: n - remove]
    if set(sub) != target:
        print(remove)
        break
