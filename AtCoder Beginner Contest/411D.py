import sys

sys.setrecursionlimit(2 * 10**5 + 50)
input = sys.stdin.readline

n, q = map(int, input().split())

states = [(-1, "")]

pc = [0] * (n + 1)
server = 0

for _ in range(q):
    parts = input().split()
    t = parts[0]

    if t == "1":
        p = int(parts[1])
        pc[p] = server

    elif t == "2":
        p = int(parts[1])
        s = parts[2]

        parent_state_id = pc[p]
        new_state_id = len(states)
        states.append((parent_state_id, s))
        pc[p] = new_state_id

    else:
        p = int(parts[1])
        server = pc[p]

result_parts = []
cur = server

while cur != -1:
    parent_id, added_string = states[cur]
    if added_string:
        result_parts.append(added_string)
    cur = parent_id

print("".join(reversed(result_parts)))
