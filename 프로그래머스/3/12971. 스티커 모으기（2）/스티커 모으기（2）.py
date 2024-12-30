def solution(sticker):
    answer = 0
    
    if len(sticker)==1:
        answer = sticker[0]
    elif len(sticker)==2:
        answer = max(sticker[0], sticker[1])
    else:
        sticker1 = sticker[0:-1]
        dp = sticker[0 : -1]
        sticker2 = sticker[1:]
        dp2 = sticker[1:]
        dp[1] = max(dp[0], dp[1])
        dp2[1] = max(dp2[0], dp2[1])
    
        for i in range(2, len(sticker)-1):
            dp[i] = max(dp[i-2]+sticker1[i], dp[i-1])
            dp2[i] = max(dp2[i-2]+sticker2[i], dp2[i-1])
        answer= max(max(dp), max(dp2))
        
    return answer