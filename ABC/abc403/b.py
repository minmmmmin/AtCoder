t = input()
u = input()

n = len(t)
m = len(u)
ok = False

for i in range(n - m + 1):
    match = True
    for j in range(m):
        if t[i + j] != "?" and t[i + j] != u[j]:
            match = False
            break
    if match:
        ok = True
        break

if ok:
    print("Yes")
else:
    print("No")
