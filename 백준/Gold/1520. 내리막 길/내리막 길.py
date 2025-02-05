import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

def dfs(x, y):
    if x==n-1 and y==m-1:
        return 1
    
    if visited[x][y]!=-1:
        return visited[x][y]   
    
    ways=0
    for i in range(4):
        new_x, new_y = x+dx[i], y+dy[i]
        if 0<=new_x<n and 0<=new_y<m and (field[new_x][new_y] < field[x][y]):
            ways += dfs(new_x, new_y)
    visited[x][y] = ways
    return visited[x][y]

n, m = map(int, input().split())
field = []
for i in range(n):
    field.append(list(map(int, input().split())))
visited=[[-1]*m for _ in range(n)]
print(dfs(0,0))