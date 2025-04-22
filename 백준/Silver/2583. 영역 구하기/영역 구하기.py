# 영역구하기(실버1)
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(i, j):
    total=1
    queue = deque()
    queue.append((i,j))
    visited[i][j]=1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if 0<=new_x<m and 0<=new_y<n and field[new_x][new_y]==0 and visited[new_x][new_y]==0:
                queue.append((new_x, new_y))
                total+=1
                visited[new_x][new_y]=1
    return total

m, n, k = map(int, input().split())
field=[[0]*(n) for _ in range(m)]
visited=[[0]*(n) for _ in range(m)]
for i in range(k):
    start_x, start_y, end_x, end_y = map(int, input().split())
    for j in range(start_y, end_y):
        for k in range(start_x, end_x):
            field[j][k]=1
answer_1=0
answer_2 = []
for i in range(m):
    for j in range(n):
        if field[i][j]==0 and visited[i][j]==0:
            answer_1+=1
            answer_2.append(bfs(i,j))
answer_2.sort()
print(answer_1)
print(*answer_2)