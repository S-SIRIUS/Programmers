from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, maps):
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(0, 4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            
            if new_x <0 or new_y<0 or new_x >= len(maps) or new_y >= len(maps[0]):
                continue
            if maps[new_x][new_y] == 0:
                continue
            if maps[new_x][new_y] == 1:
                queue.append((new_x, new_y))
                maps[new_x][new_y] = maps[x][y]+1         

def solution(maps):
    answer = 0
    bfs(0,0, maps)
    answer = maps[len(maps)-1][len(maps[0])-1]
    
    if(answer==1):
        answer=-1
    
    return answer