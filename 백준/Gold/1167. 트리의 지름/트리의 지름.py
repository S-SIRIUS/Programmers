# 트리의 지름(골드2)
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def dfs(node, count):
    global max_count, last_node
    visited[node]=True
    for i in graph[node]:
        if visited[i[0]]==False:
           dfs(i[0], count+i[1])
    if max_count < count:
        max_count = count
        last_node = node    
    return

v = int(input().strip())
graph=[[] for _ in range(v+1)]
for i in range(1, v+1):
    temp = list(map(int, input().strip().split()))
    for j in range(1, len(temp), 2):
        if temp[j]==-1:
            break
        else:
            graph[temp[0]].append((temp[j], temp[j+1]))
max_count=-1
last_node=0
visited = [False]*(v+1)
dfs(1, 0)
visited = [False]*(v+1)
max_count=-1
dfs(last_node, 0)
print(max_count)