N, M, Q = map(int, input().split())

permissions = [None] * (N + 1)
all_permissions = [False] * (N + 1)

output = []

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        X, Y = query[1], query[2]
        if not all_permissions[X]:
            if permissions[X] is None:
                permissions[X] = set()
            permissions[X].add(Y)

    elif query[0] == 2:
        X = query[1]
        all_permissions[X] = True
        permissions[X] = None

    elif query[0] == 3:
        X, Y = query[1], query[2]
        if all_permissions[X]:
            output.append("Yes")
        elif permissions[X] is not None and Y in permissions[X]:
            output.append("Yes")
        else:
            output.append("No")

print("\n".join(output))
