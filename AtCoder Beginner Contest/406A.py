a, b, c, d = map(int, input().split())

ab_min = a * 60 + b
cd_min = c * 60 + d

if cd_min < ab_min:
    print("Yes")
else:
    print("No")
