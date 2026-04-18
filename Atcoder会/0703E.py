n = int(input())
s = input()

x, y = 0, 0

visited = set()
visited.add((x, y))

for move in s:
    if move == "R":
        x += 1
    elif move == "L":
        x -= 1
    elif move == "U":
        y += 1
    elif move == "D":
        y -= 1

    if (x, y) in visited:
        print("Yes")
        break
    visited.add((x, y))
else:
    print("No")
