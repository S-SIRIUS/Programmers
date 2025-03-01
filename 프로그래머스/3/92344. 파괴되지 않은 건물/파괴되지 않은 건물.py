def solution(board, skill):
    answer = 0
    d=[[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for s in skill:
        if s[0]==1:
            value = -s[5]
        else:
            value = s[5]
        d[s[1]][s[2]] += (value)
        d[s[3]+1][s[4]+1] += (value)
        d[s[1]][s[4]+1] -= (value)
        d[s[3]+1][s[2]] -= (value)

    for i in range(1, len(board[0])):
        for j in range(0, len(board)):
            d[j][i] += d[j][i-1]
    
    for i in range(1, len(board)):
        for j in range(0, len(board[0])):
            d[i][j] += d[i-1][j]
    
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if (board[i][j] + d[i][j])>0:
                answer+=1
    return answer