# 아기상어(골드3)
from collections import deque
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(i, j):
    queue = deque()
    queue.append((i, j, 0))
    visited = [[0]*(n) for _ in range(n)]
    visited[i][j]=1
    candidates=[]

    while queue:
        x, y, second = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0<=new_x<n and 0<=new_y<n and visited[new_x][new_y]==0 and field[new_x][new_y]<=shark_size:
                queue.append((new_x, new_y, second+1))
                visited[new_x][new_y]=1
                if 0< field[new_x][new_y]<shark_size:
                    candidates.append((second+1, new_x, new_y))
    if candidates:
        return min(candidates)
    else:
        return None

n = int(input())
field = []
start_x, start_y = 0, 0
shark_size=2
eat_num=0
for _ in range(n):
    field.append(list(map(int, input().split())))
answer=0
for i in range(n):
    for j in range(n):
        if field[i][j]==9:
            start_x = i
            start_y = j
            field[start_x][start_y]=0
            break

while True:
    flag = bfs(start_x, start_y)
    if flag==None:
        break
    else:
        s, n_x, n_y = flag
        answer+=s
        eat_num+=1
        if eat_num == shark_size:
            shark_size+=1
            eat_num=0
        start_x = n_x
        start_y = n_y
        field[n_x][n_y]=0
print(answer)