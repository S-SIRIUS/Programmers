a=int(input())
dp=[0]*(1001) # a+1로 하면 메모리 오류난다.
dp[1]=1; dp[2]=2
for i in range(3, a+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[a]%10007)