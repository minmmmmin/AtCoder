n = input()
S = list(map(str, input().split()))

w = ["and", "not", "that", "the", "you"]

for i in S:
    if i in w:
        print("Yes")
        exit()
print("No")
