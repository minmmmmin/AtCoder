n = int(input())
a = list(map(int, input().split()))

b = sum(a)
c = sum(x * x for x in a)

result = (b * b - c) // 2
print(result)
