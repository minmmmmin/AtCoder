n = int(input())
a = list(map(int, input().split()))

q = int(input())
for _ in range(q):
    parts = input().split()
    if parts[0] == "1":
        k = int(parts[1]) - 1
        x = int(parts[2])
        a[k] = x
    else:
        k = int(parts[1]) - 1
        print(a[k])
