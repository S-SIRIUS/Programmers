from collections import deque
      
def solution(queue1, queue2):
    result=0
    size = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    if(s1+s2)%2!=0:
        result=-1
    else:
        target = (s1+s2)//2
        i=0
        while i < size*3:
            if s1 > s2:
                temp = queue1.popleft()
                queue2.append(temp)
                s1-=temp
                s2+=temp
                result+=1
            elif s1 < s2:
                temp = queue2.popleft()
                queue1.append(temp)
                s2-=temp
                s1+=temp
                result+=1
            else:
                break
            i+=1
        if s1!=s2:
            result=-1
    return result