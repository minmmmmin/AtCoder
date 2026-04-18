N = int(input())
S = input()

max_length = 0
n = len(S)

count_1 = [0] * (n + 1)
count_2 = [0] * (n + 1)

for i in range(1, n + 1):
    count_1[i] = count_1[i - 1] + (1 if S[i - 1] == '1' else 0)
    count_2[i] = count_2[i - 1] + (1 if S[i - 1] == '2' else 0)

for i in range(n):
    for j in range(i + 1, n + 1, 2):
        length = j - i
        middle_index = length // 2

        if S[i + middle_index] == '/':
            if count_1[i + middle_index] - count_1[i] == middle_index and count_2[j] - count_2[i + middle_index + 1] == middle_index:
                max_length = max(max_length, length)

print(max_length)