a, b, c, d = sorted(map(int, input().split()))
if a + b + c == d or a + d == b + c:
    print("Yes")
else:
    print("No")
