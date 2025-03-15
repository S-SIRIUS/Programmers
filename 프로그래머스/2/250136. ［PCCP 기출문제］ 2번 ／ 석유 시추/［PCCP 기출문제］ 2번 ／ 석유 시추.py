from collections import deque
dx=[-1, 1, 0, 0]
dy=[0, 0, 1, -1]

def bfs(x, y, n, m, land, visited, candidates, group):
    queue = deque()
    queue.append((x,y))
    candidates.append((x,y))
    visited[x][y]=group
    count=1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]
            if 0<=new_x<n and 0<=new_y<m and land[new_x][new_y]==1 and visited[new_x][new_y]==0:
                count+=1
                candidates.append((new_x, new_y))
                visited[new_x][new_y]=group
                queue.append((new_x, new_y))
    
    return count, visited, candidates

def fill(count, filled, candidates):
    for i, j in candidates:
        filled[i][j]=count
    return filled

def find(filled, n, m, visited):
    answers=[]
    for i in range(m):
        s = set()
        answer=0
        for j in range(n):
            if filled[j][i]!=0 and visited[j][i] not in s:
                s.add(visited[j][i])
                answer +=filled[j][i]
        answers.append(answer)
    return max(answers)

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    visited=[[0]*(m) for _ in range(n)]
    filled=[[0]*(m) for _ in range(n)]
    group=1
    for i in range(n):
        for j in range(m):
            if land[i][j]==1 and visited[i][j]==0:
                candidates=[]
                count, visited, candidates = bfs(i,j, n, m,land, visited, candidates, group)
                filled = fill(count, filled, candidates)
                group+=1
    answer = find(filled, n, m, visited)
    return answer