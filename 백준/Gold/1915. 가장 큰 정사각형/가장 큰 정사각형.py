# 가장 큰 정사각형 찾기
n, m = map(int, input().split())
dp = [[0]*(m+1)]
for i in range(1, n+1):
    dp.append([0] + list(map(int, input())))
maxi=0
for i in range(1, n+1):
    for j in range(1, m+1):
        if dp[i][j]!=0:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
            maxi = max(maxi, dp[i][j])
print(maxi*maxi)