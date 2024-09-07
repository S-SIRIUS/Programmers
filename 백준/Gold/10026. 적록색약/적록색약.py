# 적록색약 (골드5)
from collections import deque
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

def normal(x,y, target):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if(new_x>=0 and new_x<n and new_y>=0 and new_y<n and visited[new_x][new_y]==False and field[new_x][new_y]==target):
                visited[new_x][new_y]=True
                queue.append((new_x, new_y))

def abnormal(x,y, target):
    queue = deque()
    queue.append((x,y))

    if target == "R" or target == "G":
        targets = ["R", "G"]
    else:
        targets = ["B"]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if(new_x>=0 and new_x<n and new_y>=0 and new_y<n and visited[new_x][new_y]==False and field[new_x][new_y] in targets):

                visited[new_x][new_y]=True
                queue.append((new_x, new_y))

n = int(input())
field=[]
for i in range(n):
    field.append(list(input().strip()))
visited=[[False]*n for _ in range(n)]

normal_color=["R", "G", "B"]

normal_count=0
abnormal_count=0
for i in range(0, n):
    for j in range(0, n):
            if visited[i][j] == False:
                target = field[i][j]
                normal(i,j, target)
                normal_count+=1
visited=[[False]*n for _ in range(n)]
for i in range(0, n):
    for j in range(0, n):
            if visited[i][j] == False:
                target = field[i][j]
                abnormal(i,j, target)
                abnormal_count+=1
print(normal_count, abnormal_count)