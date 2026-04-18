from collections import deque

q = int(input())
s = [input() for _ in range(q)]

queue = deque()

for line in s:
    parts = line.split()
    if parts[0] == "1":
        x = int(parts[1])
        queue.append(x)
    else:
        print(queue.popleft())
