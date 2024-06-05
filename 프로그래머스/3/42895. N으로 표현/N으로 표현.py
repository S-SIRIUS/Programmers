def solution(N, number):
    if N == number:
        return 1

    # dp 리스트 초기화
    dp = [set() for _ in range(9)]
    
    # 초기값 설정
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
    
    # dp를 이용한 최소값 탐색
    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        # 목표 숫자를 찾은 경우
        if number in dp[i]:
            return i

    return -1