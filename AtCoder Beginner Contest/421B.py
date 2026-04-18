X, Y = map(int, input().split())

a1 = X
a2 = Y

for i in range(3, 11):
    s = str(a1 + a2)[::-1]
    ai = int(s)
    a1, a2 = a2, ai
print(a2)
