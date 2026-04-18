A, op, B = input().split()
A = int(A)
B = int(B)

if op == "+":
    print(A + B)

elif op == "-":
    print(A - B)

elif op == "*":
    print(A * B)

elif op == "/":
    if B != 0 :
        print(A // B)
    else:
        print("error")

elif op == "?" or op == "=" or op == "!":
    print("error")


# ここにプログラムを追記
