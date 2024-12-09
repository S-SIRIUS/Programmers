from collections import deque
def solution(order):
    
    original_order = [i for i in range(1, len(order)+1)]
    queue = deque(original_order)
    
    convey=[]
    result=0
    cnt=0
    
    while queue:
        now = queue.popleft()
        
        if convey and convey[-1] == order[cnt]:
            cnt+=1
            result+=1
            convey.pop()
        if now == order[cnt]:
            result+=1
            cnt+=1
        else:
            convey.append(now)

    while convey:
        convey_now = convey.pop()
        if convey_now == order[cnt]:
            result+=1
            cnt+=1
        else:
            break
    return result