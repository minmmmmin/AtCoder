from collections import Counter

N = int(input())
A = list(map(int, input().split()))
A_dict = Counter(A)
colors = [0] * 8
extra = 0

for key in A_dict.keys():
    if key in range(1, 400):
        colors[0] = 1
    elif key in range(400, 800):
        colors[1] = 1
    elif key in range(800, 1200):
        colors[2] = 1
    elif key in range(1200, 1600):
        colors[3] = 1
    elif key in range(1600, 2000):
        colors[4] = 1
    elif key in range(2000, 2400):
        colors[5] = 1
    elif key in range(2400, 2800):
        colors[6] = 1
    elif key in range(2800, 3200):
        colors[7] = 1
    else:
        extra += A_dict[key]
        # print(A_dict[key])

min_color = sum(colors)
max_color = min_color + extra

if sum(colors) == 0 and extra > 0:
    min_color = 1

print(min_color, max_color)
