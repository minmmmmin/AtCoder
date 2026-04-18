S = input()

answer = 0

for i in range(len(S)):
    if S[i] == "1":
        answer += 1

print(answer)