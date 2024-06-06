def solution(arr):
    n = (len(arr) + 1) // 2  # 숫자의 개수
    
    # 최대값과 최소값을 저장할 DP 테이블 생성
    max_dp = [[None] * n for _ in range(n)]
    min_dp = [[None] * n for _ in range(n)]
    
    # 초기화: 숫자들은 그대로 DP 테이블에 넣는다
    for i in range(n):
        max_dp[i][i] = int(arr[2 * i])
        min_dp[i][i] = int(arr[2 * i])
    
    # DP 테이블 채우기
    for length in range(1, n):  # 부분 문제의 길이
        for i in range(n - length):
            j = i + length
            max_val = -float('inf')
            min_val = float('inf')
            for k in range(i, j):
                operator = arr[2 * k + 1]
                if operator == '+':
                    max_val = max(max_val, max_dp[i][k] + max_dp[k + 1][j])
                    min_val = min(min_val, min_dp[i][k] + min_dp[k + 1][j])
                elif operator == '-':
                    max_val = max(max_val, max_dp[i][k] - min_dp[k + 1][j])
                    min_val = min(min_val, min_dp[i][k] - max_dp[k + 1][j])
            max_dp[i][j] = max_val
            min_dp[i][j] = min_val
    
    return max_dp[0][n - 1]