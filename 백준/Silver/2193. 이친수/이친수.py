n=int(input())
dp=[0]*(91)
dp[1]=1
dp[2]=1
for i in range(1,n-1):
    dp[i+2]=dp[i+1]+dp[i]
print(dp[n])