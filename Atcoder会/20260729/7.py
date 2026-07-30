K = int(input())

r = 0

for i in range(1, K + 1):
    r = (r * 10 + 7) % K

    if r == 0:
        print(i)
        exit()

print(-1)
