N = int(input())

a = set()

for i in range(N):
    n = int(input())
    if n in a:
        a.discard(n)
    else:
        a.add(n)

print(len(a))