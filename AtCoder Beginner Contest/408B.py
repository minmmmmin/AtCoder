n = int(input())
a = list(map(int, input().split()))

ans = sorted(set(a))

print(len(ans))
print(*ans)
