n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

ab_sum = set()
for i in a:
    for j in b:
        ab_sum.add(i + j)

abc_sum = set()
for k in c:
    for s in ab_sum:
        abc_sum.add(s + k)

for xi in x:
    print("Yes" if xi in abc_sum else "No")
