import sys
input = sys.stdin.readline

t = int(input())
ans = []

for _ in range(t):
    a = input().strip()
    b = input().strip()

    sa = []
    for c in a:
        sa.append(c)
        while len(sa) >= 4 and sa[-4] == '(' and sa[-3] == 'x' and sa[-2] == 'x' and sa[-1] == ')':
            sa.pop()
            sa.pop()
            sa.pop()
            sa.pop()
            sa.append('x')
            sa.append('x')

    sb = []
    for c in b:
        sb.append(c)
        while len(sb) >= 4 and sb[-4] == '(' and sb[-3] == 'x' and sb[-2] == 'x' and sb[-1] == ')':
            sb.pop()
            sb.pop()
            sb.pop()
            sb.pop()
            sb.append('x')
            sb.append('x')

    if sa == sb:
        ans.append("Yes")
    else:
        ans.append("No")

print("\n".join(ans))