# 촌수계산(실버2)
answer=None
def dfs(start, graph, visited, target, count):
    global answer
    if start==target:
        answer=count+1
        return    
    else:
        visited[start]=True
        for i in graph[start]:
            if visited[i] == True:
                continue
            else:
                dfs(i, graph, visited, target, count+1)
    return

n =int(input())
t1, t2 = map(int, input().split())
m = int(input())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*(n+1)


for i in range(n+1):
    if i==t1:
        for j in graph[i]:
            visited[i]=True
            dfs(j, graph, visited, t2, 0)
if answer==None:
    print(-1)
else:
    print(answer)