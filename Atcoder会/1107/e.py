s = list(input())
t = list(input())
n = len(s)
X = []

while s != t:
    a = -1
    # 辞書順で大きくなる時は末尾から見る
    for i in range(n - 1, -1, -1):
        if s[i] > t[i]:
            a = i
    # 逆に小さくなる時はなるときは先頭から見る
    if a == -1:
        for i in range(n):
            if s[i] < t[i]:
                a = i

    s[a] = t[a]
    X.append("".join(s))

print(len(X))
for i in X:
    print(i)
