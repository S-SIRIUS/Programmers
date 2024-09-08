# 테트로미토(골드4)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def dfs(x, y, depth, total):
    global max_sum
    if depth == 4:  # 4개의 칸을 채운 경우
        value.append(total)
        return

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + field[nx][ny])
            visited[nx][ny] = False
def etc(x, y):
    if(x+2>=0 and x+2<n):
        summ=0
        summ+=field[x][y] + field[x+1][y] + field[x+2][y]
        if(y+1>=0 and y+1<m):
            summ1=summ+field[x+1][y+1]
            value.append(summ1)
        if(y-1>=0 and y-1<m):
            summ2=summ+field[x+1][y-1]
            value.append(summ2)
    if(x-2>=0 and x-2<n):
        summ=0
        summ+=field[x][y] + field[x-1][y] + field[x-2][y]
        if(y+1>=0 and y+1<m):
            summ1=summ+field[x-1][y+1]
            value.append(summ1)
        if(y-1>=0 and y-1<m):
            summ2=summ+field[x-1][y-1]
            value.append(summ2)
    if(y+2>=0 and y+2<m):
        summ=0
        summ+=field[x][y] + field[x][y+1] + field[x][y+2]
        if(x+1>=0 and x+1<n):
            summ1=summ+field[x+1][y+1]
            value.append(summ1)
        if(x-1>=0 and x-1<n):
            summ2=summ+field[x-1][y+1]
            value.append(summ2)
    if(y-2>=0 and y-2<m):
        summ=0
        summ+=field[x][y] + field[x][y-1] + field[x][y-2]
        if(x+1>=0 and x+1<n):
            summ1=summ+field[x+1][y-1]
            value.append(summ1)
        if(x-1>=0 and x-1<n):
            summ2=summ+field[x-1][y-1]
            value.append(summ2)
        


n, m = map(int, input().split())
field=[]
visited=[[False]*m for _ in range(n)]
for i in range(n):
    field.append(list(map(int, input().split())))

value=[]
for i in range(0, n):
    for j in range(0, m):
        visited[i][j] = True
        dfs(i, j, 1, field[i][j])
        visited[i][j] = False
        etc(i,j)
print(max(value))
