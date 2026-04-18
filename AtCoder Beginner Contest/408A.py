n, s = map(int, input().split())
t = list(map(int, input().split()))
last_tap = 0

for i in range(n):
    if t[i] - last_tap > s:
        print("No")
        break
    last_tap = t[i]
else:
    print("Yes")
