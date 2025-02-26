import heapq
def solution(n, works):
    answer = 0
    queue=[]
    for w in works:
        queue.append(-w)
    heapq.heapify(queue)
    
    while n>0:
        work = heapq.heappop(queue)
        if work==0:
            break
        work+=1
        heapq.heappush(queue, work)
        n-=1
    
    answer=0
    for q in queue:
        answer += q**2
    return answer