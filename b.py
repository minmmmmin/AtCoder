N = input()

for i in range(len(N)):
    if N[i].isupper():
        print(i + 1)
        break
