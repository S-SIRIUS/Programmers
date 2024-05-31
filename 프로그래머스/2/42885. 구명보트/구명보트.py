from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque(people)
    summ=0

    while queue:  
        if (summ + queue[0]) <= limit:
            summ += queue.popleft()
            answer+=1           
        while queue:
            if (summ + queue[-1]) <= limit:
                queue.pop()
                summ=0
                break
                
            else:
                queue.pop()
                answer+=1    
    return answer
        
    