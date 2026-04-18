S = input().strip()
digits = list(map(int, S))
cnt = 0
cntB = 0

while digits:
    last_digit = (digits[-1] - cntB) % 10
    if last_digit == 0:
        digits.pop()
        cnt += 1
    else:
        cntB += 1
        cnt += 1
print(cnt)
