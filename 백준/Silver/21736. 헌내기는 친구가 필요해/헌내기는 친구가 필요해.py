# 헌내기는 친구가 필요해(실버2)
from collections import deque

dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(x,y):

    count=0
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        if field[x][y]=="P":
            count+=1
        for i in range(0, 4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if(new_x>=0 and new_x<n and new_y>=0 and new_y<m and visited[new_x][new_y]==False and field[new_x][new_y]!='X'):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))
    return count
n, m = map(int, input().split())
visited=[[False]*m for _ in range(n)]
field=[]
for i in range(n):
    field.append(list(input().strip()))

for i in range(n):
    for j in range(m):
        if field[i][j]=="I":
            answer = bfs(i,j)
if answer!=0:
    print(answer)
else:
    print("TT")