n, r, c = map(int, input().split())
s = input()

smoke_positions = set()
smoke_positions.add((0, 0))

fire_r, fire_c = 0, 0

takahashi_r, takahashi_c = r, c

reverse_move = {
    "N": (1, 0),
    "W": (0, 1),
    "S": (-1, 0),
    "E": (0, -1),
}

result = []

for t in range(n):
    dr, dc = reverse_move[s[t]]
    fire_r += dr
    fire_c += dc
    takahashi_r += dr
    takahashi_c += dc

    smoke_positions.add((fire_r, fire_c))

    if (takahashi_r, takahashi_c) in smoke_positions:
        result.append("1")
    else:
        result.append("0")

print("".join(result))
