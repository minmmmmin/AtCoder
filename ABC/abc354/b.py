N = int(input())
S = [] #先に配列の箱を作っちゃう
C = []
for i in range (N):
    s,c =map(str,input().split())
    S.append(s) #配列の末尾に要素を追加する
    C.append(int(c))

rate = sum(C)
S.sort() #辞書順になる

print(S[rate % N])
