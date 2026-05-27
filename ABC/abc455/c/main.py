from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)

# print(c)

loss = []

for x, cnt in c.items():
    loss.append(x * cnt)

loss.sort(reverse=True)

# print(loss)

ans = sum(A) - sum(loss[:K])
print(ans)