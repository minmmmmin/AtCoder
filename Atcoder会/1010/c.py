n, m, t = map(int, input().split())

a = list(map(int, input().split()))

# ボーナス部屋をまとめた
b = [0] * n

for i in range(m):
    x, y = map(int, input().split())
    x -= 2
    b[x] = y

for i in range(n - 1):
    t -= a[i]
    if t <= 0:
        print("No")
        exit()
    t += b[i]

print("Yes")
