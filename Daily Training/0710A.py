k = int(input())
ans = []

for i in range(k):
  ans.append(chr(65+i))

print(*ans, sep="")