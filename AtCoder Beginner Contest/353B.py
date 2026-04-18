N,K = map(int,input().split())

A = list(map(int,input().split()))

ans = 0
i = 0
cnt = 0

while i < N:
    if cnt + A[i] <= K:
        cnt += A[i]
        i += 1
    else:
        ans += 1
        cnt = 0

if cnt != 0: #収まりきってしまった場合そのゴンドラの加算
    ans += 1

print(ans)