q = int(input())
S = []
b = 0

for _ in range(q):
    query = input().split()
    ok = True

    if query[0] == "1":
        c = query[1]
        S.append(c)
    else:
        c = S.pop()
    b = 0
    ok = True
    for c in S:
        if c == "(":
            b += 1
        else:
            b -= 1
        if b < 0:
            ok = False
            break
    # print(S)
    if ok and b == 0:
        print("Yes")
    else:
        print("No")
