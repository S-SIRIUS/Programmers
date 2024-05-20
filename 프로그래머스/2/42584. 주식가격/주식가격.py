from collections import deque
def solution(prices):
    answer = []    
    prices_queue=deque(prices)
    time=0
    
    while prices_queue:
        standard=prices_queue.popleft()
        
        for price in prices_queue:
            if(standard <= price):
                time+=1
            else:
                time+=1
                break
        
        answer.append(time)
        time=0
        
    return answer