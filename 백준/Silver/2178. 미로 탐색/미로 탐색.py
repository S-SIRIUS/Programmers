# 미로 탐색하기(실버1)
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    queue.append((0,0))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x >=0 and new_x < n and new_y>=0 and new_y < m and field[new_x][new_y]==1:
                queue.append((new_x, new_y))
                field[new_x][new_y]=field[x][y]+1

n, m = map(int, input().split())
field=[]
for i in range(n):
    temp = list(input().strip())
    field.append(list(map(int, temp)))

bfs()
print(field[n-1][m-1])