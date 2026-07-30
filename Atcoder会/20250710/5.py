n = int(input())

even_numbers = [0, 2, 4, 6, 8]
result = ""
if n > 1:
    n -= 1

    while n > 0:
        result = str(even_numbers[n % 5]) + result
        n = n // 5

    print(result)
else:
    print(0)
