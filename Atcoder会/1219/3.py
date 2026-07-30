S = input()

upper = 0
lower = 0

for i in range(len(S)):
    if S[i].isupper():
        upper += 1
    else:
        lower += 1

if upper > lower:
    print(S.upper())
else:
    print(S.lower())
