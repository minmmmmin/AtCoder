N = int(input())

a = 1

for i in range(2, int(N ** 0.5) + 1):
  if N % i == 0:
    a = i
    
print(a + N // a - 2)

