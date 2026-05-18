n = int(input())

a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row[1:])

x, y = map(int, input().split())

# print(a)

print(a[x - 1][y - 1])