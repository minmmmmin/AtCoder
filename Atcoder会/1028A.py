a, b = map(int, input().split())
s=list(input())

result = ""
count = 0
for i in range(a):
    if s[i] == 'o' and count < b:
        result += 'o'
        count += 1
    else:
        result += 'x'

print(result)