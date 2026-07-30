n = int(input())

a = list(map(int, input().split()))

a.sort()

all = (len(a) * (len(a) - 1)) / 2

dic = {}
for i in a:
    if i in dic:
        value = dic[i] + 1
        dic[i] = value
    else:
        dic[i] = 1

pattern = 0
for v in dic.values():
    pattern += v * (v - 1) / 2

print(dic)
print(int(all - pattern))
