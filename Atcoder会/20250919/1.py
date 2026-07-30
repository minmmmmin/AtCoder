N = int(input())
S = input()

if N % 2 == 0:
    print("No")
    exit()

mid = N // 2

if S[mid] != "/":
    print("No")
    exit()

for i in range(mid):
    if S[i] != "1":
        print("No")
        exit()

for i in range(mid + 1, N):
    if S[i] != "2":
        print("No")
        exit()

print("Yes")
