from collections import deque

def bfs(start, target, n):
    visited=[False]*(target+1)
    queue = deque([])
    queue.append((start,0))
    visited[start]=True
    while queue:
        new, value = queue.popleft()
        if new == target:
            return value
        else:
            if new*3<=target and visited[new*3]==False:
                queue.append((new*3, value+1))
                visited[new*3] = True
            if new*2<=target and visited[new*2]==False:
                queue.append((new*2, value+1))
                visited[new*2] = True
            if new+n<=target and visited[new+n]==False:
                queue.append((new+n, value+1))
                visited[new+n] = True
    return -1
    
def solution(x, y, n):
    answer = bfs(x,y,n)
    return answer