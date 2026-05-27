n, a, b = map(int, input().split())
s = input()

for i in range(a, n - b):
    print(s[i], end="")
