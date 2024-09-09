# 뱀과 사다리 게임(골드5)
from collections import deque

def bfs(loc):
    queue=deque()
    queue.append(loc)
    visited[loc]=True
    
    while queue:
        loc = queue.popleft()

        for i in range(1, 7):
            new_loc = loc+i
            
            if 1<= new_loc<=100 and visited[new_loc]==False:
                if new_loc in ladder:
                    new_loc = ladder[new_loc]

                elif new_loc in snake:
                    new_loc = snake[new_loc]

                if visited[new_loc] == False:
                    queue.append(new_loc)
                    visited[new_loc] = True
                    field[new_loc] = field[loc]+1


n, m = map(int,input().split())
field=[0]*101
visited=[False]*101
ladder={}
snake={}
for i in range(n):
    index, value = map(int, input().split())
    ladder[index] = value
for i in range(m):
    index, value = map(int, input().split())
    snake[index] = value
bfs(1)
print(field[100])