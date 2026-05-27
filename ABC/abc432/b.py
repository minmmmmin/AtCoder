x = input().strip()

digits = list(x)

digits.sort()

if digits[0] == "0":
    for i in range(len(digits)):
        if digits[i] != "0":
            digits[0], digits[i] = digits[i], digits[0]
            break

ans = "".join(digits)
print(ans)
