# 내려가기(골드5)
import sys
input = sys.stdin.readline
n = int(input())
field = [[int(x) for x in input().split()] for i in range(n)]
max_dp = [0] * 3
min_dp = [0] * 3
prev_max_dp = [0] * 3
prev_min_dp = [0] * 3

# 첫 번째 줄 초기화
prev_max_dp[0], prev_max_dp[1], prev_max_dp[2] = field[0][0], field[0][1], field[0][2]
prev_min_dp[0], prev_min_dp[1], prev_min_dp[2] = field[0][0], field[0][1], field[0][2]

for i in range(1, n):
    max_dp[0] = max(prev_max_dp[0], prev_max_dp[1]) + field[i][0]
    max_dp[1] = max(prev_max_dp[0], prev_max_dp[1], prev_max_dp[2]) + field[i][1]
    max_dp[2] = max(prev_max_dp[1], prev_max_dp[2]) + field[i][2]

    min_dp[0] = min(prev_min_dp[0], prev_min_dp[1]) + field[i][0]
    min_dp[1] = min(prev_min_dp[0], prev_min_dp[1], prev_min_dp[2]) + field[i][1]
    min_dp[2] = min(prev_min_dp[1], prev_min_dp[2]) + field[i][2]

    prev_max_dp = max_dp[:]
    prev_min_dp = min_dp[:]

print(max(prev_max_dp), min(prev_min_dp))