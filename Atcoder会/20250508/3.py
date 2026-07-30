n = int(input())
ANS = []

while n > 0:
    n -= 1
    i = n % 26
    ANS.append(chr(ord("a") + i))
    n //= 26

ANS.reverse()
print("".join(ANS))
