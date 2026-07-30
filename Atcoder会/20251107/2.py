N, L, R = map(int, input().split())
if L > 1:
    print(*range(1, L), end=" ")
print(*range(R, L - 1, -1), end=" ")

print(*range(R + 1, N + 1))
