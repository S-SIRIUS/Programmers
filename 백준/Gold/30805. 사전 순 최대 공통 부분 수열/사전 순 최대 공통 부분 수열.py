n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

dp = [[[] for _ in range(m+1)] for _ in range(n+1)]

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        candidates = []
        if A[i] == B[j]:
            candidates.append([A[i]] + dp[i+1][j+1])
        candidates.append(dp[i+1][j])
        candidates.append(dp[i][j+1])
        
        dp[i][j] = max(candidates)

result = dp[0][0]
print(len(result))
if result:
    print(*result)