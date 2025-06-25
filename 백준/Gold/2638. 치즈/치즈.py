# 치즈(골드3)
from collections import deque
dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]


n, m = map(int, input().split())
fields = []

for i in range(n):
    fields.append(list(map(int, input().split())))

def get_outer_air():
    visited = [[0]*m for _ in range(n)]
    queue =deque()
    queue.append((0,0))
    visited[0][0]=1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m:
                if visited[nx][ny]==0 and fields[nx][ny] ==0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return visited
answer=0

while True:
    outer_air = get_outer_air()
    candidates=[]

    for i in range(n):
        for j in range(m):
            if fields[i][j]==1:
                count=0
                for k in range(4):
                    new_x = i + dx[k]
                    new_y = j + dy[k]
                    if 0<=new_x<n and 0<=new_y<m and outer_air[new_x][new_y]==1:
                        count+=1
                if count>=2:
                    candidates.append((i,j))
    if len(candidates)==0:
        print(answer)
        break
    for c in candidates:
        fields[c[0]][c[1]]=0
    answer+=1