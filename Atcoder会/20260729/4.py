# 順番に見ていくゆっくり

S = input()

a = 0
ab = 0
ans = 0

for x in S:
    if x == "A":
        a += 1

    elif x == "B":
        if a > 0:
            a -= 1
            ab += 1

    else:
        if ab > 0:
            ab -= 1
            ans += 1

print(ans)
