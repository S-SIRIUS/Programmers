# 줄세우기(골드4)
import sys
input = sys.stdin.readline
n = int(input())
children=[]
for i in range(n):
    children.append(int(input()))

dp=[1]*(n)
for i in range(n):
    for j in range(i, n):
        if children[j] > children[i]:
            dp[j] = max(dp[j], dp[i]+1)
print(n-max(dp))