S = input()
n = len(S)

max_fill = 0.0

for i in range(n):
    for j in range(i + 1, n + 1):
        t = S[i:j]
        if len(t) >= 3 and t[0] == "t" and t[-1] == "t":
            count_t = t.count("t")
            fill = (count_t - 2) / (len(t) - 2)
            max_fill = max(max_fill, fill)

print(max_fill)
