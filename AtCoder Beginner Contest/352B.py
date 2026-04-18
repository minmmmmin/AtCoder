S = input()
T = input()

a = 0

for i in range(len(S)):
    for j in range(a,len(T)):
        if S[i] == T[j]:
            print(j + 1,end=" ")
            a = j + 1
            break
            