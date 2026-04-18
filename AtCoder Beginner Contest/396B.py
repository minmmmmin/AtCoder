stack = [0] * 100

Q = int(input().strip())

output = []

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        stack.append(x)
    else:
        output.append(stack.pop())

for ans in output:
    print(ans)
