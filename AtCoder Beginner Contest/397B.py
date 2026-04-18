S = input()

count = 0
T = ""

for i in range(len(S)):
    if len(T) % 2 == 0:
        if S[i] != "i":
            T += "i"
            count += 1
        T += S[i]
    else:
        if S[i] != "o":
            T += "o"
            count += 1
        T += S[i]

if len(T) % 2 != 0:
    T += "o"
    count += 1

print(count)
