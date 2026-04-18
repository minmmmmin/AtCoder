for i in range(8):
    S = input()
    if "*" in S:
        j = S.find("*")
        print("abcdefgh"[j], 8 - i, sep="")
