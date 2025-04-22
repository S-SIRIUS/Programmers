from collections import deque
dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(i, j,maps, target, score, n, m):
    visited=[[0]*(m) for _ in range(n)]
    queue = deque()
    queue.append((i,j,score))
    visited[i][j]=1
    while queue:
        x, y, score = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<n and 0<=new_y<m and maps[new_x][new_y]==target:
                score+=1
                return new_x, new_y, score
            elif 0<=new_x<n and 0<=new_y<m and maps[new_x][new_y]!='X' and visited[new_x][new_y]==0:
                visited[new_x][new_y]=1
                queue.append((new_x, new_y, score+1))
    return -1, -1, -1
            
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    score=0
    start_x, start_y = 0, 0;
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='S':
                start_x, start_y = i, j
                break
    x, y, score = bfs(start_x, start_y, maps, 'L', score, n, m)
    if x==-1:
        return -1
    else:
        x, y, score = bfs(x, y, maps, 'E', score, n, m)
    return score