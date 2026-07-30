N = int(input())
S = input()

n = len(S)

if n % 2 == 0:
    print("No")
else:
    middle_index = n // 2
    if not all(c == '1' for c in S[:middle_index]):
        print("No")
    else:
        if S[middle_index] != '/':
            print("No")
        else:
            if not all(c == '2' for c in S[middle_index+1:]):
                print("No")
            else:
                print("Yes")
