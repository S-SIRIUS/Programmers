# DFS & BFS(실버2)
import sys
from collections import deque
input = sys.stdin.readline
def dfs(node):
    visited[node]=True
    print(node, end=" ")
    for i in graph[node]:
        if visited[i]==False:
            dfs(i)
    return

def bfs(node):
    queue = deque([node])
    visited[node]=True
    while queue:
        new_node = queue.popleft()
        print(new_node, end=" ")
        for i in graph[new_node]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True

    return

n, m, s = map(int, input().split())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()
visited=[False]*(n+1)
dfs(s)
visited=[False]*(n+1)
print()
bfs(s)