S = input()

n = 0
for _ in S:
    n += 1
if n % 2 != 0:
    print("No")
else:
    i = 0
    is_valid = True
    while i < n:
        if S[i] != S[i + 1]:
            is_valid = False
            break
        i += 2
    if not is_valid:
        print("No")
    else:
        is_valid = True
        for char in S:
            count = 0
            for c in S:
                if c == char:
                    count += 1
            if count != 2:
                is_valid = False
                break
        if is_valid:
            print("Yes")
        else:
            print("No")
