from collections import deque
def bfs(graph, visited):
    queue = deque()
    queue.append(1)
    visited[1]=1
    
    while queue:
        now_node = queue.popleft()
        for i in graph[now_node]:
            if visited[i]==0:
                visited[i]=visited[now_node]+1
                queue.append(i)
    return visited

def solution(n, edge):
    answer = 0
    graph=[[] for _ in range(n+1)]
    visited=[0]*(n+1)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    visited = bfs(graph, visited)
    target = max(visited)
    for i in visited:
        if i == target:
            answer+=1
    return answer