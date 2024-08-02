# 동전1 (골드V)
n, k = map(int, input().split())
dp=[0]*(k+1)
coin=[]
for i in range(n):
    coin.append(int(input()))
dp[0]=1
coin.sort()
for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
print(dp[k])