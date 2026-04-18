r, c = map(int, input().split())

d = max(abs(r - 8), abs(c - 8))

print("white" if d % 2 == 0 else "black")
