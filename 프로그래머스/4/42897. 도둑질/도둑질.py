def solution(money):
    answer = 0
    
    money_forLast = money.copy()
    money_forLast[0] = 0
    
    money_cache= [0 for _ in range(len(money))]
    money_cache2 = [0 for _ in range(len(money))]
    
    
    # 초기화
    money_cache = money.copy()
    money_cache2 = money_forLast.copy()
    
    if(len(money)>3):
        money_cache[2] += money_cache[0]
        money_cache2[2] += money_cache2[0]
        
        for i in range(3, len(money)):
            money_cache[i] = max(money_cache[i-2] + money[i], money_cache[i-3] + money[i])

        for i in range(3, len(money_forLast)):
            money_cache2[i] = max(money_cache2[i-2] + money_forLast[i], money_cache2[i-3] + money_forLast[i])

        answer = max(money_cache[len(money)-2], money_cache[len(money)-3], money_cache2[len(money)-1])
    else:
        answer = max(money)
    
    
    return answer