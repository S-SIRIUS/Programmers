import heapq
def solution(scoville, K):
    answer = 0
    maxi = len(scoville)
    heapq.heapify(scoville)
    
    if(scoville[0]>=K):
        return answer
    
    while scoville:
        if(len(scoville) <2):
            answer=-1
            break
        answer+=1
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
        
        if(scoville[0] >= K):
            heapq.heappop(scoville)
            break
        
            
    
    return answer