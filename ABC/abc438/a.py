D, F = map(int, input().split())

shift = D % 7
ans = F - shift

if ans <= 0:
    ans += 7

print(ans)
