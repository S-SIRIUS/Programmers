# 연구소(골드4)
from collections import deque
import sys
import copy

input = sys.stdin.readline

dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

maximum = int(-1e9)

def bfs(field):
    temp_field = copy.deepcopy(field)
    queue= deque()
    global maximum
    
    for i in range(n):
        for j in range(m):
            if temp_field[i][j]==2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x <0 or new_x >=n or new_y<0 or new_y>=m:
                continue
            if temp_field[new_x][new_y]==0:
                temp_field[new_x][new_y]=2
                queue.append((new_x, new_y))

    total=0
    for i in range(n):
        total += temp_field[i].count(0)
        
    if total > maximum:
        maximum = total
    return

def make_wall(count):
    if count ==3:
        bfs(field)
        return
    for i in range(n):
        for j in range(m):
            if field[i][j]==0:
                field[i][j]=1
                make_wall(count+1)
                field[i][j]=0

n, m = map(int, input().split())
field=[]
for i in range(n):
    field.append(list(map(int, input().split())))

make_wall(0)
print(maximum)