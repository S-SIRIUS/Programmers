import copy
def solution(land):
    answer = 0
    dp= copy.deepcopy(land)
    for i in range(1, len(land)):
        for j in range(0, 4):
            if j == 0:
                dp[i][j] += max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
            elif j == 1:
                dp[i][j] += max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
            elif j == 2:
                dp[i][j] += max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
            else:
                dp[i][j] += max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    return max(dp[len(land)-1])