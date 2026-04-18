S = int(input())

if S % 4 != 0 or S % 100 == 0 and S%400 != 0:
    print("365")
else:
    print("366")
