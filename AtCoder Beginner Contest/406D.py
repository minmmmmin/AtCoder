from collections import defaultdict

H, W, N = map(int, input().split())

row_dict = defaultdict(set)
col_dict = defaultdict(set)

for _ in range(N):
    x, y = map(int, input().split())
    row_dict[x].add(y)
    col_dict[y].add(x)

Q = int(input())
deleted_rows = set()
deleted_cols = set()

for _ in range(Q):
    t, v = map(int, input().split())
    if t == 1:
        if v in deleted_rows:
            print(0)
        else:
            ys = row_dict[v]
            print(len(ys))
            for y in ys:
                col_dict[y].discard(v)
            row_dict[v].clear()
            deleted_rows.add(v)
    else:
        if v in deleted_cols:
            print(0)
        else:
            xs = col_dict[v]
            print(len(xs))
            for x in xs:
                row_dict[x].discard(v)
            col_dict[v].clear()
            deleted_cols.add(v)
