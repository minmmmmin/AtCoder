n,a,b = map(int,input().split())

ans = 0

for i in range(1,n+1):
    val = i
    sum = 0
    while i != 0:
        sum += i%10
        i = i//10
    if a <= sum and sum <= b:
        ans += val

print(ans)