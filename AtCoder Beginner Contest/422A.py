S = input().strip()
i, j = map(int, S.split('-'))

if j < 8:
    print(f"{i}-{j+1}")
else:
    print(f"{i+1}-1")
