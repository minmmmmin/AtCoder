N = int(input())
S = input()

if N % 2 == 1:
    print("No")
else:
    mid = N // 2

    ans = 0
    for i in range(mid):
        if S[i] == S[mid + i]:
            ans += 1

    if ans == mid:
        print("Yes")
    else:
        print("No")
