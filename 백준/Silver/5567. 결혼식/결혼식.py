# 결혼식(실버2)
import sys
from collections import deque

def bfs():
    queue = deque()
    queue.append((1, 1))
    answer=0
    visited[1]=1
    while queue:
        node, level = queue.popleft()

        if level<3:
            for next_node in graph[node]:
                if visited[next_node]==0:
                    answer+=1
                    queue.append((next_node, level+1))
                    visited[next_node]=1
    return answer
n = int(input())
m = int(input())
graph=[[] for _ in range(n+1)]
visited=[0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = bfs()
print(answer)