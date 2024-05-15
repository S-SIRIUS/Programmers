from collections import deque
def solution(arr):
    queue = deque()
    
    for i in arr:
        queue.append(i)
    ans=[]
    while queue:
        value = queue.popleft()            
        if(len(ans)==0 or (len(ans)>0 and value != ans[-1])):
            ans.append(value)
    return ans