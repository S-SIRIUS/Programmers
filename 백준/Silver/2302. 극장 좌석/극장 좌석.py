# 극장좌석(실버1)
n = int(input())
m = int(input())
start=0
dp=[0]*(41)
dp[0]=1
dp[1]=1
dp[2]=2
for i in range(3, 41):
    dp[i] = dp[i-1]+dp[i-2]
total=1
if m==0:
    total=dp[n]
else:
    for i in range(m):
        end = int(input())
        total*=dp[end-start-1]
        start=end
    if n>end:
        total*=dp[n-end]
print(total)