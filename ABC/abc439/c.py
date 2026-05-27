import math

N = int(input())

count = [0] * (N + 1)

# ルートまで見れば十分
limit = int(math.isqrt(N))

for x in range(1, limit + 1):
    x2 = x * x
    for y in range(x + 1, limit + 1):
        s = x2 + y * y
        if s > N:
            break
        if count[s] < 2:
            count[s] += 1

ans = []
for i in range(1, N + 1):
    if count[i] == 1:
        ans.append(i)

print(len(ans))
if ans:
    print(*ans)
else:
    print()
