n = int(input())
s = str(input())

stack = []
output = [0] * n
for i in range(n):
    if s[i] == "(":
      stack.append(i)
    elif s[i] == ")":
      if len(stack) > 0:
        output[stack.pop()] += 1
        if i + 1 < n:
          output[i + 1] -= 1
soutput = [0] * n
soutput[0] = output[0]
for i in range(1, n):
  soutput[i] = soutput[i - 1] + output[i]

for i in range(n):
  if soutput[i] == 0:
    print(s[i], end = "")
print()