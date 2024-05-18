from collections import deque
def solution(priorities, location):
    answer = 0
    
    queue1 = deque()
    queue2 = deque()
    
    for p in priorities:
        queue1.append(p)
    
    for i in range(0, len(priorities)):
        queue2.append(i)

    while queue1:  
        if queue1[0] < max(queue1):
            queue1.append(queue1[0])
            queue1.popleft()
            
            queue2.append(queue2[0])
            queue2.popleft()
        
        else:
            answer+=1
            
            if queue2[0] == location:
                    break
            queue1.popleft()
            queue2.popleft()
            
    return answer