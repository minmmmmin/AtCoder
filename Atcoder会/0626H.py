import sys

input = sys.stdin.readline

N = int(input())
ans = 0
i = 1

while i <= N:
    q = N // i
    # q出てくる区間（i~j）
    j = N // q
    count = j - i + 1
    ans += q * count
    # 次の区間に行く
    i = j + 1

print(ans)
