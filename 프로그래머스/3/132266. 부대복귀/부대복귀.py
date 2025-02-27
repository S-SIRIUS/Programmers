from collections import deque
def bfs(n, graph, sources, destination):
    queue = deque()
    visited=[-1]*(n+1)
    queue.append((destination,0))
    visited[destination]=0
    
    while queue:
        now_node, value = queue.popleft()
        if now_node in sources:
            sources.remove(now_node)
            if len(sources)==0:
                break
        for i in graph[now_node]:
            if visited[i]==-1:
                queue.append((i, value+1))
                visited[i]=value+1
    return visited
def solution(n, roads, sources, destination):
    graph=[[] for _ in range(n+1)]
    answer=[]
    for r in roads:
        graph[r[0]].append(r[1])
        graph[r[1]].append(r[0])
    
    result = bfs(n, graph, sources.copy(), destination)
    for s in sources:
        answer.append(result[s])
    return answer