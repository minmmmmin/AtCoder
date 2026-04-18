N = int(input())
ans = 0
for i in range(1, 10 ** 6 + 1):
    
  num = i * i * i
  if num <= N and str(num) == str(num)[::-1]:
    ans = num

print(ans)