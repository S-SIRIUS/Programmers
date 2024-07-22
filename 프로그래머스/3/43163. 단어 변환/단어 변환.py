from collections import deque

def bfs(begin, target, words):
    answer = 0
    queue = deque()
    queue.append((begin,0))
    
    while queue:
        value, level = queue.popleft()
        print(value)
        if target == value:
            return level
        else:
            if value in words:
                words.remove(value)
            for i in words:
                count=0
                for j in range(0, len(value)):
                    if i[j]== value[j]:
                        count+=1
                    if count==len(value)-1:
                        queue.append((i, level+1))
                        words.remove(i)
                        break 
    return 0            

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer