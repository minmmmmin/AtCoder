from collections import defaultdict

N, K, M = map(int, input().split())

gems = defaultdict(list)

for _ in range(N):
    c, v = map(int, input().split())
    gems[c].append(v)

# print(gems)

tops = []
rest = []

for color in gems:
    values = sorted(gems[color], reverse=True)
    tops.append(values[0])
    rest.extend(values[1:])

# print(tops)
# print(rest)

tops.sort(reverse=True)

ans = sum(tops[:M])

# 色数を満たした後はでっかいのから
sub = tops[M:] + rest
sub.sort(reverse=True)

ans += sum(sub[: K - M])

print(ans)
