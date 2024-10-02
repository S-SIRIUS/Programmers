# 벽부수고 이동하기(골드3)
import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y,brk):
    queue = deque()
    queue.append((x,y,brk))
    visited[x][y][0] =1
    
    while queue:
        x, y, brk = queue.popleft()

        if x==n-1 and y==m-1:
            return visited[x][y][brk]

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            # 일단 갈 수 있는지 체크
            if(0<=new_x<n and 0<=new_y<m):

                # 갈수있는 길이고 한번도 안갔으면 간다
                if field[new_x][new_y]==0 and visited[new_x][new_y][brk]==0:
                    queue.append((new_x, new_y, brk))
                    visited[new_x][new_y][brk]=visited[x][y][brk]+1
                
                # 막혀있는 길이고 그동안 벽을 부수지 않았다(brk==0)면 부순다
                elif field[new_x][new_y]==1 and brk==0:
                    queue.append((new_x, new_y, 1))
                    visited[new_x][new_y][1]= visited[x][y][brk]+1
    return -1

n, m = map(int, input().split())


field=[]
visited=[[[0]*(2) for _ in range(m)] for _ in range(n)]
for i in range(n):
    field.append(list(map(int, list(input().strip()))))
print(bfs(0,0,0))