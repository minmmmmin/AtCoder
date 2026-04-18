n = int(input())

s = ['-'] * n

if n % 2 == 1:
    s[n // 2] = '='
else:
    s[n // 2 - 1] = '='
    s[n // 2] = '='

print("".join(s))
