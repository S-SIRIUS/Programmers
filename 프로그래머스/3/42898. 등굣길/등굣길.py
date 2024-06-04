def solution(m, n, puddles):
    answer = 0
    # 대각선은 합친다. 웅덩이면 그냥 0됨
    table = [[0] * (m+1) for _ in range(n+1)]
    print(table)
    for i in range (1, n+1):
        for j in range (1, m+1):   
            if i==1 and j==1:
                table[i][j]=1
            elif [j, i] in puddles:
                table[i][j] = 0
            else:
                table[i][j] = table[i-1][j] + table[i][j-1]
    answer = table[n][m] % 1000000007
    return answer