n = int(input())
s_list = [input() for _ in range(n)]

result_set = set()

for i in range(n):
    for j in range(n):
        if i != j:
            combined = s_list[i] + s_list[j]
            result_set.add(combined)

print(len(result_set))
