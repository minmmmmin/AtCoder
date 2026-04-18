import sys
from collections import Counter

T = int(sys.stdin.readline() or 0)

for _ in range(T):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    if n <= 1:
        print("Yes")
        continue

    c = Counter(arr)

    if len(c) < n:
        if len(c) == 1:
            print("Yes")
            continue
        if len(c) == 2:
            k = list(c.keys())
            if k[0] + k[1] == 0 and abs(c[k[0]] - c[k[1]]) <= 1:
                print("Yes")
                continue
        print("No")
        continue

    arr = sorted(arr, key=abs)

    if n <= 2:
        print("Yes")
        continue

    ok = True
    for i in range(2, n):
        if arr[i] * arr[0] != arr[i - 1] * arr[1]:
            ok = False
            break

    print("Yes" if ok else "No")
