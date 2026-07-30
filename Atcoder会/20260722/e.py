n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

sides = []
i = 0

while i < n - 1:
    if a[i] == a[i + 1]:
        sides.append(a[i])
        i += 2
    else:
        i += 1

    if len(sides) == 2:
        break

if len(sides) == 2:
    print(sides[0] * sides[1])
else:
    print(0)
