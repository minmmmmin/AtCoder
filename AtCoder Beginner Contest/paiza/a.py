s = input()

a = s[0]
op = s[2]
b = s[4]
c = s[8]

if a == "x":
    if op == "-":
        print(int(b) + int(c))
    else:
        print(int(c) - int(b))
if b == "x":
    if op == "-":
        print(int(a) - int(c))
    else:
        print(int(c) - int(a))
if c == "x":
    if op == "-":
        print(int(a) - int(b))
    else:
        print(int(a) + int(b))
