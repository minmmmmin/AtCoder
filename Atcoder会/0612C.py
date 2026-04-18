p = list(map(int, input().split()))

for i in p:
    print(chr(ord("a") + i - 1), end="")
