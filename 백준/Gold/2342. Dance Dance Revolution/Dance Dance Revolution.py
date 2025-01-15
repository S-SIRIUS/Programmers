# DDR을 해보자(골드3)
import sys
input = sys.stdin.readline
temp = int(1e9)
dp=[[[temp]*(5) for _ in range(5)] for _ in range(100001)]

s=1
dp[0][0][0]=0
mp=[[0, 2, 2, 2, 2],
    [2, 1, 3, 4, 3],
    [2, 3, 1, 3, 4],
    [2, 4, 3, 1, 3],
    [2, 3, 4, 3, 1]]
field = list(map(int ,input().split()))
index=0

while field[index]!=0:
    n = field[index]
    for i in range(5):
        if n==i:
            continue
        for j in range(5):
            dp[s][i][n] = min(dp[s-1][i][j] + mp[j][n], dp[s][i][n])
    
    for i in range(5):
        if n==i:
            continue
        for j in range(5):
            dp[s][n][i] = min(dp[s-1][j][i] + mp[j][n], dp[s][n][i])
    
    s+=1
    index+=1

s-=1

result = int(1e9)
for i in range(5):
    for j in range(5):
        result = min(result, dp[s][i][j])
print(result)