# 퇴사(실버3)
n = int(input())
ans = [()]
dp = [0]*(n+2)
for i in range(1, n+1):
    t, p = map(int, input().split())
    ans.append((t,p))

for i in range(1, n+1):
    
    dp[i] = max(dp[i], dp[i-1])
    t, p = ans[i]
    if i+t-1<=n:
        dp[i+t] = max(dp[i+t], dp[i] + p)
print(max(dp))