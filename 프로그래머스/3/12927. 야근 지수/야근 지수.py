import heapq
def solution(n, works):
    answer = 0
    new_works=[]
    for i in works:
        new_works.append(-i)
    heapq.heapify(new_works)
    
    for i in range(0, n):
        temp = heapq.heappop(new_works)
        heapq.heappush(new_works, temp+1)
        
    for i in new_works:
        if i >0:
            answer = 0
            break
        answer += i**2
    return answer