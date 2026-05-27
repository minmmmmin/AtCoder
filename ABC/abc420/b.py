N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

scores = [0] * N

for j in range(M):
    ones = sum(S[i][j] == "1" for i in range(N))
    zeros = N - ones
    if ones == 0 or zeros == 0:
        for i in range(N):
            scores[i] += 1
    else:
        if zeros < ones:
            for i in range(N):
                if S[i][j] == "0":
                    scores[i] += 1
        else:
            for i in range(N):
                if S[i][j] == "1":
                    scores[i] += 1

mx = max(scores)
ans = [str(i + 1) for i in range(N) if scores[i] == mx]
print(" ".join(ans))
