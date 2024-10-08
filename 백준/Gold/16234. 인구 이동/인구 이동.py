# 인구 이동(골드4)
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    union=[]
    queue = deque()
    queue.append((x,y))
    union.append((x,y))

    total=field[x][y]
    count=1
    visited[x][y]=True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0<=new_x<n and 0<=new_y<n and visited[new_x][new_y]==False and l<=abs(field[new_x][new_y] - field[x][y])<=r:
                visited[new_x][new_y]=True
                total+=field[new_x][new_y]
                count+=1
                queue.append((new_x, new_y))
                union.append((new_x, new_y))

    if len(union)==1:
        total, count = 0, 0
        union.pop()

    return total, count, union

n, l , r = map(int, input().split())
field=[]
for i in range(n):
    field.append(list(map(int, input().split())))

day=0
while True:
    visited = [[False]*(n) for _ in range(n)]
    integration=False
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                total, count, union = bfs(i,j)

            if count!=0:
                for a,b in union:
                    field[a][b] = total//count
                integration=True
    if integration:
        day+=1
    else:
        break
print(day)