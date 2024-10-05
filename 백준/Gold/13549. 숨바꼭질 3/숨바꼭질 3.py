# 숨바꼭질 3 (골드5)
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue= deque()
    queue.append((n, 0))
    visited[n]=True
    while queue:
        subin, time = queue.popleft()
        if subin == k:
            return time
        
        if 0<=(subin*2)<=100000 and visited[subin*2]==False:
            queue.appendleft((subin*2, time))
            visited[subin*2]=True
            
        if 0<=(subin-1) <= 100000 and visited[subin-1]==False:
            queue.append((subin-1, time+1))
            visited[subin-1]=True

        if 0<=(subin+1)<=100000 and visited[subin+1]==False:
            queue.append((subin+1, time+1))
            visited[subin+1]=True
  
n, k = map(int, input().split())
visited=[False]*(100001)
print(bfs())