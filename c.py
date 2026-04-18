n = int(input())
s = set()
for i in range(n):
    t = input()
    if t not in s:
        s.add(t)
    else:
        print("Yes")
        break
else:
    print("No")
