N = int(input())
w = [list(map(int, input().split())) for _ in range(N)]
d = [list(map(int, input().split())) for _ in range(N)]

used = [[False] * N for _ in range(N)]
res = []


def dist(i, j):
    return i + j


def can_stack(stack, new_box, dist):
    temp_stack = stack + [new_box]
    for i in range(len(temp_stack)):
        weight_above = sum(w for w, _ in temp_stack[i + 1 :])
        if temp_stack[i][1] < weight_above * dist:
            return False
    return True


positions = []
for total in range(1, 2 * N - 1):
    for i in range(N):
        j = total - i
        if 0 <= j < N and (i != 0 or j != 0):
            positions.append((i, j))

idx = 0
while idx < len(positions):
    i1, j1 = positions[idx]
    if used[i1][j1]:
        idx += 1
        continue

    stack = [(w[i1][j1], d[i1][j1])]
    used[i1][j1] = True

    res += ["D"] * i1 + ["R"] * j1
    res.append("1")

    for _ in range(2):
        best_score = float("inf")
        best_pos = None

        for jdx in range(idx + 1, len(positions)):
            i2, j2 = positions[jdx]
            if used[i2][j2]:
                continue

            move_dist = abs(i2 - i1) + abs(j2 - j1)
            total_dist = dist(i1, j1) + move_dist + i2 + j2

            box2 = (w[i2][j2], d[i2][j2])

            if not can_stack(stack, box2, total_dist):
                continue

            weight_above = sum(w for w, _ in stack)
            durability_margin = box2[1] - weight_above * total_dist
            score = total_dist + 0.5 * box2[0] - durability_margin * 0.1

            if score < best_score:
                best_score = score
                best_pos = (i2, j2)

        if best_pos is None:
            break

        i2, j2 = best_pos
        move_i = i2 - i1
        move_j = j2 - j1
        res += ["D" if move_i > 0 else "U"] * abs(move_i)
        res += ["R" if move_j > 0 else "L"] * abs(move_j)
        res.append("1")
        stack.append((w[i2][j2], d[i2][j2]))
        used[i2][j2] = True
        i1, j1 = i2, j2

    res += ["L"] * j1 + ["U"] * i1
    idx += 1

print("\n".join(res))
