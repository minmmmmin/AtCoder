n = int(input())
a = list(map(int, input().split()))

ans = "ok"

for i in range(n - 2):
    if a[i] * a[i + 2] != a[i + 1] * a[i + 1]:
        ans = "no"

if ans == "ok":
    print("Yes")
else:
    print("No")
