n, q = map(int, input().split())
a = list(map(int, input().split()))

color = [False] * (n + 2)
count = 0

for x in a:
    i = x

    left_black = color[i - 1]
    right_black = color[i + 1]
    current_black = color[i]

    if current_black:
        if not left_black and not right_black:
            count -= 1
        elif left_black and right_black:
            count += 1
    else:
        if not left_black and not right_black:
            count += 1
        elif left_black and right_black:
            count -= 1

    color[i] = not color[i]

    print(count)
