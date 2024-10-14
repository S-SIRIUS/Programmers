def solution(n):
    dp=[0]*(n+1)
    
    dp[1]=1
    dp[2]=1
    
    if n>=3:
        for i in range(1, n-1):
            dp[i+2] = dp[i+1]+dp[i]
    return dp[n] % 1234567