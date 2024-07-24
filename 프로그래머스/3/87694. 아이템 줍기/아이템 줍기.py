from collections import deque


dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]
def bfs(visited, new_chX, new_chY, new_itemX, new_itemY, field):
    
    queue = deque()
    
    queue.append((new_chX, new_chY, 1))
    while queue:
        x, y, distance= queue.popleft()
        
        if x== new_itemX and y == new_itemY:
            return distance//2
        else:
            for i in range(0, 4):
                n_x = x + dx[i]
                n_y = y + dy[i]
                
                if(0<=n_x<102 and 0<=n_y<102 and visited[n_x][n_y]==False and field[n_x][n_y]==1):
                    visited[n_x][n_y]= True
                    queue.append((n_x, n_y, distance+1))
            
            

def solution(rectangle, characterX, characterY, itemX, itemY):
    field=[[-1]*102 for _ in range(102)]
    visited=[[False]*102 for _ in range(102)]
    
    for rec in rectangle:
        re_x1, re_y1, re_x2, re_y2 = map(lambda x: x*2, rec)
        
        for i in range(re_x1, re_x2+1):
            for j in range(re_y1, re_y2+1):
                if re_x1< i <re_x2 and re_y1 < j <re_y2:
                    field[i][j]=0
                elif field[i][j]!=0:
                    field[i][j]=1
    new_chX, new_chY, new_itemX, new_itemY = characterX*2, characterY*2, itemX*2, itemY*2
    
    answer = bfs(visited, new_chX, new_chY, new_itemX, new_itemY, field)
    
    return answer