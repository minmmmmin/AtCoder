x, y = map(int, input().split())

if x == 2 or y == 2:
    print("No")

elif y == 4 or y == 6 or y == 9 or y == 11:
    if x == 4 or x == 6 or x == 9 or x == 11:
        print("Yes")
    else:
        print("No")

elif x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
    print("Yes")

else:
    print("No")
