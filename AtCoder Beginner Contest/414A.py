n, l, r = map(int, input().split())
count = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x <= l and r <= y:
        count += 1

print(count)
