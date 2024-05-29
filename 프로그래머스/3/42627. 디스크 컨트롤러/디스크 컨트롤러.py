import heapq
def solution(jobs):
    answer = 0
    finish = 0
    now_Time = 0
    heap=[]
    total_Time= 0
    before_Request = -1
    
    while finish < len(jobs):
        for job in jobs:
            if before_Request < job[0] <= now_Time:
                heapq.heappush(heap, [job[1], job[0]])
        
        if len(heap) > 0:
            now_Working = heapq.heappop(heap)
            before_Request = now_Time
            now_Time += now_Working[0]
            total_Time += (now_Time - now_Working[1])
            finish += 1
        else:
            now_Time += 1
    answer = int(total_Time / len(jobs))
    return answer