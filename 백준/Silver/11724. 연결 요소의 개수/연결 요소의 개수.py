import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline
def dfs(graph, V, visited):
    visited[V]=True
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m = map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(0,m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
ans=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        ans+=1
print(ans)