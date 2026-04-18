N = int(input())
d = [int(input()) for i in range(N)]

d.sort()
d.reverse()

count = 1

for i in range(0,N-1):
    if d[i] > d[i+1]:
        count += 1

print(count)