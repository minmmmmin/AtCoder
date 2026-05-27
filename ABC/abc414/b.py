n = int(input())
result = []
total_length = 0

for _ in range(n):
    c, l = input().split()
    l = int(l)
    total_length += l
    if total_length > 100:
        print("Too Long")
        exit()
    result.append(c * l)

print("".join(result))
