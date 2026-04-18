n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

m = max(a)
flag = False

for i in range(k):
    if a[b[i] - 1] == m:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
