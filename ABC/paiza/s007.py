from collections import Counter

s = input()

stack = []
i = 0
n = len(s)

while i < n:
    if s[i] == "(":
        stack.append("(")
        i += 1

    elif s[i] == ")":
        temp = Counter()
        while stack and stack[-1] != "(":
            temp += stack.pop()
        stack.pop()

        i += 1
        j = i
        while j < n and s[j].isdigit():
            j += 1
        repeat = int(s[i:j]) if j > i else 1
        i = j

        for k in temp:
            temp[k] *= repeat
        stack.append(temp)

    elif s[i].isdigit():
        j = i
        while j < n and s[j].isdigit():
            j += 1

        repeat = int(s[i:j])
        i = j

        last = stack.pop()
        newc = Counter()
        for k in last:
            newc[k] = last[k] * repeat
        stack.append(newc)

    else:
        stack.append(Counter({s[i]: 1}))
        i += 1

cnt = Counter()
for c in stack:
    cnt += c

for c in "abcdefghijklmnopqrstuvwxyz":
    print(c, cnt[c])
