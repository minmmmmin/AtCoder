n = int(input())
s = input()

a = False
ans = False

for i in s:
    if i == "|":
        a = not a
    if i == "*":
        if a:
            ans = True
print("in" if ans else "out")
