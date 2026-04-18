from collections import Counter

A = list(map(int, input().split()))

count = Counter(A)

for x in count:
    for y in count:
        if x != y and count[x] >= 3 and count[y] >= 2:
            print("Yes")
            exit()

print("No")
