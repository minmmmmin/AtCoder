r, x = map(int, input().split())

if (r >= 1600 and r < 3000 and x == 1) or (r >= 1200 and r < 2400 and x == 2):
    print("Yes")
else:
    print("No")
