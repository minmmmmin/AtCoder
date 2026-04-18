L,R = map(int,input().split())

count = 0
for num in range(L, R + 1):
    num_str = str(num)
    if all(num_str[i] >= num_str[i + 1] for i in range(len(num_str) - 1)):
        count += 1

print(count)