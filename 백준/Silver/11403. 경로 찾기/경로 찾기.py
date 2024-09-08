# 경로찾기(실버1)
# start부터 다 돌아서 중간에 target을 찾으면 종료

def dfs(start,target):
    visited[start]=True
    if target in graph[start]:
        return True
    else:
        for i in graph[start]:
            if visited[i]==False:
                if (dfs(i,target)):
                    return True
    return False 
    
n = int(input())
g=[]
graph=[[] for _  in range(n)]
for i in range(n):
    g.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if g[i][j]==1:
            graph[i].append(j)

answer=[[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        visited=[False]*(n)
        if(dfs(i,j)):
            answer[i][j]=1

for i in answer:
    print(*i, end=" ")
    print()
