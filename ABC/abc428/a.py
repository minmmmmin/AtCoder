s, a, b, x = map(int, input().split())

cycle = a + b
full = x // cycle
remainder = x % cycle

ans = full * s * a + s * min(a, remainder)

print(ans)
