# xが何個あるか考える
N = int(input())
S = input()

x_pos = []

for i in range(N):
    if S[i] == "x":
        x_pos.append(i + 1)

# print(x_pos)

for k in range(1, N + 1):
    if k <= len(x_pos):
        print(x_pos[k - 1])
    else:
        print(N)
