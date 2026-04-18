n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

for i in range(n):
    max_index = -1
    max_dis2 = -1
    for j in range(n):
        if i == j:
            continue
        dis2 = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        if dis2 > max_dis2:
            max_index = j + 1
            max_dis2 = dis2
    print(max_index)