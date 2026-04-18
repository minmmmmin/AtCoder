n = int(input())
MOD = 998244353

#これは何？２次元配列の作り方10は行の幅nは高さ
dp = [[0]* 10 for i in range(n)]

#1桁の時
for i in range(1,10):
    dp[0][i] = 1


for i in range(1, n):
    for j in range(1, 10):
        #1の時だけdp[i][j-1]が使えないので抜く
        if j != 1:
            dp[i][j] += dp[i-1][j-1]
            #先にMOD求めとく
            dp[i][j] %= MOD
            
        #すべての末尾に使える
        dp[i][j] += dp[i-1][j]
        dp[i][j] %= MOD
        
        #9の時だけdp[i][j+1]が使えないので抜く
        if j != 9:
            dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= MOD

ans = 0

#最後にN桁目だけ順番に足す
for i in range(1,10):
    #-1って何これは何?→後ろから見て１番目
    ans += dp[-1][i]
    #最後にもう一回割る
    ans %= MOD
    
print(ans)