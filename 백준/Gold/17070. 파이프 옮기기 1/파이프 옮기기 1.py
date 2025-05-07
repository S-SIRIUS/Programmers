# 파이프 옮기기1(골드5)
n = int(input())
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0]=1
field=[]
for i in range(n):
    field.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if field[i][j]==1:
            continue
        else:
            if j-1>=0:
                dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]

            if i-1>=0:
                dp[i][j][1] += dp[i-1][j][1] +dp[i-1][j][2]
            
            if i-1>=0 and j-1>=0:
                if field[i-1][j]==0 and field[i][j-1]==0:
                    dp[i][j][2] += dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
print(sum(dp[n-1][n-1]))