import math
from collections import deque
def solution(progresses, speeds):    
    s_index = len(speeds)-1
    d_time=[]
    while progresses:
        value = progresses.pop()
        rest_time = 100 - value
        distribute_time = math.ceil(rest_time / speeds[s_index])
        d_time.append(distribute_time)
        s_index-=1
    
    
    count=0
    answer=[]
    
    queue = deque()
    for i in d_time:
        queue.appendleft(i)
    print(queue)
    
    while queue:
        standard=queue.popleft()
        count=1
        while queue and standard >= queue[0]:
            count+=1
            queue.popleft()
        answer.append(count)
    print(answer)
    return answer