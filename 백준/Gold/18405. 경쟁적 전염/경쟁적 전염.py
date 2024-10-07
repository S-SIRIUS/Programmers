# 경쟁적 전염(골드5)
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(sorted_list, answer_x, answer_y):

    queue = deque(sorted_list)
    while queue:
        x, y, second = queue.popleft()

        if second == s:
            break

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0<=new_x<n and 0<=new_y<n and field[new_x][new_y]==0:
                field[new_x][new_y] = field[x][y]
                queue.append((new_x, new_y, second+1))

    return field[answer_x][answer_y]

n, k = map(int, input().split())
field=[]

for i in range(n):
    field.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

sorted_list=[]
for l in range(1, k+1): 
    for i in range(n):
        for j in range(n):
            if field[i][j]==l:
                sorted_list.append((i,j, 0))
print(bfs(sorted_list, x-1, y-1))