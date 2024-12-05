# 연속된 정수의 합 구하기
n = int(input())
a = list(map(int, input().split()))
dp = [0]*(n)
dp2 = [0]*(n)
b = a.copy()
b.reverse()
dp[0] = a[0]
dp2[0] = b[0]

for i in range(1, n):
    dp[i] = max(a[i], dp[i-1]+a[i])
    dp2[i] = max(b[i], dp2[i-1] + b[i])
result = max(dp)
dp2.reverse()

for i in range(1, n-1):    
    temp = dp[i-1] + dp2[i+1]
    result = max(result, temp)
print(result)