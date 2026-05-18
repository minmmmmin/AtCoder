n,m = map(int,input().split())
f = list(map(int,input().split()))

a = set(f)

if len(a) == len(f):
    print("Yes")
else:
    print("No")

if len(a) == m:
    print("Yes")
else:
    print("No")


