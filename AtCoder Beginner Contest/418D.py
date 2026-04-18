import sys

input = sys.stdin.readline
N = int(input())
T = input().strip()

cnt = [[0, 0], [0, 0]]

cnt[0][0] = 1

ans = 0
px = 0
for i, ch in enumerate(T, 1):
    bit = 1 if ch == "1" else 0
    px ^= bit
    parity = i & 1

    ans += cnt[parity][px]

    ans += cnt[parity ^ 1][px ^ 1]

    cnt[parity][px] += 1

print(ans)
